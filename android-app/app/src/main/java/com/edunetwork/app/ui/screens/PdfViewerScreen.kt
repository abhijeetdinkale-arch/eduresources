package com.edunetwork.app.ui.screens

import android.content.Context
import android.graphics.Bitmap
import android.graphics.pdf.PdfRenderer
import android.os.ParcelFileDescriptor
import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.gestures.detectTapGestures
import androidx.compose.foundation.gestures.detectTransformGestures
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.statusBarsPadding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.rememberLazyListState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material.icons.filled.Key
import androidx.compose.material.icons.filled.Lock
import androidx.compose.material.icons.filled.RestartAlt
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.derivedStateOf
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateMapOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.edunetwork.app.data.model.MaterialItem
import com.edunetwork.app.data.repository.AuthRepository
import com.edunetwork.app.ui.components.AppleGlassSurface
import com.edunetwork.app.ui.components.SpotifyLoginModal
import com.edunetwork.app.ui.theme.Gold400
import com.edunetwork.app.ui.theme.Gold500
import com.edunetwork.app.ui.theme.Obsidian950
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import java.io.File
import java.io.FileOutputStream

@Composable
fun PdfViewerScreen(
    material: MaterialItem,
    onBack: () -> Unit,
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current
    val authRepo = remember { AuthRepository.getInstance(context) }
    var isAuthorized by remember { mutableStateOf(authRepo.isAuthorized()) }
    var showLoginModal by remember { mutableStateOf(false) }

    var pdfRenderer by remember { mutableStateOf<PdfRenderer?>(null) }
    var fileDescriptor by remember { mutableStateOf<ParcelFileDescriptor?>(null) }
    var totalPages by remember { mutableIntStateOf(0) }
    var isLoading by remember { mutableStateOf(true) }
    var errorMessage by remember { mutableStateOf<String?>(null) }

    val pageBitmaps = remember { mutableStateMapOf<Int, Bitmap>() }
    val listState = rememberLazyListState()

    var scale by remember { mutableFloatStateOf(1f) }
    var offset by remember { mutableStateOf(Offset.Zero) }

    // Free sample limit: 3 pages free for visitors, all pages for authorized members
    val accessiblePages = if (isAuthorized) totalPages else totalPages.coerceAtMost(3)

    val activePage by remember {
        derivedStateOf {
            if (totalPages > 0) (listState.firstVisibleItemIndex + 1).coerceAtMost(totalPages) else 1
        }
    }

    LaunchedEffect(material.id) {
        isLoading = true
        withContext(Dispatchers.IO) {
            try {
                val cacheFile = File(context.cacheDir, "${material.id}.pdf")
                if (!cacheFile.exists() || cacheFile.length() == 0L) {
                    val assetPath = material.bundledFile
                    context.assets.open(assetPath).use { input ->
                        FileOutputStream(cacheFile).use { output ->
                            input.copyTo(output)
                        }
                    }
                }

                val pfd = ParcelFileDescriptor.open(cacheFile, ParcelFileDescriptor.MODE_READ_ONLY)
                val renderer = PdfRenderer(pfd)
                fileDescriptor = pfd
                pdfRenderer = renderer
                totalPages = renderer.pageCount
                isLoading = false
            } catch (e: Exception) {
                e.printStackTrace()
                errorMessage = "Failed to load document: ${e.localizedMessage}"
                isLoading = false
            }
        }
    }

    DisposableEffect(Unit) {
        onDispose {
            try {
                pdfRenderer?.close()
                fileDescriptor?.close()
                pageBitmaps.clear()
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }

    val isDark = MaterialTheme.colorScheme.background.red < 0.2f
    val solidViewerBg = if (isDark) Color(0xFF000000) else Color(0xFFF2F2F7)

    Box(
        modifier = modifier
            .fillMaxSize()
            .background(solidViewerBg)
            .pointerInput(Unit) {
                detectTransformGestures { _, pan, zoom, _ ->
                    val newScale = (scale * zoom).coerceIn(1f, 4f)
                    scale = newScale
                    if (newScale > 1f) {
                        offset = Offset(x = offset.x + pan.x, y = offset.y + pan.y)
                    } else {
                        offset = Offset.Zero
                    }
                }
            }
            .pointerInput(Unit) {
                detectTapGestures(
                    onDoubleTap = {
                        if (scale > 1.05f) {
                            scale = 1f
                            offset = Offset.Zero
                        } else {
                            scale = 2.2f
                        }
                    }
                )
            }
    ) {
        if (isLoading) {
            Column(
                modifier = Modifier.align(Alignment.Center),
                horizontalAlignment = Alignment.CenterHorizontally
            ) {
                CircularProgressIndicator(color = Gold500, strokeWidth = 2.5.dp)
                Spacer(modifier = Modifier.height(14.dp))
                Text(
                    text = "Opening Archival Edition...",
                    style = MaterialTheme.typography.bodyMedium,
                    color = if (isDark) Color.White else Color(0xFF18181B)
                )
            }
        } else if (errorMessage != null) {
            Column(
                modifier = Modifier
                    .align(Alignment.Center)
                    .padding(32.dp),
                horizontalAlignment = Alignment.CenterHorizontally
            ) {
                Icon(
                    imageVector = Icons.Filled.Lock,
                    contentDescription = null,
                    tint = Color(0xFFEF4444),
                    modifier = Modifier.size(48.dp)
                )
                Spacer(modifier = Modifier.height(12.dp))
                Text(
                    text = "Access Protected",
                    style = MaterialTheme.typography.titleMedium.copy(fontWeight = FontWeight.Bold),
                    color = Color.White
                )
                Spacer(modifier = Modifier.height(6.dp))
                Text(
                    text = errorMessage ?: "Unknown error",
                    style = MaterialTheme.typography.bodySmall,
                    color = Color(0xFFA1A1AA)
                )
            }
        } else {
            // Continuous High-Performance Page Viewport
            LazyColumn(
                state = listState,
                contentPadding = PaddingValues(
                    top = 74.dp,
                    bottom = 90.dp,
                    start = 12.dp,
                    end = 12.dp
                ),
                verticalArrangement = Arrangement.spacedBy(14.dp),
                modifier = Modifier
                    .fillMaxSize()
                    .graphicsLayer {
                        scaleX = scale
                        scaleY = scale
                        translationX = offset.x
                        translationY = offset.y
                    }
            ) {
                // Free sample pages or all pages if authorized
                items(accessiblePages) { pageIndex ->
                    PdfPageCard(
                        pageIndex = pageIndex,
                        pdfRenderer = pdfRenderer,
                        cachedBitmap = pageBitmaps[pageIndex],
                        onBitmapLoaded = { bmp -> pageBitmaps[pageIndex] = bmp }
                    )
                }

                // If unauthorized and more pages exist -> Spotify-style Sample Lock Card
                if (!isAuthorized && totalPages > 3) {
                    item {
                        Surface(
                            shape = RoundedCornerShape(24.dp),
                            color = if (isDark) Color(0xFF14141B) else Color.White,
                            border = BorderStroke(1.dp, if (isDark) Gold500.copy(alpha = 0.5f) else Color(0xFFE4E4E7)),
                            shadowElevation = 12.dp,
                            modifier = Modifier
                                .fillMaxWidth()
                                .padding(vertical = 12.dp)
                        ) {
                            Column(
                                modifier = Modifier.padding(24.dp),
                                horizontalAlignment = Alignment.CenterHorizontally
                            ) {
                                Surface(
                                    shape = CircleShape,
                                    color = Color(0x25E5C05B),
                                    modifier = Modifier.size(52.dp)
                                ) {
                                    Box(contentAlignment = Alignment.Center) {
                                        Icon(
                                            imageVector = Icons.Filled.Lock,
                                            contentDescription = null,
                                            tint = Gold400,
                                            modifier = Modifier.size(24.dp)
                                        )
                                    }
                                }

                                Spacer(modifier = Modifier.height(14.dp))

                                Text(
                                    text = "Sample Preview Ended",
                                    style = MaterialTheme.typography.titleMedium.copy(
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 18.sp
                                    ),
                                    color = if (isDark) Color.White else Color(0xFF18181B)
                                )

                                Spacer(modifier = Modifier.height(4.dp))

                                Text(
                                    text = "Unlock all $totalPages pages with Google Sign-In or Secret Member Passcode.",
                                    style = MaterialTheme.typography.bodySmall,
                                    color = Color(0xFFA1A1AA),
                                    textAlign = TextAlign.Center
                                )

                                Spacer(modifier = Modifier.height(18.dp))

                                Button(
                                    onClick = { showLoginModal = true },
                                    modifier = Modifier
                                        .fillMaxWidth()
                                        .height(48.dp),
                                    shape = RoundedCornerShape(24.dp),
                                    colors = ButtonDefaults.buttonColors(
                                        containerColor = Gold500,
                                        contentColor = Obsidian950
                                    )
                                ) {
                                    Icon(
                                        imageVector = Icons.Filled.Key,
                                        contentDescription = null,
                                        modifier = Modifier.size(16.dp)
                                    )
                                    Spacer(modifier = Modifier.width(8.dp))
                                    Text(
                                        text = "UNLOCK FULL BOOK (SIGN IN)",
                                        style = MaterialTheme.typography.labelMedium.copy(
                                            fontWeight = FontWeight.Bold,
                                            fontSize = 12.sp
                                        )
                                    )
                                }
                            }
                        }
                    }
                }
            }
        }

        // Floating Top Navigation Header
        AppleGlassSurface(
            shape = RoundedCornerShape(bottomStart = 24.dp, bottomEnd = 24.dp),
            tonalElevation = 16.dp,
            modifier = Modifier
                .fillMaxWidth()
                .align(Alignment.TopCenter)
                .statusBarsPadding()
        ) {
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(horizontal = 12.dp, vertical = 8.dp),
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.SpaceBetween
            ) {
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    modifier = Modifier.weight(1f)
                ) {
                    IconButton(onClick = onBack) {
                        Icon(
                            imageVector = Icons.Filled.ArrowBack,
                            contentDescription = "Back",
                            tint = if (isDark) Color.White else Color(0xFF18181B)
                        )
                    }
                    Spacer(modifier = Modifier.width(4.dp))
                    Column {
                        Text(
                            text = material.title,
                            style = MaterialTheme.typography.titleMedium.copy(
                                fontSize = 13.5.sp,
                                fontWeight = FontWeight.Bold
                            ),
                            color = if (isDark) Color.White else Color(0xFF18181B),
                            maxLines = 1,
                            overflow = TextOverflow.Ellipsis
                        )
                        Text(
                            text = if (isAuthorized) "${material.courseCode} • Full Pass Access" else "${material.courseCode} • Free Sample Preview",
                            style = MaterialTheme.typography.labelSmall.copy(
                                fontSize = 9.5.sp,
                                fontFamily = FontFamily.Monospace
                            ),
                            color = Gold400
                        )
                    }
                }

                if (scale > 1.05f) {
                    IconButton(onClick = { scale = 1f; offset = Offset.Zero }) {
                        Icon(
                            imageVector = Icons.Filled.RestartAlt,
                            contentDescription = "Reset Zoom",
                            tint = Gold400,
                            modifier = Modifier.size(18.dp)
                        )
                    }
                }
            }
        }

        // Floating Bottom Page Scrubber Pill
        if (totalPages > 0) {
            AppleGlassSurface(
                shape = RoundedCornerShape(24.dp),
                tonalElevation = 16.dp,
                modifier = Modifier
                    .align(Alignment.BottomCenter)
                    .navigationBarsPadding()
                    .padding(bottom = 14.dp)
            ) {
                Row(
                    modifier = Modifier.padding(horizontal = 14.dp, vertical = 6.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Text(
                        text = "PAGE $activePage / $totalPages",
                        style = MaterialTheme.typography.labelSmall.copy(
                            fontFamily = FontFamily.Monospace,
                            fontSize = 11.sp,
                            fontWeight = FontWeight.Bold
                        ),
                        color = if (isDark) Color.White else Color(0xFF18181B)
                    )
                }
            }
        }

        // Spotify Login Modal
        SpotifyLoginModal(
            isOpen = showLoginModal,
            onClose = { showLoginModal = false },
            onLoginSuccess = {
                isAuthorized = true
            }
        )
    }
}

@Composable
private fun PdfPageCard(
    pageIndex: Int,
    pdfRenderer: PdfRenderer?,
    cachedBitmap: Bitmap?,
    onBitmapLoaded: (Bitmap) -> Unit
) {
    var bitmap by remember(pageIndex, cachedBitmap) { mutableStateOf(cachedBitmap) }

    LaunchedEffect(pageIndex, pdfRenderer) {
        if (bitmap != null) return@LaunchedEffect
        val renderer = pdfRenderer ?: return@LaunchedEffect

        withContext(Dispatchers.IO) {
            try {
                val page = renderer.openPage(pageIndex)
                val density = 2.0f
                val width = (page.width * density).toInt()
                val height = (page.height * density).toInt()

                val newBitmap = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888)
                newBitmap.eraseColor(android.graphics.Color.WHITE)
                page.render(newBitmap, null, null, PdfRenderer.Page.RENDER_MODE_FOR_DISPLAY)
                page.close()

                withContext(Dispatchers.Main) {
                    bitmap = newBitmap
                    onBitmapLoaded(newBitmap)
                }
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }

    Surface(
        shape = RoundedCornerShape(10.dp),
        color = Color.White,
        shadowElevation = 4.dp,
        modifier = Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(10.dp))
    ) {
        if (bitmap != null) {
            Image(
                bitmap = bitmap!!.asImageBitmap(),
                contentDescription = "Page ${pageIndex + 1}",
                contentScale = ContentScale.FillWidth,
                modifier = Modifier.fillMaxWidth()
            )
        } else {
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .height(420.dp)
                    .background(Color(0xFFE4E4E7)),
                contentAlignment = Alignment.Center
            ) {
                CircularProgressIndicator(
                    color = Gold400,
                    strokeWidth = 2.dp,
                    modifier = Modifier.size(22.dp)
                )
            }
        }
    }
}

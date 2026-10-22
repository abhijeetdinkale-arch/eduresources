package com.edunetwork.app.ui.screens

import android.widget.Toast
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.statusBarsPadding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowForward
import androidx.compose.material.icons.filled.AutoAwesome
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.DarkMode
import androidx.compose.material.icons.filled.Key
import androidx.compose.material.icons.filled.LightMode
import androidx.compose.material.icons.filled.Logout
import androidx.compose.material.icons.filled.Person
import androidx.compose.material.icons.filled.Search
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.OutlinedTextFieldDefaults
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.edunetwork.app.R
import com.edunetwork.app.data.model.CourseDossier
import com.edunetwork.app.data.repository.AuthRepository
import com.edunetwork.app.data.repository.MaterialRepository
import com.edunetwork.app.ui.components.AppBackground
import com.edunetwork.app.ui.components.SpotifyLoginModal
import com.edunetwork.app.ui.components.SubjectFolderCard
import com.edunetwork.app.ui.theme.Gold400
import com.edunetwork.app.ui.theme.Gold500
import com.edunetwork.app.ui.theme.Obsidian950

@Composable
fun HomeScreen(
    repository: MaterialRepository,
    onOpenCourse: (String) -> Unit,
    onBrowseDossiers: () -> Unit,
    onNavigateToPlans: () -> Unit,
    onOpenPracticeExam: () -> Unit = {},
    onToggleDarkTheme: () -> Unit = {},
    isDarkTheme: Boolean = true,
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current
    val authRepo = remember { AuthRepository.getInstance(context) }

    var courses by remember { mutableStateOf<List<CourseDossier>>(emptyList()) }
    var userSession by remember { mutableStateOf(authRepo.getUserSession()) }
    var showProfileDialog by remember { mutableStateOf(false) }
    var showLoginModal by remember { mutableStateOf(false) }
    var searchQuery by remember { mutableStateOf("") }

    LaunchedEffect(Unit) {
        courses = repository.getCourseDossiers()
    }

    val isDark = isDarkTheme
    val isSubscribed = userSession != null

    AppBackground(modifier = modifier.fillMaxSize(), isDark = isDark) {
        LazyColumn(
            modifier = Modifier
                .fillMaxSize()
                .statusBarsPadding(),
            contentPadding = PaddingValues(start = 18.dp, end = 18.dp, top = 12.dp, bottom = 100.dp),
            verticalArrangement = Arrangement.spacedBy(18.dp)
        ) {
            // =========================================================================
            // 1. TOP EDITORIAL STICKY HEADER (Matching Web Navbar)
            // =========================================================================
            item {
                Surface(
                    shape = RoundedCornerShape(32.dp),
                    color = if (isDark) Color(0xFF14141B).copy(alpha = 0.95f) else Color(0xFFFAF8F5).copy(alpha = 0.95f),
                    border = BorderStroke(1.dp, if (isDark) Color(0x33FFFFFF) else Color(0x22000000)),
                    shadowElevation = 4.dp,
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Row(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(horizontal = 14.dp, vertical = 10.dp),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        // Left: Celestial Star Logo Disc + Brand
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            modifier = Modifier.clickable { onBrowseDossiers() }
                        ) {
                            Surface(
                                shape = CircleShape,
                                color = if (isDark) Color(0xFFFAF8F5) else Color(0xFF18181B),
                                border = BorderStroke(1.dp, if (isDark) Color(0x33FFFFFF) else Color(0x22000000)),
                                shadowElevation = 2.dp,
                                modifier = Modifier.size(36.dp)
                            ) {
                                Box(
                                    contentAlignment = Alignment.Center,
                                    modifier = Modifier.padding(6.dp)
                                ) {
                                    Image(
                                        painter = painterResource(id = R.drawable.logo),
                                        contentDescription = "Edu network star logo",
                                        contentScale = ContentScale.Fit,
                                        modifier = Modifier.size(24.dp)
                                    )
                                }
                            }

                            Spacer(modifier = Modifier.width(10.dp))

                            Column {
                                Row(verticalAlignment = Alignment.CenterVertically) {
                                    Text(
                                        text = "Edu ",
                                        style = MaterialTheme.typography.titleMedium.copy(
                                            fontWeight = FontWeight.Black,
                                            fontSize = 16.sp,
                                            letterSpacing = (-0.3).sp
                                        ),
                                        color = if (isDark) Color(0xFFFAF8F5) else Color(0xFF18181B)
                                    )
                                    Text(
                                        text = "network",
                                        style = MaterialTheme.typography.titleMedium.copy(
                                            fontWeight = FontWeight.Normal,
                                            fontSize = 16.sp,
                                            letterSpacing = (-0.3).sp
                                        ),
                                        color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)
                                    )
                                }
                                Text(
                                    text = "• ARCHIVE 2026",
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontFamily = FontFamily.Monospace,
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 9.sp,
                                        letterSpacing = 1.sp
                                    ),
                                    color = Gold400
                                )
                            }
                        }

                        // Right: Keycard Pill + Dark Mode Switcher
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.spacedBy(8.dp)
                        ) {
                            // User Auth / Keycard Pill
                            Surface(
                                shape = RoundedCornerShape(20.dp),
                                color = if (isSubscribed) {
                                    if (isDark) Color(0x3310B981) else Color(0xFFD1FAE5)
                                } else {
                                    if (isDark) Color(0xFF1E1E28) else Color(0xFFE4E4E7)
                                },
                                border = BorderStroke(
                                    1.dp,
                                    if (isSubscribed) Color(0xFF10B981) else if (isDark) Color(0x33FFFFFF) else Color(0x22000000)
                                ),
                                modifier = Modifier.clickable {
                                    if (authRepo.isAuthorized()) {
                                        showProfileDialog = true
                                    } else {
                                        showLoginModal = true
                                    }
                                }
                            ) {
                                Row(
                                    modifier = Modifier.padding(horizontal = 10.dp, vertical = 6.dp),
                                    verticalAlignment = Alignment.CenterVertically
                                ) {
                                    Icon(
                                        imageVector = if (isSubscribed) Icons.Filled.Key else Icons.Filled.Person,
                                        contentDescription = null,
                                        tint = if (isSubscribed) Color(0xFF059669) else if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A),
                                        modifier = Modifier.size(13.dp)
                                    )
                                    Spacer(modifier = Modifier.width(5.dp))
                                    Text(
                                        text = if (isSubscribed) "PASS ACTIVE" else "LOGIN",
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontFamily = FontFamily.Monospace,
                                            fontWeight = FontWeight.Bold,
                                            fontSize = 10.sp
                                        ),
                                        color = if (isSubscribed) {
                                            if (isDark) Color(0xFF34D399) else Color(0xFF065F46)
                                        } else {
                                            if (isDark) Color(0xFFE4E4E7) else Color(0xFF27272A)
                                        }
                                    )
                                }
                            }

                            // 1-Tap Theme Mode Switcher (☀️/🌙)
                            Surface(
                                shape = CircleShape,
                                color = if (isDark) Color(0xFF1E1E28) else Color.White,
                                border = BorderStroke(1.dp, if (isDark) Color(0x33FFFFFF) else Color(0x22000000)),
                                modifier = Modifier
                                    .size(36.dp)
                                    .clickable { onToggleDarkTheme() }
                            ) {
                                Box(contentAlignment = Alignment.Center) {
                                    Icon(
                                        imageVector = if (isDark) Icons.Filled.LightMode else Icons.Filled.DarkMode,
                                        contentDescription = "Toggle Theme",
                                        tint = if (isDark) Gold400 else Color(0xFF18181B),
                                        modifier = Modifier.size(17.dp)
                                    )
                                }
                            }
                        }
                    }
                }
            }

            // =========================================================================
            // 2. EDITORIAL HERO SECTION (Matching Web Design)
            // =========================================================================
            item {
                Surface(
                    shape = RoundedCornerShape(32.dp),
                    color = if (isDark) Color(0xFF14141B) else Color(0xFFFAF8F5),
                    border = BorderStroke(1.2.dp, if (isDark) Color(0x33FFFFFF) else Color(0x22000000)),
                    shadowElevation = 8.dp,
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Box(modifier = Modifier.fillMaxWidth()) {
                        // Background Celestial Star Watermark
                        Box(
                            modifier = Modifier
                                .align(Alignment.TopEnd)
                                .padding(top = 16.dp, end = 16.dp)
                                .size(140.dp)
                        ) {
                            Image(
                                painter = painterResource(id = R.drawable.logo),
                                contentDescription = null,
                                contentScale = ContentScale.Fit,
                                alpha = if (isDark) 0.08f else 0.06f,
                                modifier = Modifier.fillMaxSize()
                            )
                        }

                        Column(
                            modifier = Modifier
                                .fillMaxWidth()
                                .padding(22.dp)
                        ) {
                            // Status Pill Badge
                            Surface(
                                shape = RoundedCornerShape(20.dp),
                                color = if (isDark) Color(0xFF1E1E28) else Color(0xFFEFECE6),
                                border = BorderStroke(1.dp, if (isDark) Color(0x33FFFFFF) else Color(0x22000000))
                            ) {
                                Row(
                                    modifier = Modifier.padding(horizontal = 12.dp, vertical = 6.dp),
                                    verticalAlignment = Alignment.CenterVertically
                                ) {
                                    if (isSubscribed) {
                                        Icon(
                                            imageVector = Icons.Filled.CheckCircle,
                                            contentDescription = null,
                                            tint = Color(0xFF10B981),
                                            modifier = Modifier.size(13.dp)
                                        )
                                        Spacer(modifier = Modifier.width(6.dp))
                                        Text(
                                            text = "ACTIVE SCHOLAR PASS • UNLIMITED VAULT ACCESS",
                                            style = MaterialTheme.typography.labelSmall.copy(
                                                fontFamily = FontFamily.Monospace,
                                                fontWeight = FontWeight.Bold,
                                                fontSize = 9.5.sp,
                                                letterSpacing = 0.5.sp
                                            ),
                                            color = if (isDark) Color(0xFF34D399) else Color(0xFF065F46)
                                        )
                                    } else {
                                        Surface(
                                            shape = CircleShape,
                                            color = Gold500,
                                            modifier = Modifier.size(6.dp)
                                        ) {}
                                        Spacer(modifier = Modifier.width(6.dp))
                                        Text(
                                            text = "OFFICIAL SYLLABUS TEXTS • IN-APP DIGITAL READER",
                                            style = MaterialTheme.typography.labelSmall.copy(
                                                fontFamily = FontFamily.Monospace,
                                                fontWeight = FontWeight.Bold,
                                                fontSize = 9.5.sp,
                                                letterSpacing = 0.5.sp
                                            ),
                                            color = if (isDark) Color(0xFFE4E4E7) else Color(0xFF3F3F46)
                                        )
                                    }
                                }
                            }

                            Spacer(modifier = Modifier.height(18.dp))

                            // Large Editorial Headline
                            Text(
                                text = "Interactive online\nstudy education",
                                style = MaterialTheme.typography.headlineLarge.copy(
                                    fontWeight = FontWeight.Black,
                                    fontSize = 28.sp,
                                    lineHeight = 33.sp,
                                    letterSpacing = (-0.5).sp
                                ),
                                color = if (isDark) Color(0xFFFAF8F5) else Color(0xFF18181B)
                            )
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Text(
                                    text = "that inspires",
                                    style = MaterialTheme.typography.headlineLarge.copy(
                                        fontStyle = FontStyle.Italic,
                                        fontWeight = FontWeight.Normal,
                                        fontSize = 28.sp,
                                        lineHeight = 33.sp
                                    ),
                                    color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF52525B)
                                )
                                Spacer(modifier = Modifier.width(6.dp))
                                Text(
                                    text = "✦",
                                    style = MaterialTheme.typography.headlineLarge.copy(
                                        fontSize = 22.sp
                                    ),
                                    color = Gold400
                                )
                            }

                            Spacer(modifier = Modifier.height(12.dp))

                            // Subtitle Paragraph
                            Text(
                                text = "Discover the joy of studying through our vibrant academic repository, where passionate educators and students share certified curriculum textbooks, verified question banks, and intelligent AI study assistance.",
                                style = MaterialTheme.typography.bodyMedium.copy(
                                    fontSize = 12.5.sp,
                                    lineHeight = 18.sp
                                ),
                                color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)
                            )

                            Spacer(modifier = Modifier.height(18.dp))

                            // Hero Action Buttons
                            Column(
                                verticalArrangement = Arrangement.spacedBy(10.dp),
                                modifier = Modifier.fillMaxWidth()
                            ) {
                                // 1. Open Dossiers Primary Button
                                Surface(
                                    shape = RoundedCornerShape(24.dp),
                                    color = if (isDark) Color(0xFFFAF8F5) else Color(0xFF18181B),
                                    shadowElevation = 4.dp,
                                    modifier = Modifier
                                        .fillMaxWidth()
                                        .height(48.dp)
                                        .clickable { onBrowseDossiers() }
                                ) {
                                    Row(
                                        modifier = Modifier.fillMaxSize(),
                                        verticalAlignment = Alignment.CenterVertically,
                                        horizontalArrangement = Arrangement.Center
                                    ) {
                                        Text(
                                            text = if (isSubscribed) "OPEN MY SUBJECT DOSSIERS" else "BROWSE SUBJECT FOLDERS",
                                            style = MaterialTheme.typography.titleMedium.copy(
                                                fontWeight = FontWeight.Bold,
                                                fontSize = 12.sp,
                                                letterSpacing = 0.8.sp
                                            ),
                                            color = if (isDark) Color(0xFF18181B) else Color(0xFFFAF8F5)
                                        )
                                        Spacer(modifier = Modifier.width(8.dp))
                                        Icon(
                                            imageVector = Icons.Filled.ArrowForward,
                                            contentDescription = null,
                                            tint = if (isDark) Color(0xFF18181B) else Color(0xFFFAF8F5),
                                            modifier = Modifier.size(15.dp)
                                        )
                                    }
                                }

                                // 2. Practice Exams (Midterm) Amber Button
                                Surface(
                                    shape = RoundedCornerShape(24.dp),
                                    color = Color(0xFFF59E0B),
                                    shadowElevation = 4.dp,
                                    modifier = Modifier
                                        .fillMaxWidth()
                                        .height(48.dp)
                                        .clickable { onOpenPracticeExam() }
                                ) {
                                    Row(
                                        modifier = Modifier.fillMaxSize(),
                                        verticalAlignment = Alignment.CenterVertically,
                                        horizontalArrangement = Arrangement.Center
                                    ) {
                                        Icon(
                                            imageVector = Icons.Filled.AutoAwesome,
                                            contentDescription = null,
                                            tint = Color(0xFF18181B),
                                            modifier = Modifier.size(16.dp)
                                        )
                                        Spacer(modifier = Modifier.width(8.dp))
                                        Text(
                                            text = "PRACTICE EXAMS (MIDTERM)",
                                            style = MaterialTheme.typography.titleMedium.copy(
                                                fontWeight = FontWeight.Black,
                                                fontSize = 12.sp,
                                                letterSpacing = 0.8.sp
                                            ),
                                            color = Color(0xFF18181B)
                                        )
                                        Spacer(modifier = Modifier.width(8.dp))
                                        Surface(
                                            shape = RoundedCornerShape(10.dp),
                                            color = Color(0xFF18181B)
                                        ) {
                                            Text(
                                                text = "NEW",
                                                style = MaterialTheme.typography.labelSmall.copy(
                                                    fontFamily = FontFamily.Monospace,
                                                    fontWeight = FontWeight.Bold,
                                                    fontSize = 8.5.sp
                                                ),
                                                color = Color(0xFFFCD34D),
                                                modifier = Modifier.padding(horizontal = 6.dp, vertical = 2.dp)
                                            )
                                        }
                                    }
                                }
                            }

                            Spacer(modifier = Modifier.height(20.dp))

                            // 4 Metric Badges in 2x2 Grid (Matching Web UI)
                            Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                                Row(
                                    modifier = Modifier.fillMaxWidth(),
                                    horizontalArrangement = Arrangement.spacedBy(8.dp)
                                ) {
                                    // 12k+ Students
                                    Surface(
                                        shape = RoundedCornerShape(16.dp),
                                        color = if (isDark) Color(0xFF1A1A24) else Color.White,
                                        border = BorderStroke(1.dp, if (isDark) Color(0x33FFFFFF) else Color(0x22000000)),
                                        modifier = Modifier.weight(1f)
                                    ) {
                                        Column(modifier = Modifier.padding(12.dp)) {
                                            Text(
                                                text = "12k+",
                                                style = MaterialTheme.typography.titleLarge.copy(
                                                    fontWeight = FontWeight.Black,
                                                    fontSize = 18.sp
                                                ),
                                                color = if (isDark) Color(0xFFFAF8F5) else Color(0xFF18181B)
                                            )
                                            Text(
                                                text = "Students served",
                                                style = MaterialTheme.typography.bodySmall.copy(fontSize = 10.5.sp),
                                                color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)
                                            )
                                        }
                                    }

                                    // 34k Hours
                                    Surface(
                                        shape = RoundedCornerShape(16.dp),
                                        color = if (isDark) Color(0xFF1A1A24) else Color.White,
                                        border = BorderStroke(1.dp, if (isDark) Color(0x33FFFFFF) else Color(0x22000000)),
                                        modifier = Modifier.weight(1f)
                                    ) {
                                        Column(modifier = Modifier.padding(12.dp)) {
                                            Text(
                                                text = "34k",
                                                style = MaterialTheme.typography.titleLarge.copy(
                                                    fontWeight = FontWeight.Black,
                                                    fontSize = 18.sp
                                                ),
                                                color = if (isDark) Color(0xFFFAF8F5) else Color(0xFF18181B)
                                            )
                                            Text(
                                                text = "Hours of study",
                                                style = MaterialTheme.typography.bodySmall.copy(fontSize = 10.5.sp),
                                                color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)
                                            )
                                        }
                                    }
                                }

                                Row(
                                    modifier = Modifier.fillMaxWidth(),
                                    horizontalArrangement = Arrangement.spacedBy(8.dp)
                                ) {
                                    // 18 Course Dossiers
                                    Surface(
                                        shape = RoundedCornerShape(16.dp),
                                        color = if (isDark) Color(0xFF1A1A24) else Color.White,
                                        border = BorderStroke(1.dp, if (isDark) Color(0x33FFFFFF) else Color(0x22000000)),
                                        modifier = Modifier.weight(1f)
                                    ) {
                                        Column(modifier = Modifier.padding(12.dp)) {
                                            Text(
                                                text = "18",
                                                style = MaterialTheme.typography.titleLarge.copy(
                                                    fontWeight = FontWeight.Black,
                                                    fontSize = 18.sp
                                                ),
                                                color = if (isDark) Color(0xFFFAF8F5) else Color(0xFF18181B)
                                            )
                                            Text(
                                                text = "Course Dossiers",
                                                style = MaterialTheme.typography.bodySmall.copy(fontSize = 10.5.sp),
                                                color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)
                                            )
                                        }
                                    }

                                    // 4.9 ★ Rating
                                    Surface(
                                        shape = RoundedCornerShape(16.dp),
                                        color = if (isDark) Color(0xFF1A1A24) else Color.White,
                                        border = BorderStroke(1.dp, if (isDark) Color(0x33FFFFFF) else Color(0x22000000)),
                                        modifier = Modifier.weight(1f)
                                    ) {
                                        Column(modifier = Modifier.padding(12.dp)) {
                                            Text(
                                                text = "4.9 ★",
                                                style = MaterialTheme.typography.titleLarge.copy(
                                                    fontWeight = FontWeight.Black,
                                                    fontSize = 18.sp
                                                ),
                                                color = Gold500
                                            )
                                            Text(
                                                text = "Faculty Rating",
                                                style = MaterialTheme.typography.bodySmall.copy(fontSize = 10.5.sp),
                                                color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)
                                            )
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }

            // =========================================================================
            // 3. MIDTERM EXAMINATION SUITE SPOTLIGHT BANNER (Matching Web Section)
            // =========================================================================
            item {
                Surface(
                    shape = RoundedCornerShape(32.dp),
                    color = Color.Transparent,
                    border = BorderStroke(1.2.dp, Color(0x446366F1)),
                    shadowElevation = 8.dp,
                    modifier = Modifier
                        .fillMaxWidth()
                        .clickable { onOpenPracticeExam() }
                ) {
                    Box(
                        modifier = Modifier
                            .fillMaxWidth()
                            .background(
                                Brush.linearGradient(
                                    listOf(
                                        Color(0xFF1E1B4B),
                                        Color(0xFF0F172A),
                                        Color(0xFF18181B)
                                    )
                                ),
                                RoundedCornerShape(32.dp)
                            )
                            .padding(22.dp)
                    ) {
                        Column {
                            // Spotlight Pill
                            Surface(
                                shape = RoundedCornerShape(16.dp),
                                color = Color(0x33F59E0B),
                                border = BorderStroke(1.dp, Color(0x66F59E0B))
                            ) {
                                Row(
                                    modifier = Modifier.padding(horizontal = 10.dp, vertical = 4.dp),
                                    verticalAlignment = Alignment.CenterVertically
                                ) {
                                    Surface(
                                        shape = CircleShape,
                                        color = Color(0xFFFCD34D),
                                        modifier = Modifier.size(6.dp)
                                    ) {}
                                    Spacer(modifier = Modifier.width(6.dp))
                                    Text(
                                        text = "NEW FEATURE • MIDTERM EXAMINATION SUITE",
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontFamily = FontFamily.Monospace,
                                            fontWeight = FontWeight.Bold,
                                            fontSize = 9.sp
                                        ),
                                        color = Color(0xFFFCD34D)
                                    )
                                }
                            }

                            Spacer(modifier = Modifier.height(14.dp))

                            Text(
                                text = "Master Your Midterms with 5 Timed Mock Exams",
                                style = MaterialTheme.typography.titleLarge.copy(
                                    fontWeight = FontWeight.Black,
                                    fontSize = 19.sp,
                                    lineHeight = 24.sp
                                ),
                                color = Color.White
                            )

                            Spacer(modifier = Modifier.height(6.dp))

                            Text(
                                text = "Experience the authentic university midterm environment with exact 90-minute timers, 30 MCQs, realistic +1.0 / -0.25 negative marking, and step-by-step animated solutions.",
                                style = MaterialTheme.typography.bodySmall.copy(
                                    fontSize = 12.sp,
                                    lineHeight = 17.sp
                                ),
                                color = Color(0xFFCBD5E1)
                            )

                            Spacer(modifier = Modifier.height(14.dp))

                            // Features Row
                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.spacedBy(6.dp)
                            ) {
                                Surface(
                                    shape = RoundedCornerShape(8.dp),
                                    color = Color.White.copy(alpha = 0.12f)
                                ) {
                                    Text(
                                        text = "90 Mins",
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontSize = 9.5.sp,
                                            fontWeight = FontWeight.SemiBold
                                        ),
                                        color = Color.White,
                                        modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp)
                                    )
                                }

                                Surface(
                                    shape = RoundedCornerShape(8.dp),
                                    color = Color.White.copy(alpha = 0.12f)
                                ) {
                                    Text(
                                        text = "30 MCQs",
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontSize = 9.5.sp,
                                            fontWeight = FontWeight.SemiBold
                                        ),
                                        color = Color.White,
                                        modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp)
                                    )
                                }

                                Surface(
                                    shape = RoundedCornerShape(8.dp),
                                    color = Color(0x33EF4444)
                                ) {
                                    Text(
                                        text = "-0.25 Penalty",
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontSize = 9.5.sp,
                                            fontWeight = FontWeight.Bold
                                        ),
                                        color = Color(0xFFFCA5A5),
                                        modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp)
                                    )
                                }

                                Surface(
                                    shape = RoundedCornerShape(8.dp),
                                    color = Color(0x33F59E0B)
                                ) {
                                    Text(
                                        text = "Solutions",
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontSize = 9.5.sp,
                                            fontWeight = FontWeight.Bold
                                        ),
                                        color = Color(0xFFFDE68A),
                                        modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp)
                                    )
                                }
                            }

                            Spacer(modifier = Modifier.height(16.dp))

                            // Launch Button
                            Surface(
                                shape = RoundedCornerShape(20.dp),
                                color = Color(0xFFF59E0B),
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .height(44.dp)
                                    .clickable { onOpenPracticeExam() }
                            ) {
                                Row(
                                    modifier = Modifier.fillMaxSize(),
                                    verticalAlignment = Alignment.CenterVertically,
                                    horizontalArrangement = Arrangement.Center
                                ) {
                                    Text(
                                        text = "START PRACTICE EXAM",
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontFamily = FontFamily.Monospace,
                                            fontWeight = FontWeight.Bold,
                                            fontSize = 11.5.sp,
                                            letterSpacing = 0.8.sp
                                        ),
                                        color = Color(0xFF18181B)
                                    )
                                    Spacer(modifier = Modifier.width(6.dp))
                                    Icon(
                                        imageVector = Icons.Filled.ArrowForward,
                                        contentDescription = null,
                                        tint = Color(0xFF18181B),
                                        modifier = Modifier.size(14.dp)
                                    )
                                }
                            }
                        }
                    }
                }
            }

            // =========================================================================
            // 4. ACADEMIC LIBRARY SHELF (Matching Web Library Header & 18 Subject Cards)
            // =========================================================================
            item {
                Column(modifier = Modifier.fillMaxWidth()) {
                    // Unlocked Pill Badge
                    Surface(
                        shape = RoundedCornerShape(14.dp),
                        color = if (isDark) Color(0x2210B981) else Color(0xFFD1FAE5),
                        border = BorderStroke(1.dp, Color(0x4410B981))
                    ) {
                        Row(
                            modifier = Modifier.padding(horizontal = 10.dp, vertical = 4.dp),
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Icon(
                                imageVector = Icons.Filled.CheckCircle,
                                contentDescription = null,
                                tint = Color(0xFF10B981),
                                modifier = Modifier.size(12.dp)
                            )
                            Spacer(modifier = Modifier.width(5.dp))
                            Text(
                                text = "ALL 18 DOSSIERS UNLOCKED • 69 EDITIONS",
                                style = MaterialTheme.typography.labelSmall.copy(
                                    fontFamily = FontFamily.Monospace,
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 9.sp
                                ),
                                color = if (isDark) Color(0xFF34D399) else Color(0xFF065F46)
                            )
                        }
                    }

                    Spacer(modifier = Modifier.height(10.dp))

                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Text(
                            text = "Academic Library Shelf",
                            style = MaterialTheme.typography.headlineSmall.copy(
                                fontWeight = FontWeight.Black,
                                fontSize = 22.sp
                            ),
                            color = if (isDark) Color(0xFFFAF8F5) else Color(0xFF18181B)
                        )

                        Text(
                            text = "Explore All ↗",
                            style = MaterialTheme.typography.labelSmall.copy(
                                fontWeight = FontWeight.Bold,
                                fontSize = 11.5.sp
                            ),
                            color = Gold400,
                            modifier = Modifier.clickable { onBrowseDossiers() }
                        )
                    }

                    Spacer(modifier = Modifier.height(4.dp))

                    Text(
                        text = "Curated curriculum textbooks, question banks, and notes across all 18 courses.",
                        style = MaterialTheme.typography.bodySmall.copy(fontSize = 12.sp),
                        color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)
                    )

                    Spacer(modifier = Modifier.height(14.dp))

                    // Minimal Search Bar
                    OutlinedTextField(
                        value = searchQuery,
                        onValueChange = { searchQuery = it },
                        modifier = Modifier.fillMaxWidth(),
                        placeholder = {
                            Text(
                                text = "Search 18 course codes, textbooks, PYQs...",
                                fontSize = 12.5.sp,
                                color = Color(0xFF71717A)
                            )
                        },
                        leadingIcon = {
                            Icon(
                                imageVector = Icons.Filled.Search,
                                contentDescription = null,
                                tint = Gold400,
                                modifier = Modifier.size(18.dp)
                            )
                        },
                        trailingIcon = {
                            if (searchQuery.isNotEmpty()) {
                                IconButton(onClick = { searchQuery = "" }) {
                                    Icon(
                                        imageVector = Icons.Filled.Close,
                                        contentDescription = "Clear",
                                        tint = if (isDark) Color.White else Color(0xFF18181B),
                                        modifier = Modifier.size(16.dp)
                                    )
                                }
                            }
                        },
                        shape = RoundedCornerShape(18.dp),
                        colors = OutlinedTextFieldDefaults.colors(
                            focusedBorderColor = Gold500,
                            unfocusedBorderColor = if (isDark) Color(0x33FFFFFF) else Color(0x22000000),
                            focusedContainerColor = if (isDark) Color(0xFF14141B) else Color.White,
                            unfocusedContainerColor = if (isDark) Color(0xFF14141B) else Color.White
                        ),
                        singleLine = true
                    )
                }
            }

            // Filtered Subject Folder Cards (All 18 courses rendered as ticket cards)
            val filteredCourses = if (searchQuery.isBlank()) courses else courses.filter {
                it.code.contains(searchQuery, ignoreCase = true) || it.title.contains(searchQuery, ignoreCase = true)
            }

            itemsIndexed(filteredCourses) { index, course ->
                SubjectFolderCard(
                    course = course,
                    index = index + 1,
                    onOpenFolder = { onOpenCourse(it) }
                )
            }
        }

        // Profile / Session Status & 1-Tap Logout Dialog
        if (showProfileDialog) {
            AlertDialog(
                onDismissRequest = { showProfileDialog = false },
                title = {
                    Text(
                        text = "Academic Keycard Active",
                        style = MaterialTheme.typography.titleMedium.copy(fontWeight = FontWeight.Bold)
                    )
                },
                text = {
                    Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                        Text(
                            text = "Member: ${userSession?.name ?: "Academic Scholar"}",
                            style = MaterialTheme.typography.bodyMedium.copy(fontWeight = FontWeight.SemiBold)
                        )
                        Text(
                            text = "Passcode: ${userSession?.passcode ?: "VIP2026"}",
                            style = MaterialTheme.typography.bodySmall.copy(fontFamily = FontFamily.Monospace)
                        )
                        Text(
                            text = "Status: All 18 Course Dossiers & 69 Textbooks Unlocked",
                            style = MaterialTheme.typography.bodySmall,
                            color = Color(0xFF10B981)
                        )
                    }
                },
                confirmButton = {
                    Button(
                        onClick = {
                            authRepo.logout()
                            userSession = null
                            showProfileDialog = false
                            Toast.makeText(context, "Logged out successfully", Toast.LENGTH_SHORT).show()
                        },
                        colors = ButtonDefaults.buttonColors(containerColor = Color(0xFFEF4444))
                    ) {
                        Icon(imageVector = Icons.Filled.Logout, contentDescription = null, modifier = Modifier.size(16.dp))
                        Spacer(modifier = Modifier.width(6.dp))
                        Text(text = "Log Out")
                    }
                },
                dismissButton = {
                    TextButton(onClick = { showProfileDialog = false }) {
                        Text(text = "Close")
                    }
                }
            )
        }

        // EduNet Auth Modal for Guests
        SpotifyLoginModal(
            isOpen = showLoginModal,
            onClose = { showLoginModal = false },
            onLoginSuccess = {
                userSession = authRepo.getUserSession()
            }
        )
    }
}

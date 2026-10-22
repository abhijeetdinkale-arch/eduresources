package com.edunetwork.app.ui.screens

import android.content.Intent
import androidx.compose.foundation.BorderStroke
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
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material.icons.filled.ArrowForward
import androidx.compose.material.icons.filled.AutoAwesome
import androidx.compose.material.icons.filled.AutoStories
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.Folder
import androidx.compose.material.icons.filled.Search
import androidx.compose.material.icons.filled.Share
import androidx.compose.material.icons.filled.Star
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.OutlinedTextFieldDefaults
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.edunetwork.app.data.model.CourseDossier
import com.edunetwork.app.data.model.MaterialItem
import com.edunetwork.app.data.repository.AuthRepository
import com.edunetwork.app.data.repository.MaterialRepository
import com.edunetwork.app.ui.components.AppBackground
import com.edunetwork.app.ui.components.COURSE_THEME_MAP
import com.edunetwork.app.ui.components.CourseThemeInfo
import com.edunetwork.app.ui.components.SpotifyLoginModal
import com.edunetwork.app.ui.components.SubjectFolderCard
import com.edunetwork.app.ui.theme.Gold400
import com.edunetwork.app.ui.theme.Gold500
import com.edunetwork.app.ui.theme.Obsidian950

data class CategoryTab(val id: String, val label: String)

val CATALOG_CATEGORIES = listOf(
    CategoryTab("All", "ALL EDITIONS"),
    CategoryTab("Textbook", "TEXTBOOKS"),
    CategoryTab("Exam Companion", "EXAM COMPANIONS"),
    CategoryTab("Question Bank", "QUESTION BANKS"),
    CategoryTab("Handwritten Notes", "NOTES"),
    CategoryTab("Sample Question Papers", "PAPERS")
)

@Composable
fun CoursesScreen(
    repository: MaterialRepository,
    selectedCourseCode: String? = null,
    isDarkTheme: Boolean = true,
    onToggleDarkTheme: () -> Unit = {},
    onOpenDocument: (MaterialItem) -> Unit,
    onSelectCourse: (String?) -> Unit,
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current
    val authRepo = remember { AuthRepository.getInstance(context) }
    var showLoginModal by remember { mutableStateOf(false) }
    var pendingDocument by remember { mutableStateOf<MaterialItem?>(null) }

    var courses by remember { mutableStateOf<List<CourseDossier>>(emptyList()) }
    var materials by remember { mutableStateOf<List<MaterialItem>>(emptyList()) }
    var selectedCategory by remember { mutableStateOf("All") }
    var searchQuery by remember { mutableStateOf("") }
    var isLoading by remember { mutableStateOf(true) }

    LaunchedEffect(selectedCourseCode, selectedCategory, searchQuery) {
        isLoading = true
        courses = repository.getCourseDossiers()
        materials = repository.filterMaterials(
            courseCode = selectedCourseCode,
            category = selectedCategory,
            query = searchQuery
        )
        isLoading = false
    }

    val handleDocClick: (MaterialItem) -> Unit = { doc ->
        // Guests can open to preview free 3 sample pages; authorized users have full access
        onOpenDocument(doc)
    }

    val isDark = isDarkTheme
    val activeCourse = courses.find { it.code == selectedCourseCode }
    val themeInfo = activeCourse?.let { COURSE_THEME_MAP[it.code] } ?: CourseThemeInfo(
        activeCourse?.title ?: "Curriculum Repository",
        "Comprehensive textbook & exam preparation edition.",
        listOf(Color(0xFF283445), Color(0xFF151C26)),
        "#${selectedCourseCode ?: "COURSE"}"
    )

    AppBackground(modifier = modifier.fillMaxSize(), isDark = isDark) {
        if (selectedCourseCode != null && activeCourse != null) {
            // =========================================================================
            // COURSE DETAIL VIEW (Matching User Reference Image 1)
            // =========================================================================
            LazyColumn(
                modifier = Modifier
                    .fillMaxSize()
                    .statusBarsPadding(),
                contentPadding = PaddingValues(start = 16.dp, end = 16.dp, top = 16.dp, bottom = 100.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp)
            ) {
                // Top Navigation Bar (Back + Title + Share)
                item {
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Surface(
                            shape = CircleShape,
                            color = if (isDark) Color(0xFF22222C) else Color.White,
                            border = BorderStroke(1.dp, if (isDark) Color(0x33FFFFFF) else Color(0x22000000)),
                            modifier = Modifier
                                .size(42.dp)
                                .clickable { onSelectCourse(null) }
                        ) {
                            Box(contentAlignment = Alignment.Center) {
                                Icon(
                                    imageVector = Icons.Filled.ArrowBack,
                                    contentDescription = "Back",
                                    tint = if (isDark) Color.White else Color(0xFF18181B),
                                    modifier = Modifier.size(20.dp)
                                )
                            }
                        }

                        Text(
                            text = activeCourse.code,
                            style = MaterialTheme.typography.titleMedium.copy(
                                fontWeight = FontWeight.Bold,
                                fontFamily = FontFamily.Monospace,
                                fontSize = 15.sp
                            ),
                            color = if (isDark) Color.White else Color(0xFF18181B)
                        )

                        Surface(
                            shape = CircleShape,
                            color = if (isDark) Color(0xFF22222C) else Color.White,
                            border = BorderStroke(1.dp, if (isDark) Color(0x33FFFFFF) else Color(0x22000000)),
                            modifier = Modifier
                                .size(42.dp)
                                .clickable {
                                    val shareIntent = Intent(Intent.ACTION_SEND).apply {
                                        type = "text/plain"
                                        putExtra(Intent.EXTRA_SUBJECT, activeCourse.title)
                                        putExtra(Intent.EXTRA_TEXT, "Study ${activeCourse.title} (${activeCourse.code}) on Edu Network!")
                                    }
                                    context.startActivity(Intent.createChooser(shareIntent, "Share Course"))
                                }
                        ) {
                            Box(contentAlignment = Alignment.Center) {
                                Icon(
                                    imageVector = Icons.Filled.Share,
                                    contentDescription = "Share",
                                    tint = if (isDark) Color.White else Color(0xFF18181B),
                                    modifier = Modifier.size(18.dp)
                                )
                            }
                        }
                    }
                }

                // Course Header Card (Matching Image 1: Fluid Header + Rating + Title)
                item {
                    Surface(
                        shape = RoundedCornerShape(28.dp),
                        color = if (isDark) Color(0xFF14141B) else Color.White,
                        border = BorderStroke(1.dp, if (isDark) Color(0x33FFFFFF) else Color(0x22000000)),
                        shadowElevation = 8.dp,
                        modifier = Modifier.fillMaxWidth()
                    ) {
                        Column {
                            // Fluid Banner Art
                            Box(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .height(140.dp)
                                    .background(
                                        Brush.linearGradient(themeInfo.gradientColors),
                                        RoundedCornerShape(topStart = 28.dp, topEnd = 28.dp)
                                    )
                                    .padding(16.dp)
                            ) {
                                Row(
                                    modifier = Modifier.fillMaxWidth(),
                                    horizontalArrangement = Arrangement.SpaceBetween,
                                    verticalAlignment = Alignment.Top
                                ) {
                                    Surface(
                                        shape = RoundedCornerShape(12.dp),
                                        color = Color.Black.copy(alpha = 0.45f)
                                    ) {
                                        Text(
                                            text = themeInfo.tag,
                                            style = MaterialTheme.typography.labelSmall.copy(
                                                fontFamily = FontFamily.Monospace,
                                                fontWeight = FontWeight.Bold,
                                                fontSize = 9.5.sp
                                            ),
                                            color = Gold400,
                                            modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp)
                                        )
                                    }

                                    // Rating Badge ★ 4.9 (Matching Image 1)
                                    Surface(
                                        shape = RoundedCornerShape(20.dp),
                                        color = Color.White.copy(alpha = 0.95f)
                                    ) {
                                        Row(
                                            modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp),
                                            verticalAlignment = Alignment.CenterVertically
                                        ) {
                                            Icon(
                                                imageVector = Icons.Filled.Star,
                                                contentDescription = null,
                                                tint = Color(0xFFF59E0B),
                                                modifier = Modifier.size(13.dp)
                                            )
                                            Spacer(modifier = Modifier.width(3.dp))
                                            Text(
                                                text = "4.9",
                                                style = MaterialTheme.typography.labelSmall.copy(
                                                    fontWeight = FontWeight.Bold,
                                                    fontSize = 11.sp
                                                ),
                                                color = Color(0xFF18181B)
                                            )
                                        }
                                    }
                                }
                            }

                            // Title & Description
                            Column(modifier = Modifier.padding(18.dp)) {
                                Text(
                                    text = activeCourse.title,
                                    style = MaterialTheme.typography.headlineSmall.copy(
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 20.sp
                                    ),
                                    color = if (isDark) Color.White else Color(0xFF18181B)
                                )

                                Spacer(modifier = Modifier.height(10.dp))

                                // Badges Row (📖 5 Editions  🔥 Official Syllabus)
                                Row(
                                    horizontalArrangement = Arrangement.spacedBy(8.dp),
                                    verticalAlignment = Alignment.CenterVertically
                                ) {
                                    Surface(
                                        shape = RoundedCornerShape(18.dp),
                                        color = if (isDark) Color(0xFF272736) else Color(0xFFFEF3C7)
                                    ) {
                                        Row(
                                            modifier = Modifier.padding(horizontal = 10.dp, vertical = 6.dp),
                                            verticalAlignment = Alignment.CenterVertically
                                        ) {
                                            Icon(
                                                imageVector = Icons.Filled.AutoStories,
                                                contentDescription = null,
                                                tint = if (isDark) Gold400 else Color(0xFFB45309),
                                                modifier = Modifier.size(13.dp)
                                            )
                                            Spacer(modifier = Modifier.width(5.dp))
                                            Text(
                                                text = "${activeCourse.materialCount} Editions",
                                                style = MaterialTheme.typography.labelSmall.copy(
                                                    fontWeight = FontWeight.Bold,
                                                    fontSize = 11.sp
                                                ),
                                                color = if (isDark) Color.White else Color(0xFF78350F)
                                            )
                                        }
                                    }

                                    Surface(
                                        shape = RoundedCornerShape(18.dp),
                                        color = if (isDark) Color(0xFF272736) else Color(0xFFFCE7F3)
                                    ) {
                                        Row(
                                            modifier = Modifier.padding(horizontal = 10.dp, vertical = 6.dp),
                                            verticalAlignment = Alignment.CenterVertically
                                        ) {
                                            Icon(
                                                imageVector = Icons.Filled.AutoAwesome,
                                                contentDescription = null,
                                                tint = if (isDark) Color(0xFFEC4899) else Color(0xFFBE185D),
                                                modifier = Modifier.size(13.dp)
                                            )
                                            Spacer(modifier = Modifier.width(5.dp))
                                            Text(
                                                text = "Syllabus 2026",
                                                style = MaterialTheme.typography.labelSmall.copy(
                                                    fontWeight = FontWeight.Bold,
                                                    fontSize = 11.sp
                                                ),
                                                color = if (isDark) Color.White else Color(0xFF831843)
                                            )
                                        }
                                    }
                                }

                                Spacer(modifier = Modifier.height(12.dp))

                                Text(
                                    text = themeInfo.desc,
                                    style = MaterialTheme.typography.bodyMedium.copy(fontSize = 12.5.sp),
                                    color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A),
                                    lineHeight = 18.sp
                                )
                            }
                        }
                    }
                }

                // Section Title: "Editions & Textbooks"
                item {
                    Text(
                        text = "Editions & Textbooks",
                        style = MaterialTheme.typography.titleMedium.copy(
                            fontWeight = FontWeight.Bold,
                            fontSize = 16.sp
                        ),
                        color = if (isDark) Color.White else Color(0xFF18181B)
                    )
                }

                // List of Clickable Books / Materials
                itemsIndexed(materials) { index, doc ->
                    Surface(
                        shape = RoundedCornerShape(20.dp),
                        color = if (isDark) Color(0xFF14141B) else Color.White,
                        border = BorderStroke(1.dp, if (isDark) Color(0x33FFFFFF) else Color(0x22000000)),
                        modifier = Modifier
                            .fillMaxWidth()
                            .clickable { handleDocClick(doc) }
                    ) {
                        Row(
                            modifier = Modifier
                                .fillMaxWidth()
                                .padding(14.dp),
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.SpaceBetween
                        ) {
                            Row(
                                verticalAlignment = Alignment.CenterVertically,
                                modifier = Modifier.weight(1f)
                            ) {
                                Surface(
                                    shape = CircleShape,
                                    color = if (isDark) Color(0xFF22222C) else Color(0xFFF4F4F5),
                                    modifier = Modifier.size(42.dp)
                                ) {
                                    Box(contentAlignment = Alignment.Center) {
                                        Icon(
                                            imageVector = Icons.Filled.AutoStories,
                                            contentDescription = null,
                                            tint = Gold400,
                                            modifier = Modifier.size(20.dp)
                                        )
                                    }
                                }

                                Spacer(modifier = Modifier.width(12.dp))

                                Column {
                                    Surface(
                                        shape = RoundedCornerShape(6.dp),
                                        color = if (isDark) Color(0xFF222230) else Color(0xFFE4E4E7)
                                    ) {
                                        Text(
                                            text = doc.category.uppercase(),
                                            style = MaterialTheme.typography.labelSmall.copy(
                                                fontSize = 8.5.sp,
                                                fontWeight = FontWeight.Bold
                                            ),
                                            color = Gold400,
                                            modifier = Modifier.padding(horizontal = 6.dp, vertical = 2.dp)
                                        )
                                    }
                                    Spacer(modifier = Modifier.height(2.dp))
                                    Text(
                                        text = doc.title,
                                        style = MaterialTheme.typography.titleSmall.copy(
                                            fontWeight = FontWeight.Bold,
                                            fontSize = 13.5.sp
                                        ),
                                        color = if (isDark) Color.White else Color(0xFF18181B),
                                        maxLines = 1
                                    )
                                    Text(
                                        text = "Complete curriculum coverage • Free Sample",
                                        style = MaterialTheme.typography.bodySmall.copy(fontSize = 10.5.sp),
                                        color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)
                                    )
                                }
                            }

                            Surface(
                                shape = CircleShape,
                                color = if (isDark) Color.White else Color(0xFF18181B),
                                modifier = Modifier.size(32.dp)
                            ) {
                                Box(contentAlignment = Alignment.Center) {
                                    Icon(
                                        imageVector = Icons.Filled.ArrowForward,
                                        contentDescription = "Read",
                                        tint = if (isDark) Color(0xFF18181B) else Color.White,
                                        modifier = Modifier.size(14.dp)
                                    )
                                }
                            }
                        }
                    }
                }
            }
        } else {
            // =========================================================================
            // ALL DOSSIERS CATALOG VIEW (with Search + Filter Chips)
            // =========================================================================
            LazyColumn(
                modifier = Modifier
                    .fillMaxSize()
                    .statusBarsPadding(),
                contentPadding = PaddingValues(start = 16.dp, end = 16.dp, top = 16.dp, bottom = 100.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp)
            ) {
                // Header
                item {
                    Column {
                        Text(
                            text = "Course Dossiers",
                            style = MaterialTheme.typography.headlineMedium.copy(
                                fontWeight = FontWeight.Bold,
                                fontSize = 24.sp
                            ),
                            color = if (isDark) Color.White else Color(0xFF18181B)
                        )
                        Text(
                            text = "Official syllabus repositories & archival textbooks",
                            style = MaterialTheme.typography.bodyMedium.copy(fontSize = 12.5.sp),
                            color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)
                        )
                    }
                }

                // Search Bar
                item {
                    OutlinedTextField(
                        value = searchQuery,
                        onValueChange = { searchQuery = it },
                        modifier = Modifier.fillMaxWidth(),
                        placeholder = {
                            Text(
                                text = "Search courses, topics or textbooks...",
                                style = MaterialTheme.typography.bodyMedium.copy(fontSize = 13.sp),
                                color = if (isDark) Color(0xFF71717A) else Color(0xFFA1A1AA)
                            )
                        },
                        leadingIcon = {
                            Icon(
                                imageVector = Icons.Filled.Search,
                                contentDescription = "Search",
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
                                        tint = Color(0xFFA1A1AA),
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

                // Category Tabs Row
                item {
                    LazyRow(
                        horizontalArrangement = Arrangement.spacedBy(8.dp),
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        items(CATALOG_CATEGORIES) { tab ->
                            val isSelected = selectedCategory == tab.id
                            Surface(
                                shape = RoundedCornerShape(16.dp),
                                color = if (isSelected) {
                                    if (isDark) Color.White else Color(0xFF18181B)
                                } else {
                                    if (isDark) Color(0xFF1E1E28) else Color(0xFFE4E4E7)
                                },
                                modifier = Modifier.clickable { selectedCategory = tab.id }
                            ) {
                                Text(
                                    text = tab.label,
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontWeight = if (isSelected) FontWeight.Bold else FontWeight.Medium,
                                        fontSize = 11.sp
                                    ),
                                    color = if (isSelected) {
                                        if (isDark) Color(0xFF18181B) else Color.White
                                    } else {
                                        if (isDark) Color(0xFFA1A1AA) else Color(0xFF52525B)
                                    },
                                    modifier = Modifier.padding(horizontal = 14.dp, vertical = 7.dp)
                                )
                            }
                        }
                    }
                }

                // Web Dossier Cards List
                itemsIndexed(courses) { index, course ->
                    SubjectFolderCard(
                        course = course,
                        index = index + 1,
                        onOpenFolder = { onSelectCourse(course.code) }
                    )
                }
            }
        }

        // Spotify Login Modal for Guests
        SpotifyLoginModal(
            isOpen = showLoginModal,
            onClose = { showLoginModal = false },
            onLoginSuccess = {
                pendingDocument?.let { doc ->
                    onOpenDocument(doc)
                    pendingDocument = null
                }
            }
        )
    }
}

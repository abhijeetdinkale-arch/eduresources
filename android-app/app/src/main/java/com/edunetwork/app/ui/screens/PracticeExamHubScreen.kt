package com.edunetwork.app.ui.screens

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
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.statusBarsPadding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Alarm
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material.icons.filled.ArrowForward
import androidx.compose.material.icons.filled.Assignment
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.PlayArrow
import androidx.compose.material.icons.filled.School
import androidx.compose.material.icons.filled.WarningAmber
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
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
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.edunetwork.app.data.model.MockExam
import com.edunetwork.app.data.repository.MockExamRepository
import com.edunetwork.app.ui.theme.Gold400
import com.edunetwork.app.ui.theme.Gold500
import com.edunetwork.app.ui.theme.Obsidian950

@Composable
fun PracticeExamHubScreen(
    examRepository: MockExamRepository,
    isDarkTheme: Boolean = true,
    onSelectExam: (MockExam) -> Unit,
    onBack: () -> Unit
) {
    var exams by remember { mutableStateOf<List<MockExam>>(emptyList()) }
    var selectedSubjectCode by remember { mutableStateOf("ALL") }
    var isLoading by remember { mutableStateOf(true) }

    LaunchedEffect(Unit) {
        exams = examRepository.loadExams()
        isLoading = false
    }

    val filteredExams = remember(exams, selectedSubjectCode) {
        if (selectedSubjectCode == "ALL") exams
        else exams.filter { it.courseCode.equals(selectedSubjectCode, ignoreCase = true) }
    }

    val activeSubject = remember(selectedSubjectCode) {
        examRepository.availableSubjects.find { it.code.equals(selectedSubjectCode, ignoreCase = true) }
    }

    val isDark = isDarkTheme
    val bgColor = if (isDark) Color(0xFF0F0F14) else Color(0xFFFBF9F5)
    val cardBg = if (isDark) Color(0xFF181822) else Color.White
    val textPrimary = if (isDark) Color.White else Color(0xFF18181B)
    val textSecondary = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)
    val borderCol = if (isDark) Color(0x33FFFFFF) else Color(0xFFE4E4E7)

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(bgColor)
            .statusBarsPadding()
            .navigationBarsPadding()
    ) {
        if (isLoading) {
            Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                CircularProgressIndicator(color = Gold400)
            }
        } else {
            LazyColumn(
                modifier = Modifier.fillMaxSize(),
                contentPadding = PaddingValues(start = 18.dp, end = 18.dp, top = 12.dp, bottom = 100.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp)
            ) {
                // Top Navigation Bar
                item {
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            modifier = Modifier.clickable { onBack() }
                        ) {
                            Surface(
                                shape = CircleShape,
                                color = if (isDark) Color(0xFF272736) else Color(0xFFF4F4F5),
                                modifier = Modifier.size(40.dp)
                            ) {
                                Box(contentAlignment = Alignment.Center) {
                                    Icon(
                                        imageVector = Icons.Filled.ArrowBack,
                                        contentDescription = "Back",
                                        tint = textPrimary,
                                        modifier = Modifier.size(18.dp)
                                    )
                                }
                            }

                            Spacer(modifier = Modifier.width(12.dp))

                            Column {
                                Text(
                                    text = "EXAMINATION VAULT",
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontFamily = FontFamily.Monospace,
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 11.sp,
                                        letterSpacing = 1.sp
                                    ),
                                    color = Gold400
                                )
                                Text(
                                    text = if (activeSubject != null) "${activeSubject.code} Midterms" else "All Midterm Vaults",
                                    style = MaterialTheme.typography.titleLarge.copy(
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 20.sp
                                    ),
                                    color = textPrimary
                                )
                            }
                        }

                        // Exam Pattern Pill
                        Surface(
                            shape = RoundedCornerShape(12.dp),
                            color = if (isDark) Color(0xFF242434) else Color(0xFFFEF3C7),
                            border = BorderStroke(1.dp, Gold500)
                        ) {
                            Text(
                                text = "${filteredExams.size} Papers",
                                style = MaterialTheme.typography.labelSmall.copy(
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 11.sp
                                ),
                                color = if (isDark) Gold400 else Color(0xFFB45309),
                                modifier = Modifier.padding(horizontal = 10.dp, vertical = 5.dp)
                            )
                        }
                    }
                }

                // Subject Filter Chips
                item {
                    LazyRow(
                        horizontalArrangement = Arrangement.spacedBy(8.dp),
                        modifier = Modifier.fillMaxWidth()
                    ) {
                        item {
                            val isSelected = selectedSubjectCode == "ALL"
                            Surface(
                                shape = RoundedCornerShape(12.dp),
                                color = if (isSelected) Gold400 else (if (isDark) Color(0xFF242434) else Color(0xFFF4F4F5)),
                                border = BorderStroke(1.dp, if (isSelected) Gold400 else borderCol),
                                modifier = Modifier.clickable { selectedSubjectCode = "ALL" }
                            ) {
                                Text(
                                    text = "ALL (${exams.size})",
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 11.5.sp
                                    ),
                                    color = if (isSelected) Obsidian950 else textPrimary,
                                    modifier = Modifier.padding(horizontal = 12.dp, vertical = 7.dp)
                                )
                            }
                        }

                        items(examRepository.availableSubjects) { subject ->
                            val isSelected = selectedSubjectCode == subject.code
                            Surface(
                                shape = RoundedCornerShape(12.dp),
                                color = if (isSelected) Gold400 else (if (isDark) Color(0xFF242434) else Color(0xFFF4F4F5)),
                                border = BorderStroke(1.dp, if (isSelected) Gold400 else borderCol),
                                modifier = Modifier.clickable { selectedSubjectCode = subject.code }
                            ) {
                                Text(
                                    text = "${subject.code} (${subject.paperCount})",
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 11.5.sp
                                    ),
                                    color = if (isSelected) Obsidian950 else textPrimary,
                                    modifier = Modifier.padding(horizontal = 12.dp, vertical = 7.dp)
                                )
                            }
                        }
                    }
                }

                // Official Syllabus & Instructions Banner
                item {
                    Surface(
                        shape = RoundedCornerShape(24.dp),
                        color = if (isDark) Color(0xFF1E1E2A) else Color(0xFFFFFBEB),
                        border = BorderStroke(1.dp, if (isDark) Color(0x33F59E0B) else Color(0xFFFDE68A)),
                        shadowElevation = 4.dp,
                        modifier = Modifier.fillMaxWidth()
                    ) {
                        Column(modifier = Modifier.padding(18.dp)) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Icon(
                                    imageVector = Icons.Filled.School,
                                    contentDescription = null,
                                    tint = Gold400,
                                    modifier = Modifier.size(20.dp)
                                )
                                Spacer(modifier = Modifier.width(8.dp))
                                Text(
                                    text = if (activeSubject != null) "${activeSubject.name} (${activeSubject.department})" else "Official University Midterm Syllabus",
                                    style = MaterialTheme.typography.titleMedium.copy(
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 15.sp
                                    ),
                                    color = textPrimary
                                )
                            }

                            Spacer(modifier = Modifier.height(8.dp))

                            Text(
                                text = if (activeSubject != null) activeSubject.syllabusSummary else "Comprehensive midterm exam papers covering Units 1 to 3 across 8 academic engineering subjects. Built directly from authentic university PYQs and textbook companion blueprints.",
                                style = MaterialTheme.typography.bodySmall.copy(
                                    fontSize = 12.sp,
                                    lineHeight = 17.sp
                                ),
                                color = textSecondary
                            )
                        }
                    }
                }

                // Header title
                item {
                    Text(
                        text = "AVAILABLE MIDTERM PAPERS (${filteredExams.size})",
                        style = MaterialTheme.typography.labelSmall.copy(
                            fontFamily = FontFamily.Monospace,
                            fontWeight = FontWeight.Bold,
                            fontSize = 11.sp,
                            letterSpacing = 1.sp
                        ),
                        color = textSecondary,
                        modifier = Modifier.padding(start = 4.dp, top = 4.dp)
                    )
                }

                // Exam Papers List
                items(filteredExams) { exam ->
                    Surface(
                        shape = RoundedCornerShape(24.dp),
                        color = cardBg,
                        border = BorderStroke(1.2.dp, borderCol),
                        shadowElevation = 4.dp,
                        modifier = Modifier
                            .fillMaxWidth()
                            .clickable { onSelectExam(exam) }
                    ) {
                        Column(
                            modifier = Modifier.padding(18.dp)
                        ) {
                            // Top Row: Code Badge & Duration
                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.SpaceBetween,
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Surface(
                                    shape = RoundedCornerShape(8.dp),
                                    color = if (isDark) Color(0xFF272736) else Color(0xFFF4F4F5)
                                ) {
                                    Text(
                                        text = "${exam.courseCode} • ${exam.code}",
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontFamily = FontFamily.Monospace,
                                            fontWeight = FontWeight.Bold,
                                            fontSize = 12.sp
                                        ),
                                        color = Gold400,
                                        modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp)
                                    )
                                }

                                Row(verticalAlignment = Alignment.CenterVertically) {
                                    Icon(
                                        imageVector = Icons.Filled.Alarm,
                                        contentDescription = null,
                                        tint = textSecondary,
                                        modifier = Modifier.size(14.dp)
                                    )
                                    Spacer(modifier = Modifier.width(4.dp))
                                    Text(
                                        text = "${exam.durationMinutes} mins",
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontWeight = FontWeight.SemiBold,
                                            fontSize = 11.5.sp
                                        ),
                                        color = textSecondary
                                    )
                                }
                            }

                            Spacer(modifier = Modifier.height(10.dp))

                            Text(
                                text = exam.title,
                                style = MaterialTheme.typography.titleMedium.copy(
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 16.sp,
                                    lineHeight = 22.sp
                                ),
                                color = textPrimary
                            )

                            Spacer(modifier = Modifier.height(6.dp))

                            Text(
                                text = exam.description,
                                style = MaterialTheme.typography.bodySmall.copy(
                                    fontSize = 12.5.sp,
                                    lineHeight = 17.sp
                                ),
                                color = textSecondary,
                                maxLines = 2
                            )

                            Spacer(modifier = Modifier.height(14.dp))

                            // Badges & Action Button Row
                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.SpaceBetween,
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Row(horizontalArrangement = Arrangement.spacedBy(6.dp)) {
                                    Surface(
                                        shape = RoundedCornerShape(10.dp),
                                        color = if (isDark) Color(0xFF242434) else Color(0xFFF4F4F5)
                                    ) {
                                        Text(
                                            text = if (exam.isDraftingExam) "Subjective CAD" else "${exam.totalQuestions} MCQs",
                                            style = MaterialTheme.typography.labelSmall.copy(
                                                fontWeight = FontWeight.Bold,
                                                fontSize = 11.sp
                                            ),
                                            color = textPrimary,
                                            modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp)
                                        )
                                    }

                                    Surface(
                                        shape = RoundedCornerShape(10.dp),
                                        color = if (exam.isDraftingExam) (if (isDark) Color(0x333B82F6) else Color(0xFFEFF6FF)) else (if (isDark) Color(0x33DC2626) else Color(0xFFFEE2E2))
                                    ) {
                                        Text(
                                            text = if (exam.isDraftingExam) "${exam.maxMarks.toInt()} Marks Max" else "-0.25 Neg",
                                            style = MaterialTheme.typography.labelSmall.copy(
                                                fontWeight = FontWeight.Bold,
                                                fontSize = 11.sp
                                            ),
                                            color = if (exam.isDraftingExam) Color(0xFF3B82F6) else Color(0xFFDC2626),
                                            modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp)
                                        )
                                    }
                                }

                                // Start Button (Solid Ink Pill)
                                Surface(
                                    shape = RoundedCornerShape(20.dp),
                                    color = if (isDark) Color.White else Obsidian950,
                                    modifier = Modifier.clickable { onSelectExam(exam) }
                                ) {
                                    Row(
                                        modifier = Modifier.padding(horizontal = 14.dp, vertical = 8.dp),
                                        verticalAlignment = Alignment.CenterVertically
                                    ) {
                                        Text(
                                            text = if (exam.isDraftingExam) "Drafting Studio" else "Start Exam",
                                            style = MaterialTheme.typography.labelSmall.copy(
                                                fontWeight = FontWeight.Bold,
                                                fontSize = 12.5.sp
                                            ),
                                            color = if (isDark) Obsidian950 else Color.White
                                        )
                                        Spacer(modifier = Modifier.width(4.dp))
                                        Icon(
                                            imageVector = Icons.Filled.ArrowForward,
                                            contentDescription = null,
                                            tint = if (isDark) Obsidian950 else Color.White,
                                            modifier = Modifier.size(14.dp)
                                        )
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

package com.orbit.app.ui.screens

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
import androidx.compose.material.icons.filled.AutoAwesome
import androidx.compose.material.icons.filled.School
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
import com.orbit.app.data.model.MockExam
import com.orbit.app.data.repository.MockExamRepository
import com.orbit.app.ui.theme.DarkPlumBase
import com.orbit.app.ui.theme.DarkPlumCard
import com.orbit.app.ui.theme.NeonCapsuleYellow
import com.orbit.app.ui.theme.PastelAmberBg
import com.orbit.app.ui.theme.PastelLavenderBg
import com.orbit.app.ui.theme.TextWhiteMuted
import com.orbit.app.ui.theme.TextWhitePrimary
import com.orbit.app.ui.theme.TextWhiteSecondary

@Composable
fun OrbitPracticeExamHubScreen(
    examRepository: MockExamRepository,
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

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(DarkPlumBase)
            .statusBarsPadding()
            .navigationBarsPadding()
    ) {
        if (isLoading) {
            Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                CircularProgressIndicator(color = NeonCapsuleYellow)
            }
        } else {
            LazyColumn(
                modifier = Modifier.fillMaxSize(),
                contentPadding = PaddingValues(start = 18.dp, end = 18.dp, top = 12.dp, bottom = 100.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp)
            ) {
                // Header
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
                                color = Color(0x33FFFFFF),
                                modifier = Modifier.size(40.dp)
                            ) {
                                Box(contentAlignment = Alignment.Center) {
                                    Icon(
                                        imageVector = Icons.Filled.ArrowBack,
                                        contentDescription = "Back",
                                        tint = TextWhitePrimary,
                                        modifier = Modifier.size(18.dp)
                                    )
                                }
                            }

                            Spacer(modifier = Modifier.width(12.dp))

                            Column {
                                Text(
                                    text = "ORBIT EXAM VAULT",
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontFamily = FontFamily.Monospace,
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 11.sp,
                                        letterSpacing = 1.sp
                                    ),
                                    color = PastelLavenderBg
                                )
                                Text(
                                    text = if (activeSubject != null) "${activeSubject.code} Midterms" else "All Midterm Vaults",
                                    style = MaterialTheme.typography.titleLarge.copy(
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 20.sp
                                    ),
                                    color = TextWhitePrimary
                                )
                            }
                        }

                        Surface(
                            shape = RoundedCornerShape(12.dp),
                            color = Color(0x33B8A9FD),
                            border = BorderStroke(1.dp, PastelLavenderBg.copy(alpha = 0.3f))
                        ) {
                            Text(
                                text = "${filteredExams.size} Papers",
                                style = MaterialTheme.typography.labelSmall.copy(
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 11.sp
                                ),
                                color = PastelLavenderBg,
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
                                color = if (isSelected) NeonCapsuleYellow else Color(0x22FFFFFF),
                                border = BorderStroke(1.dp, if (isSelected) NeonCapsuleYellow else Color(0x33FFFFFF)),
                                modifier = Modifier.clickable { selectedSubjectCode = "ALL" }
                            ) {
                                Text(
                                    text = "ALL (${exams.size})",
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 11.5.sp
                                    ),
                                    color = if (isSelected) Color(0xFF130E1B) else TextWhitePrimary,
                                    modifier = Modifier.padding(horizontal = 12.dp, vertical = 7.dp)
                                )
                            }
                        }

                        items(examRepository.availableSubjects) { subject ->
                            val isSelected = selectedSubjectCode == subject.code
                            Surface(
                                shape = RoundedCornerShape(12.dp),
                                color = if (isSelected) NeonCapsuleYellow else Color(0x22FFFFFF),
                                border = BorderStroke(1.dp, if (isSelected) NeonCapsuleYellow else Color(0x33FFFFFF)),
                                modifier = Modifier.clickable { selectedSubjectCode = subject.code }
                            ) {
                                Text(
                                    text = "${subject.code} (${subject.paperCount})",
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 11.5.sp
                                    ),
                                    color = if (isSelected) Color(0xFF130E1B) else TextWhitePrimary,
                                    modifier = Modifier.padding(horizontal = 12.dp, vertical = 7.dp)
                                )
                            }
                        }
                    }
                }

                // Official Syllabus Card
                item {
                    Surface(
                        shape = RoundedCornerShape(24.dp),
                        color = DarkPlumCard,
                        border = BorderStroke(1.dp, Color.White.copy(alpha = 0.1f)),
                        shadowElevation = 4.dp,
                        modifier = Modifier.fillMaxWidth()
                    ) {
                        Column(modifier = Modifier.padding(18.dp)) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Icon(imageVector = Icons.Filled.School, contentDescription = null, tint = PastelAmberBg, modifier = Modifier.size(20.dp))
                                Spacer(modifier = Modifier.width(8.dp))
                                Text(
                                    text = if (activeSubject != null) "${activeSubject.name} (${activeSubject.department})" else "University Midterm Examination Syllabus",
                                    style = MaterialTheme.typography.titleMedium.copy(fontWeight = FontWeight.Bold, fontSize = 15.sp),
                                    color = TextWhitePrimary
                                )
                            }
                            Spacer(modifier = Modifier.height(8.dp))
                            Text(
                                text = if (activeSubject != null) activeSubject.syllabusSummary else "Comprehensive midterm exam papers covering Units 1 to 3 across 8 academic engineering subjects. Built directly from authentic university PYQs and textbook companion blueprints.",
                                style = MaterialTheme.typography.bodySmall.copy(fontSize = 12.sp, lineHeight = 17.sp),
                                color = TextWhiteSecondary
                            )
                        }
                    }
                }

                item {
                    Text(
                        text = "AVAILABLE MIDTERM PAPERS (${filteredExams.size})",
                        style = MaterialTheme.typography.labelSmall.copy(
                            fontFamily = FontFamily.Monospace,
                            fontWeight = FontWeight.Bold,
                            fontSize = 11.sp,
                            letterSpacing = 1.sp
                        ),
                        color = TextWhiteMuted,
                        modifier = Modifier.padding(start = 4.dp, top = 4.dp)
                    )
                }

                items(filteredExams) { exam ->
                    Surface(
                        shape = RoundedCornerShape(24.dp),
                        color = DarkPlumCard,
                        border = BorderStroke(1.2.dp, Color.White.copy(alpha = 0.1f)),
                        shadowElevation = 4.dp,
                        modifier = Modifier
                            .fillMaxWidth()
                            .clickable { onSelectExam(exam) }
                    ) {
                        Column(modifier = Modifier.padding(18.dp)) {
                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.SpaceBetween,
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Surface(
                                    shape = RoundedCornerShape(8.dp),
                                    color = Color(0x33B8A9FD)
                                ) {
                                    Text(
                                        text = "${exam.courseCode} • ${exam.code}",
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontFamily = FontFamily.Monospace,
                                            fontWeight = FontWeight.Bold,
                                            fontSize = 12.sp
                                        ),
                                        color = PastelLavenderBg,
                                        modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp)
                                    )
                                }

                                Row(verticalAlignment = Alignment.CenterVertically) {
                                    Icon(imageVector = Icons.Filled.Alarm, contentDescription = null, tint = TextWhiteMuted, modifier = Modifier.size(14.dp))
                                    Spacer(modifier = Modifier.width(4.dp))
                                    Text(
                                        text = "${exam.durationMinutes} mins",
                                        style = MaterialTheme.typography.labelSmall.copy(fontWeight = FontWeight.SemiBold, fontSize = 11.5.sp),
                                        color = TextWhiteMuted
                                    )
                                }
                            }

                            Spacer(modifier = Modifier.height(10.dp))

                            Text(
                                text = exam.title,
                                style = MaterialTheme.typography.titleMedium.copy(fontWeight = FontWeight.Bold, fontSize = 16.sp, lineHeight = 22.sp),
                                color = TextWhitePrimary
                            )

                            Spacer(modifier = Modifier.height(6.dp))

                            Text(
                                text = exam.description,
                                style = MaterialTheme.typography.bodySmall.copy(fontSize = 12.5.sp, lineHeight = 17.sp),
                                color = TextWhiteMuted,
                                maxLines = 2
                            )

                            Spacer(modifier = Modifier.height(14.dp))

                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.SpaceBetween,
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Row(horizontalArrangement = Arrangement.spacedBy(6.dp)) {
                                    Surface(
                                        shape = RoundedCornerShape(10.dp),
                                        color = Color(0x22FFFFFF)
                                    ) {
                                        Text(
                                            text = if (exam.isDraftingExam) "Subjective CAD" else "${exam.totalQuestions} MCQs",
                                            style = MaterialTheme.typography.labelSmall.copy(fontWeight = FontWeight.Bold, fontSize = 11.sp),
                                            color = TextWhitePrimary,
                                            modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp)
                                        )
                                    }

                                    Surface(
                                        shape = RoundedCornerShape(10.dp),
                                        color = if (exam.isDraftingExam) Color(0x333B82F6) else Color(0x33EF4444)
                                    ) {
                                        Text(
                                            text = if (exam.isDraftingExam) "${exam.maxMarks.toInt()} Marks Max" else "-0.25 Neg",
                                            style = MaterialTheme.typography.labelSmall.copy(fontWeight = FontWeight.Bold, fontSize = 11.sp),
                                            color = if (exam.isDraftingExam) Color(0xFF60A5FA) else Color(0xFFEF4444),
                                            modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp)
                                        )
                                    }
                                }

                                Surface(
                                    shape = RoundedCornerShape(20.dp),
                                    color = NeonCapsuleYellow,
                                    modifier = Modifier.clickable { onSelectExam(exam) }
                                ) {
                                    Row(
                                        modifier = Modifier.padding(horizontal = 14.dp, vertical = 8.dp),
                                        verticalAlignment = Alignment.CenterVertically
                                    ) {
                                        Text(
                                            text = if (exam.isDraftingExam) "Drafting Studio" else "Start Exam",
                                            style = MaterialTheme.typography.labelSmall.copy(fontWeight = FontWeight.Bold, fontSize = 12.5.sp),
                                            color = Color(0xFF130E1B)
                                        )
                                        Spacer(modifier = Modifier.width(4.dp))
                                        Icon(imageVector = Icons.Filled.ArrowForward, contentDescription = null, tint = Color(0xFF130E1B), modifier = Modifier.size(14.dp))
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

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
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Alarm
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.EmojiEvents
import androidx.compose.material.icons.filled.Lightbulb
import androidx.compose.material.icons.filled.Refresh
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
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
import com.edunetwork.app.data.model.ExamQuestion
import com.edunetwork.app.data.model.ExamResultSummary
import com.edunetwork.app.ui.theme.Gold400
import com.edunetwork.app.ui.theme.Gold500
import com.edunetwork.app.ui.theme.Obsidian950

enum class ResultFilter {
    ALL,
    INCORRECT,
    CORRECT,
    UNATTEMPTED
}

@Composable
fun PracticeExamResultsScreen(
    result: ExamResultSummary,
    isDarkTheme: Boolean = true,
    onRetakeExam: () -> Unit,
    onBackToHub: () -> Unit
) {
    var selectedFilter by remember { mutableStateOf(ResultFilter.ALL) }

    val isDark = isDarkTheme
    val bgColor = if (isDark) Color(0xFF0F0F14) else Color(0xFFFBF9F5)
    val cardBg = if (isDark) Color(0xFF181822) else Color.White
    val textPrimary = if (isDark) Color.White else Color(0xFF18181B)
    val textSecondary = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)
    val borderCol = if (isDark) Color(0x33FFFFFF) else Color(0xFFE4E4E7)

    val filteredQuestions = remember(selectedFilter, result) {
        result.exam.questions.filter { q ->
            val ans = result.userAnswers[q.id]?.selectedOptionIndex
            when (selectedFilter) {
                ResultFilter.ALL -> true
                ResultFilter.INCORRECT -> ans != null && ans != q.correctIndex
                ResultFilter.CORRECT -> ans != null && ans == q.correctIndex
                ResultFilter.UNATTEMPTED -> ans == null
            }
        }
    }

    val timeFormatted = remember(result.timeSpentSeconds) {
        val minutes = result.timeSpentSeconds / 60
        val seconds = result.timeSpentSeconds % 60
        String.format("%02d:%02d", minutes, seconds)
    }

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(bgColor)
            .statusBarsPadding()
            .navigationBarsPadding()
    ) {
        LazyColumn(
            modifier = Modifier.fillMaxSize(),
            contentPadding = PaddingValues(start = 18.dp, end = 18.dp, top = 12.dp, bottom = 40.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            // Header Bar
            item {
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Row(
                        verticalAlignment = Alignment.CenterVertically,
                        modifier = Modifier.clickable { onBackToHub() }
                    ) {
                        Surface(
                            shape = CircleShape,
                            color = if (isDark) Color(0xFF272736) else Color(0xFFF4F4F5),
                            modifier = Modifier.size(38.dp)
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
                        Spacer(modifier = Modifier.width(10.dp))
                        Column {
                            Text(
                                text = "EXAMINATION SCORECARD",
                                style = MaterialTheme.typography.labelSmall.copy(
                                    fontFamily = FontFamily.Monospace,
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 11.sp,
                                    letterSpacing = 1.sp
                                ),
                                color = Gold400
                            )
                            Text(
                                text = result.exam.code,
                                style = MaterialTheme.typography.titleMedium.copy(
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 16.sp
                                ),
                                color = textPrimary
                            )
                        }
                    }

                    // Retake Button
                    OutlinedButton(
                        onClick = onRetakeExam,
                        shape = RoundedCornerShape(18.dp),
                        border = BorderStroke(1.dp, borderCol),
                        colors = ButtonDefaults.outlinedButtonColors(contentColor = textPrimary)
                    ) {
                        Icon(imageVector = Icons.Filled.Refresh, contentDescription = null, modifier = Modifier.size(14.dp))
                        Spacer(modifier = Modifier.width(4.dp))
                        Text(text = "Retake", fontSize = 12.sp, fontWeight = FontWeight.Bold)
                    }
                }
            }

            // Scorecard Hero Summary Card
            item {
                Surface(
                    shape = RoundedCornerShape(26.dp),
                    color = cardBg,
                    border = BorderStroke(1.2.dp, borderCol),
                    shadowElevation = 6.dp,
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Column(modifier = Modifier.padding(20.dp)) {
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Column {
                                Text(
                                    text = "NET SCORE",
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontFamily = FontFamily.Monospace,
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 11.sp
                                    ),
                                    color = textSecondary
                                )
                                Spacer(modifier = Modifier.height(2.dp))
                                Row(verticalAlignment = Alignment.Bottom) {
                                    Text(
                                        text = String.format("%.2f", result.netScore),
                                        style = MaterialTheme.typography.displayMedium.copy(
                                            fontWeight = FontWeight.ExtraBold,
                                            fontSize = 38.sp
                                        ),
                                        color = if (result.netScore >= 18) Color(0xFF16A34A) else if (result.netScore >= 12) Gold500 else Color(0xFFDC2626)
                                    )
                                    Text(
                                        text = " / ${String.format("%.0f", result.maxMarks)}",
                                        style = MaterialTheme.typography.titleMedium.copy(
                                            fontWeight = FontWeight.Bold,
                                            fontSize = 18.sp
                                        ),
                                        color = textSecondary,
                                        modifier = Modifier.padding(bottom = 6.dp, start = 4.dp)
                                    )
                                }
                            }

                            // Accuracy & Grade Badge
                            Surface(
                                shape = RoundedCornerShape(16.dp),
                                color = if (isDark) Color(0xFF242434) else Color(0xFFFEF3C7),
                                border = BorderStroke(1.dp, Gold500)
                            ) {
                                Column(
                                    modifier = Modifier.padding(horizontal = 14.dp, vertical = 8.dp),
                                    horizontalAlignment = Alignment.CenterHorizontally
                                ) {
                                    Text(
                                        text = "${String.format("%.1f", result.accuracy)}%",
                                        style = MaterialTheme.typography.titleMedium.copy(
                                            fontWeight = FontWeight.Bold,
                                            fontSize = 17.sp
                                        ),
                                        color = if (isDark) Gold400 else Color(0xFFB45309)
                                    )
                                    Text(
                                        text = "Accuracy",
                                        style = MaterialTheme.typography.labelSmall.copy(fontSize = 10.sp),
                                        color = if (isDark) textSecondary else Color(0xFF78350F)
                                    )
                                }
                            }
                        }

                        Spacer(modifier = Modifier.height(18.dp))

                        // Score Breakdown Matrix
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween
                        ) {
                            BreakdownMetric(
                                label = "Correct",
                                value = "+${result.correctCount}",
                                subtext = "+${String.format("%.1f", result.positiveMarks)}",
                                color = Color(0xFF16A34A),
                                isDark = isDark
                            )
                            BreakdownMetric(
                                label = "Incorrect",
                                value = "-${result.incorrectCount}",
                                subtext = "-${String.format("%.2f", result.penaltyMarks)}",
                                color = Color(0xFFDC2626),
                                isDark = isDark
                            )
                            BreakdownMetric(
                                label = "Unattempted",
                                value = "${result.unattemptedCount}",
                                subtext = "0.00",
                                color = textSecondary,
                                isDark = isDark
                            )
                            BreakdownMetric(
                                label = "Time Spent",
                                value = timeFormatted,
                                subtext = "90m max",
                                color = Gold400,
                                isDark = isDark
                            )
                        }
                    }
                }
            }

            // Filter Chips Row
            item {
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.spacedBy(8.dp)
                ) {
                    ResultFilterChip(
                        title = "All (${result.totalQuestions})",
                        isSelected = selectedFilter == ResultFilter.ALL,
                        onClick = { selectedFilter = ResultFilter.ALL },
                        isDark = isDark
                    )
                    ResultFilterChip(
                        title = "Incorrect (${result.incorrectCount})",
                        isSelected = selectedFilter == ResultFilter.INCORRECT,
                        onClick = { selectedFilter = ResultFilter.INCORRECT },
                        isDark = isDark
                    )
                    ResultFilterChip(
                        title = "Correct (${result.correctCount})",
                        isSelected = selectedFilter == ResultFilter.CORRECT,
                        onClick = { selectedFilter = ResultFilter.CORRECT },
                        isDark = isDark
                    )
                    ResultFilterChip(
                        title = "Skipped (${result.unattemptedCount})",
                        isSelected = selectedFilter == ResultFilter.UNATTEMPTED,
                        onClick = { selectedFilter = ResultFilter.UNATTEMPTED },
                        isDark = isDark
                    )
                }
            }

            // Question Derivation Cards
            itemsIndexed(filteredQuestions) { _, q ->
                val userAns = result.userAnswers[q.id]?.selectedOptionIndex
                val isCorrect = userAns == q.correctIndex
                val isUnattempted = userAns == null

                val statusColor = when {
                    isCorrect -> Color(0xFF16A34A)
                    isUnattempted -> textSecondary
                    else -> Color(0xFFDC2626)
                }

                Surface(
                    shape = RoundedCornerShape(22.dp),
                    color = cardBg,
                    border = BorderStroke(1.dp, borderCol),
                    shadowElevation = 2.dp,
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Column(modifier = Modifier.padding(18.dp)) {
                        // Question Header
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Text(
                                text = "Question ${q.id} • ${q.topic}",
                                style = MaterialTheme.typography.labelSmall.copy(
                                    fontFamily = FontFamily.Monospace,
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 11.5.sp
                                ),
                                color = textSecondary
                            )

                            Surface(
                                shape = RoundedCornerShape(10.dp),
                                color = statusColor.copy(alpha = 0.15f)
                            ) {
                                Text(
                                    text = when {
                                        isCorrect -> "Correct (+1.0)"
                                        isUnattempted -> "Unattempted (0.0)"
                                        else -> "Incorrect (-0.25)"
                                    },
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 11.sp
                                    ),
                                    color = statusColor,
                                    modifier = Modifier.padding(horizontal = 8.dp, vertical = 3.dp)
                                )
                            }
                        }

                        Spacer(modifier = Modifier.height(10.dp))

                        Text(
                            text = q.question,
                            style = MaterialTheme.typography.bodyMedium.copy(
                                fontWeight = FontWeight.Bold,
                                fontSize = 15.sp,
                                lineHeight = 21.sp
                            ),
                            color = textPrimary
                        )

                        Spacer(modifier = Modifier.height(12.dp))

                        // Answer Options with Highlighting
                        val letters = listOf("A", "B", "C", "D")
                        q.options.forEachIndexed { optIdx, optText ->
                            val isThisCorrect = optIdx == q.correctIndex
                            val isThisUserAns = optIdx == userAns

                            val optBg = when {
                                isThisCorrect -> Color(0x2216A34A)
                                isThisUserAns && !isThisCorrect -> Color(0x22DC2626)
                                else -> if (isDark) Color(0xFF1E1E2A) else Color(0xFFF9FAFB)
                            }

                            val optBorder = when {
                                isThisCorrect -> Color(0xFF16A34A)
                                isThisUserAns && !isThisCorrect -> Color(0xFFDC2626)
                                else -> borderCol
                            }

                            Surface(
                                shape = RoundedCornerShape(14.dp),
                                color = optBg,
                                border = BorderStroke(1.dp, optBorder),
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .padding(vertical = 3.dp)
                            ) {
                                Row(
                                    modifier = Modifier.padding(horizontal = 12.dp, vertical = 10.dp),
                                    verticalAlignment = Alignment.CenterVertically
                                ) {
                                    Text(
                                        text = "${letters.getOrElse(optIdx) { "${optIdx + 1}" }}.",
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 13.sp,
                                        color = if (isThisCorrect) Color(0xFF16A34A) else if (isThisUserAns) Color(0xFFDC2626) else textSecondary
                                    )
                                    Spacer(modifier = Modifier.width(8.dp))
                                    Text(
                                        text = optText,
                                        fontSize = 13.5.sp,
                                        color = textPrimary,
                                        fontWeight = if (isThisCorrect || isThisUserAns) FontWeight.Bold else FontWeight.Normal,
                                        modifier = Modifier.weight(1f)
                                    )
                                    if (isThisCorrect) {
                                        Text(text = "✓ Correct Answer", fontSize = 10.5.sp, fontWeight = FontWeight.Bold, color = Color(0xFF16A34A))
                                    } else if (isThisUserAns) {
                                        Text(text = "✗ Your Choice", fontSize = 10.5.sp, fontWeight = FontWeight.Bold, color = Color(0xFFDC2626))
                                    }
                                }
                            }
                        }

                        // Mathematical Derivation & Explanation
                        if (q.explanation != null) {
                            Spacer(modifier = Modifier.height(14.dp))
                            Surface(
                                shape = RoundedCornerShape(16.dp),
                                color = if (isDark) Color(0xFF222230) else Color(0xFFF4F4F6),
                                border = BorderStroke(1.dp, borderCol),
                                modifier = Modifier.fillMaxWidth()
                            ) {
                                Column(modifier = Modifier.padding(14.dp)) {
                                    Row(verticalAlignment = Alignment.CenterVertically) {
                                        Icon(
                                            imageVector = Icons.Filled.Lightbulb,
                                            contentDescription = null,
                                            tint = Gold400,
                                            modifier = Modifier.size(16.dp)
                                        )
                                        Spacer(modifier = Modifier.width(6.dp))
                                        Text(
                                            text = "Step-by-Step Mathematical Derivation:",
                                            style = MaterialTheme.typography.labelSmall.copy(
                                                fontWeight = FontWeight.Bold,
                                                fontSize = 11.5.sp
                                            ),
                                            color = textPrimary
                                        )
                                    }

                                    Spacer(modifier = Modifier.height(8.dp))

                                    q.explanation.steps.forEachIndexed { sIdx, step ->
                                        Text(
                                            text = "• $step",
                                            style = MaterialTheme.typography.bodySmall.copy(
                                                fontSize = 12.5.sp,
                                                lineHeight = 18.sp
                                            ),
                                            color = textPrimary,
                                            modifier = Modifier.padding(vertical = 2.dp)
                                        )
                                    }

                                    if (!q.explanation.keyConcept.isNullOrBlank()) {
                                        Spacer(modifier = Modifier.height(8.dp))
                                        Surface(
                                            shape = RoundedCornerShape(8.dp),
                                            color = if (isDark) Color(0xFF181822) else Color.White,
                                            border = BorderStroke(1.dp, Gold500)
                                        ) {
                                            Text(
                                                text = "Key Concept: ${q.explanation.keyConcept}",
                                                style = MaterialTheme.typography.bodySmall.copy(
                                                    fontWeight = FontWeight.SemiBold,
                                                    fontSize = 11.5.sp
                                                ),
                                                color = if (isDark) Gold400 else Color(0xFFB45309),
                                                modifier = Modifier.padding(horizontal = 10.dp, vertical = 6.dp)
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
}

@Composable
private fun BreakdownMetric(
    label: String,
    value: String,
    subtext: String,
    color: Color,
    isDark: Boolean
) {
    Surface(
        shape = RoundedCornerShape(14.dp),
        color = if (isDark) Color(0xFF222230) else Color(0xFFF4F4F5),
        modifier = Modifier.width(76.dp)
    ) {
        Column(
            modifier = Modifier.padding(vertical = 8.dp, horizontal = 4.dp),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text(
                text = value,
                style = MaterialTheme.typography.titleMedium.copy(
                    fontWeight = FontWeight.Bold,
                    fontSize = 14.sp
                ),
                color = color
            )
            Text(
                text = label,
                style = MaterialTheme.typography.labelSmall.copy(fontSize = 9.sp),
                color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)
            )
            Text(
                text = subtext,
                style = MaterialTheme.typography.labelSmall.copy(fontSize = 8.5.sp, fontFamily = FontFamily.Monospace),
                color = color.copy(alpha = 0.8f)
            )
        }
    }
}

@Composable
private fun ResultFilterChip(
    title: String,
    isSelected: Boolean,
    onClick: () -> Unit,
    isDark: Boolean
) {
    Surface(
        shape = RoundedCornerShape(16.dp),
        color = if (isSelected) (if (isDark) Color.White else Obsidian950) else (if (isDark) Color(0xFF1E1E2A) else Color(0xFFF4F4F5)),
        modifier = Modifier.clickable { onClick() }
    ) {
        Text(
            text = title,
            style = MaterialTheme.typography.labelSmall.copy(
                fontWeight = FontWeight.Bold,
                fontSize = 11.sp
            ),
            color = if (isSelected) (if (isDark) Obsidian950 else Color.White) else (if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)),
            modifier = Modifier.padding(horizontal = 10.dp, vertical = 6.dp)
        )
    }
}

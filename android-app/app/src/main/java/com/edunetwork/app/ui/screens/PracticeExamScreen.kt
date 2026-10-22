package com.edunetwork.app.ui.screens

import androidx.activity.compose.BackHandler
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
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.items
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Alarm
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material.icons.filled.ArrowForward
import androidx.compose.material.icons.filled.BookmarkBorder
import androidx.compose.material.icons.filled.Clear
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.Done
import androidx.compose.material.icons.filled.GridView
import androidx.compose.material.icons.filled.Warning
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateMapOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.window.Dialog
import com.edunetwork.app.data.model.MockExam
import com.edunetwork.app.data.model.QuestionAnswerState
import com.edunetwork.app.ui.theme.Gold400
import com.edunetwork.app.ui.theme.Gold500
import com.edunetwork.app.ui.theme.Obsidian950
import kotlinx.coroutines.delay

@Composable
fun PracticeExamScreen(
    exam: MockExam,
    isDarkTheme: Boolean = true,
    onSubmitExam: (Map<Int, QuestionAnswerState>, Int) -> Unit,
    onExitExam: () -> Unit
) {
    var currentIndex by remember { mutableIntStateOf(0) }
    val userAnswers = remember { mutableStateMapOf<Int, QuestionAnswerState>() }
    var secondsRemaining by remember { mutableIntStateOf(exam.durationMinutes * 60) }
    var totalTimeSpent by remember { mutableIntStateOf(0) }

    var showPaletteDialog by remember { mutableStateOf(false) }
    var showSubmitConfirmation by remember { mutableStateOf(false) }
    var showExitConfirmation by remember { mutableStateOf(false) }

    // Intercept hardware/gesture Back button
    BackHandler {
        showExitConfirmation = true
    }

    // Exam Countdown Timer (1 second interval)
    LaunchedEffect(Unit) {
        while (secondsRemaining > 0) {
            delay(1000)
            secondsRemaining--
            totalTimeSpent++
        }
        // Auto-submit when time expires
        onSubmitExam(userAnswers.toMap(), totalTimeSpent)
    }

    val isDark = isDarkTheme
    val bgColor = if (isDark) Color(0xFF0F0F14) else Color(0xFFFBF9F5)
    val cardBg = if (isDark) Color(0xFF181822) else Color.White
    val textPrimary = if (isDark) Color.White else Color(0xFF18181B)
    val textSecondary = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)
    val borderCol = if (isDark) Color(0x33FFFFFF) else Color(0xFFE4E4E7)

    val currentQuestion = exam.questions.getOrNull(currentIndex)
    val currentState = currentQuestion?.let { userAnswers[it.id] } ?: QuestionAnswerState()

    val formattedTime = remember(secondsRemaining) {
        val minutes = secondsRemaining / 60
        val seconds = secondsRemaining % 60
        String.format("%02d:%02d", minutes, seconds)
    }

    val answeredCount = userAnswers.values.count { it.selectedOptionIndex != null }
    val reviewedCount = userAnswers.values.count { it.isMarkedForReview }

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(bgColor)
            .statusBarsPadding()
            .navigationBarsPadding()
    ) {
        Column(
            modifier = Modifier.fillMaxSize()
        ) {
            // =========================================================================
            // 1. TOP EXAM HEADER (Timer, Question Tracker, Palette Trigger, Exit)
            // =========================================================================
            Surface(
                color = cardBg,
                border = BorderStroke(1.dp, borderCol),
                shadowElevation = 4.dp,
                modifier = Modifier.fillMaxWidth()
            ) {
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(horizontal = 16.dp, vertical = 12.dp),
                    horizontalArrangement = Arrangement.SpaceBetween,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    // Exit Button & Exam Title
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Surface(
                            shape = CircleShape,
                            color = if (isDark) Color(0xFF272736) else Color(0xFFF4F4F5),
                            modifier = Modifier
                                .size(36.dp)
                                .clickable { showExitConfirmation = true }
                        ) {
                            Box(contentAlignment = Alignment.Center) {
                                Icon(
                                    imageVector = Icons.Filled.Close,
                                    contentDescription = "Exit Exam",
                                    tint = textPrimary,
                                    modifier = Modifier.size(18.dp)
                                )
                            }
                        }

                        Spacer(modifier = Modifier.width(10.dp))

                        Column {
                            Text(
                                text = exam.code,
                                style = MaterialTheme.typography.labelSmall.copy(
                                    fontFamily = FontFamily.Monospace,
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 12.sp
                                ),
                                color = Gold400
                            )
                            Text(
                                text = "MTH165 Midterm",
                                style = MaterialTheme.typography.titleSmall.copy(
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 14.sp
                                ),
                                color = textPrimary
                            )
                        }
                    }

                    // Timer Capsule & Palette Button
                    Row(
                        verticalAlignment = Alignment.CenterVertically,
                        horizontalArrangement = Arrangement.spacedBy(8.dp)
                    ) {
                        // Timer Pill
                        val isTimeCritical = secondsRemaining < 300 // < 5 mins
                        Surface(
                            shape = RoundedCornerShape(16.dp),
                            color = if (isTimeCritical) Color(0x33EF4444) else if (isDark) Color(0xFF222230) else Color(0xFFFEF3C7),
                            border = BorderStroke(1.dp, if (isTimeCritical) Color(0xFFEF4444) else Gold500)
                        ) {
                            Row(
                                modifier = Modifier.padding(horizontal = 10.dp, vertical = 6.dp),
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Icon(
                                    imageVector = Icons.Filled.Alarm,
                                    contentDescription = null,
                                    tint = if (isTimeCritical) Color(0xFFEF4444) else Gold400,
                                    modifier = Modifier.size(15.dp)
                                )
                                Spacer(modifier = Modifier.width(5.dp))
                                Text(
                                    text = formattedTime,
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontFamily = FontFamily.Monospace,
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 12.5.sp
                                    ),
                                    color = if (isTimeCritical) Color(0xFFEF4444) else if (isDark) Color.White else Color(0xFF18181B)
                                )
                            }
                        }

                        // Question Palette Trigger
                        Surface(
                            shape = RoundedCornerShape(16.dp),
                            color = if (isDark) Color(0xFF272736) else Color(0xFFF4F4F5),
                            border = BorderStroke(1.dp, borderCol),
                            modifier = Modifier.clickable { showPaletteDialog = true }
                        ) {
                            Row(
                                modifier = Modifier.padding(horizontal = 10.dp, vertical = 6.dp),
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Icon(
                                    imageVector = Icons.Filled.GridView,
                                    contentDescription = "Palette",
                                    tint = textPrimary,
                                    modifier = Modifier.size(15.dp)
                                )
                                Spacer(modifier = Modifier.width(4.dp))
                                Text(
                                    text = "$answeredCount/${exam.questions.size}",
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontFamily = FontFamily.Monospace,
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 11.5.sp
                                    ),
                                    color = textPrimary
                                )
                            }
                        }
                    }
                }
            }

            // =========================================================================
            // 2. QUESTION CONTENT BODY (Scrollable)
            // =========================================================================
            if (currentQuestion != null) {
                Column(
                    modifier = Modifier
                        .weight(1f)
                        .verticalScroll(rememberScrollState())
                        .padding(horizontal = 18.dp, vertical = 14.dp)
                ) {
                    // Question Meta Badge & Topic
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Surface(
                            shape = RoundedCornerShape(12.dp),
                            color = if (isDark) Color(0xFF242434) else Color(0xFFF4F4F5),
                            border = BorderStroke(1.dp, borderCol)
                        ) {
                            Text(
                                text = "Question ${currentIndex + 1} of ${exam.questions.size}",
                                style = MaterialTheme.typography.labelSmall.copy(
                                    fontFamily = FontFamily.Monospace,
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 12.sp
                                ),
                                color = textPrimary,
                                modifier = Modifier.padding(horizontal = 10.dp, vertical = 5.dp)
                            )
                        }

                        Row(
                            horizontalArrangement = Arrangement.spacedBy(6.dp),
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            if (currentState.isMarkedForReview) {
                                Surface(
                                    shape = RoundedCornerShape(10.dp),
                                    color = Color(0x33F59E0B)
                                ) {
                                    Text(
                                        text = "Review",
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontSize = 10.sp,
                                            fontWeight = FontWeight.Bold
                                        ),
                                        color = Gold400,
                                        modifier = Modifier.padding(horizontal = 8.dp, vertical = 3.dp)
                                    )
                                }
                            }

                            Surface(
                                shape = RoundedCornerShape(10.dp),
                                color = if (isDark) Color(0x22FFFFFF) else Color(0xFFE4E4E7)
                            ) {
                                Text(
                                    text = currentQuestion.topic,
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontSize = 10.sp,
                                        fontWeight = FontWeight.SemiBold
                                    ),
                                    color = textSecondary,
                                    modifier = Modifier.padding(horizontal = 8.dp, vertical = 3.dp)
                                )
                            }
                        }
                    }

                    Spacer(modifier = Modifier.height(14.dp))

                    // Question Text Card
                    Surface(
                        shape = RoundedCornerShape(20.dp),
                        color = cardBg,
                        border = BorderStroke(1.dp, borderCol),
                        shadowElevation = 2.dp,
                        modifier = Modifier.fillMaxWidth()
                    ) {
                        Text(
                            text = currentQuestion.question,
                            style = MaterialTheme.typography.bodyLarge.copy(
                                fontWeight = FontWeight.SemiBold,
                                fontSize = 16.5.sp,
                                lineHeight = 24.sp
                            ),
                            color = textPrimary,
                            modifier = Modifier.padding(18.dp)
                        )
                    }

                    Spacer(modifier = Modifier.height(16.dp))

                    Text(
                        text = "SELECT AN OPTION",
                        style = MaterialTheme.typography.labelSmall.copy(
                            letterSpacing = 1.sp,
                            fontWeight = FontWeight.Bold,
                            fontSize = 11.sp
                        ),
                        color = textSecondary,
                        modifier = Modifier.padding(start = 4.dp, bottom = 8.dp)
                    )

                    // Options List
                    val optionLetters = listOf("A", "B", "C", "D")
                    currentQuestion.options.forEachIndexed { optIndex, optionText ->
                        val isSelected = currentState.selectedOptionIndex == optIndex

                        val optBorderColor = when {
                            isSelected -> Gold500
                            isDark -> Color(0x33FFFFFF)
                            else -> Color(0xFFE4E4E7)
                        }

                        val optBgColor = when {
                            isSelected && isDark -> Color(0xFF2A281E)
                            isSelected && !isDark -> Color(0xFFFFFBEB)
                            else -> cardBg
                        }

                        Surface(
                            shape = RoundedCornerShape(18.dp),
                            color = optBgColor,
                            border = BorderStroke(if (isSelected) 1.8.dp else 1.dp, optBorderColor),
                            shadowElevation = if (isSelected) 4.dp else 1.dp,
                            modifier = Modifier
                                .fillMaxWidth()
                                .padding(vertical = 5.dp)
                                .clickable {
                                    val updated = currentState.copy(selectedOptionIndex = optIndex)
                                    userAnswers[currentQuestion.id] = updated
                                }
                        ) {
                            Row(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .padding(horizontal = 14.dp, vertical = 14.dp),
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                // Letter Circle (A, B, C, D)
                                Surface(
                                    shape = CircleShape,
                                    color = if (isSelected) Gold500 else if (isDark) Color(0xFF272736) else Color(0xFFF4F4F5),
                                    modifier = Modifier.size(32.dp)
                                ) {
                                    Box(contentAlignment = Alignment.Center) {
                                        Text(
                                            text = optionLetters.getOrElse(optIndex) { "${optIndex + 1}" },
                                            style = MaterialTheme.typography.labelSmall.copy(
                                                fontWeight = FontWeight.Bold,
                                                fontSize = 13.sp
                                            ),
                                            color = if (isSelected) Obsidian950 else textPrimary
                                        )
                                    }
                                }

                                Spacer(modifier = Modifier.width(12.dp))

                                Text(
                                    text = optionText,
                                    style = MaterialTheme.typography.bodyMedium.copy(
                                        fontSize = 15.sp,
                                        fontWeight = if (isSelected) FontWeight.Bold else FontWeight.Normal,
                                        lineHeight = 21.sp
                                    ),
                                    color = textPrimary,
                                    modifier = Modifier.weight(1f)
                                )
                            }
                        }
                    }
                }
            }

            // =========================================================================
            // 3. BOTTOM BUTTONS (High Contrast, 100% Visible, Intuitive Flow)
            // =========================================================================
            Surface(
                color = cardBg,
                border = BorderStroke(1.dp, borderCol),
                shadowElevation = 12.dp,
                modifier = Modifier.fillMaxWidth()
            ) {
                Column(
                    modifier = Modifier.padding(horizontal = 14.dp, vertical = 10.dp)
                ) {
                    // Secondary Actions Row: Clear & Mark for Review
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        // Clear Selection Button
                        OutlinedButton(
                            onClick = {
                                if (currentQuestion != null && currentState.selectedOptionIndex != null) {
                                    userAnswers[currentQuestion.id] = currentState.copy(selectedOptionIndex = null)
                                }
                            },
                            shape = RoundedCornerShape(18.dp),
                            border = BorderStroke(1.dp, borderCol),
                            colors = ButtonDefaults.outlinedButtonColors(
                                contentColor = textSecondary
                            ),
                            enabled = currentState.selectedOptionIndex != null,
                            modifier = Modifier.height(36.dp)
                        ) {
                            Icon(imageVector = Icons.Filled.Clear, contentDescription = null, modifier = Modifier.size(14.dp))
                            Spacer(modifier = Modifier.width(4.dp))
                            Text(text = "Clear", fontSize = 11.5.sp, fontWeight = FontWeight.SemiBold)
                        }

                        // Mark for Review Button
                        OutlinedButton(
                            onClick = {
                                if (currentQuestion != null) {
                                    userAnswers[currentQuestion.id] = currentState.copy(
                                        isMarkedForReview = !currentState.isMarkedForReview
                                    )
                                }
                            },
                            shape = RoundedCornerShape(18.dp),
                            border = BorderStroke(1.dp, if (currentState.isMarkedForReview) Gold500 else borderCol),
                            colors = ButtonDefaults.outlinedButtonColors(
                                contentColor = if (currentState.isMarkedForReview) Gold400 else textPrimary
                            ),
                            modifier = Modifier.height(36.dp)
                        ) {
                            Icon(
                                imageVector = Icons.Filled.BookmarkBorder,
                                contentDescription = null,
                                modifier = Modifier.size(14.dp)
                            )
                            Spacer(modifier = Modifier.width(4.dp))
                            Text(
                                text = if (currentState.isMarkedForReview) "Marked" else "Mark for Review",
                                fontSize = 11.5.sp,
                                fontWeight = FontWeight.SemiBold
                            )
                        }

                        // Submit Exam Button (Red / Prominent)
                        Button(
                            onClick = { showSubmitConfirmation = true },
                            shape = RoundedCornerShape(18.dp),
                            colors = ButtonDefaults.buttonColors(
                                containerColor = Color(0xFFDC2626),
                                contentColor = Color.White
                            ),
                            modifier = Modifier.height(36.dp)
                        ) {
                            Text(text = "Submit", fontSize = 12.sp, fontWeight = FontWeight.Bold)
                        }
                    }

                    Spacer(modifier = Modifier.height(10.dp))

                    // Primary Navigation Row: Previous & Next / Save
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.spacedBy(10.dp)
                    ) {
                        // Previous Question Button
                        Button(
                            onClick = {
                                if (currentIndex > 0) currentIndex--
                            },
                            enabled = currentIndex > 0,
                            shape = RoundedCornerShape(22.dp),
                            colors = ButtonDefaults.buttonColors(
                                containerColor = if (isDark) Color(0xFF272736) else Color(0xFFE4E4E7),
                                contentColor = textPrimary,
                                disabledContainerColor = if (isDark) Color(0xFF1B1B26) else Color(0xFFF4F4F5),
                                disabledContentColor = textSecondary.copy(alpha = 0.5f)
                            ),
                            modifier = Modifier
                                .weight(1f)
                                .height(48.dp)
                        ) {
                            Icon(imageVector = Icons.Filled.ArrowBack, contentDescription = null, modifier = Modifier.size(16.dp))
                            Spacer(modifier = Modifier.width(6.dp))
                            Text(text = "Previous", fontWeight = FontWeight.Bold, fontSize = 13.5.sp)
                        }

                        // Save & Next Button (Solid Ink High Contrast)
                        val isLastQuestion = currentIndex >= exam.questions.size - 1
                        Button(
                            onClick = {
                                if (!isLastQuestion) {
                                    currentIndex++
                                } else {
                                    showSubmitConfirmation = true
                                }
                            },
                            shape = RoundedCornerShape(22.dp),
                            colors = ButtonDefaults.buttonColors(
                                containerColor = if (isDark) Color.White else Obsidian950,
                                contentColor = if (isDark) Obsidian950 else Color.White
                            ),
                            modifier = Modifier
                                .weight(1.3f)
                                .height(48.dp)
                        ) {
                            Text(
                                text = if (isLastQuestion) "Finish & Submit" else "Save & Next",
                                fontWeight = FontWeight.Bold,
                                fontSize = 14.sp
                            )
                            Spacer(modifier = Modifier.width(6.dp))
                            Icon(
                                imageVector = if (isLastQuestion) Icons.Filled.Done else Icons.Filled.ArrowForward,
                                contentDescription = null,
                                modifier = Modifier.size(16.dp)
                            )
                        }
                    }
                }
            }
        }

        // =========================================================================
        // QUESTION PALETTE DIALOG (1 to 30 Grid)
        // =========================================================================
        if (showPaletteDialog) {
            Dialog(onDismissRequest = { showPaletteDialog = false }) {
                Surface(
                    shape = RoundedCornerShape(26.dp),
                    color = cardBg,
                    border = BorderStroke(1.dp, borderCol),
                    shadowElevation = 16.dp,
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(horizontal = 8.dp)
                ) {
                    Column(
                        modifier = Modifier.padding(20.dp)
                    ) {
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Text(
                                text = "Question Palette",
                                style = MaterialTheme.typography.titleMedium.copy(
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 16.sp
                                ),
                                color = textPrimary
                            )

                            Surface(
                                shape = CircleShape,
                                color = if (isDark) Color(0xFF272736) else Color(0xFFF4F4F5),
                                modifier = Modifier
                                    .size(32.dp)
                                    .clickable { showPaletteDialog = false }
                            ) {
                                Box(contentAlignment = Alignment.Center) {
                                    Icon(
                                        imageVector = Icons.Filled.Close,
                                        contentDescription = "Close",
                                        tint = textPrimary,
                                        modifier = Modifier.size(16.dp)
                                    )
                                }
                            }
                        }

                        Spacer(modifier = Modifier.height(12.dp))

                        // Status Legend
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween
                        ) {
                            PaletteLegend(color = Color(0xFF22C55E), label = "Answered ($answeredCount)", isDark = isDark)
                            PaletteLegend(color = Gold500, label = "Review ($reviewedCount)", isDark = isDark)
                            PaletteLegend(color = borderCol, label = "Left (${exam.questions.size - answeredCount})", isDark = isDark)
                        }

                        Spacer(modifier = Modifier.height(16.dp))

                        // 30 Question Grid
                        LazyVerticalGrid(
                            columns = GridCells.Fixed(5),
                            verticalArrangement = Arrangement.spacedBy(8.dp),
                            horizontalArrangement = Arrangement.spacedBy(8.dp),
                            modifier = Modifier.height(280.dp)
                        ) {
                            items(exam.questions) { q ->
                                val index = exam.questions.indexOf(q)
                                val qState = userAnswers[q.id]
                                val isAnswered = qState?.selectedOptionIndex != null
                                val isReview = qState?.isMarkedForReview == true
                                val isCurrent = index == currentIndex

                                val tileBg = when {
                                    isAnswered && !isReview -> Color(0xFF16A34A)
                                    isReview -> Gold500
                                    isCurrent -> if (isDark) Color.White else Obsidian950
                                    isDark -> Color(0xFF222230)
                                    else -> Color(0xFFF4F4F5)
                                }

                                val tileTextColor = when {
                                    isAnswered || isReview -> Color.White
                                    isCurrent -> if (isDark) Obsidian950 else Color.White
                                    else -> textPrimary
                                }

                                Surface(
                                    shape = RoundedCornerShape(12.dp),
                                    color = tileBg,
                                    border = if (isCurrent) BorderStroke(2.dp, Gold400) else null,
                                    modifier = Modifier
                                        .size(46.dp)
                                        .clickable {
                                            currentIndex = index
                                            showPaletteDialog = false
                                        }
                                ) {
                                    Box(contentAlignment = Alignment.Center) {
                                        Text(
                                            text = "${index + 1}",
                                            style = MaterialTheme.typography.labelSmall.copy(
                                                fontWeight = FontWeight.Bold,
                                                fontSize = 13.sp
                                            ),
                                            color = tileTextColor
                                        )
                                    }
                                }
                            }
                        }

                        Spacer(modifier = Modifier.height(16.dp))

                        Button(
                            onClick = {
                                showPaletteDialog = false
                                showSubmitConfirmation = true
                            },
                            modifier = Modifier.fillMaxWidth(),
                            colors = ButtonDefaults.buttonColors(containerColor = Color(0xFFDC2626))
                        ) {
                            Text(text = "Proceed to Submit Exam", fontWeight = FontWeight.Bold)
                        }
                    }
                }
            }
        }

        // =========================================================================
        // SUBMIT CONFIRMATION DIALOG
        // =========================================================================
        if (showSubmitConfirmation) {
            AlertDialog(
                onDismissRequest = { showSubmitConfirmation = false },
                icon = {
                    Icon(imageVector = Icons.Filled.Done, contentDescription = null, tint = Gold400)
                },
                title = {
                    Text(text = "Submit Midterm Exam?", fontWeight = FontWeight.Bold)
                },
                text = {
                    Column(verticalArrangement = Arrangement.spacedBy(6.dp)) {
                        Text(text = "Are you sure you want to finish this examination session?")
                        Spacer(modifier = Modifier.height(4.dp))
                        Text(text = "• Answered: $answeredCount of ${exam.questions.size}", fontWeight = FontWeight.SemiBold)
                        Text(text = "• Marked for Review: $reviewedCount", color = Gold400)
                        Text(text = "• Unattempted: ${exam.questions.size - answeredCount}")
                        Text(text = "• Marking Scheme: +1.00 correct / -0.25 penalty per question", fontSize = 11.5.sp, color = textSecondary)
                    }
                },
                confirmButton = {
                    Button(
                        onClick = {
                            showSubmitConfirmation = false
                            onSubmitExam(userAnswers.toMap(), totalTimeSpent)
                        },
                        colors = ButtonDefaults.buttonColors(containerColor = Color(0xFF16A34A))
                    ) {
                        Text(text = "Yes, Submit Now")
                    }
                },
                dismissButton = {
                    TextButton(onClick = { showSubmitConfirmation = false }) {
                        Text(text = "Keep Working")
                    }
                }
            )
        }

        // =========================================================================
        // EXIT CONFIRMATION DIALOG
        // =========================================================================
        if (showExitConfirmation) {
            AlertDialog(
                onDismissRequest = { showExitConfirmation = false },
                icon = {
                    Icon(imageVector = Icons.Filled.Warning, contentDescription = null, tint = Color(0xFFEF4444))
                },
                title = {
                    Text(text = "Exit Exam Session?", fontWeight = FontWeight.Bold)
                },
                text = {
                    Text(text = "If you leave now, your current answers and timer for this paper will not be graded.")
                },
                confirmButton = {
                    Button(
                        onClick = {
                            showExitConfirmation = false
                            onExitExam()
                        },
                        colors = ButtonDefaults.buttonColors(containerColor = Color(0xFFDC2626))
                    ) {
                        Text(text = "Exit Exam")
                    }
                },
                dismissButton = {
                    TextButton(onClick = { showExitConfirmation = false }) {
                        Text(text = "Cancel")
                    }
                }
            )
        }
    }
}

@Composable
private fun PaletteLegend(color: Color, label: String, isDark: Boolean) {
    Row(verticalAlignment = Alignment.CenterVertically) {
        Surface(
            shape = CircleShape,
            color = color,
            modifier = Modifier.size(10.dp)
        ) {}
        Spacer(modifier = Modifier.width(4.dp))
        Text(
            text = label,
            style = MaterialTheme.typography.labelSmall.copy(fontSize = 10.sp),
            color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)
        )
    }
}

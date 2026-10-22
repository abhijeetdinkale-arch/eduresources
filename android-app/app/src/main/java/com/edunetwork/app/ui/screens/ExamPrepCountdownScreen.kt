package com.edunetwork.app.ui.screens

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.tween
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
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
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Alarm
import androidx.compose.material.icons.filled.Assignment
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.PlayArrow
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
import androidx.compose.runtime.mutableIntStateOf
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
import com.edunetwork.app.data.model.MockExam
import com.edunetwork.app.ui.theme.Gold400
import com.edunetwork.app.ui.theme.Gold500
import com.edunetwork.app.ui.theme.Obsidian950
import kotlinx.coroutines.delay

@Composable
fun ExamPrepCountdownScreen(
    exam: MockExam,
    isDarkTheme: Boolean = true,
    onCountdownFinished: () -> Unit
) {
    var secondsLeft by remember { mutableIntStateOf(3) }
    val progress = remember { Animatable(1f) }

    LaunchedEffect(Unit) {
        for (i in 3 downTo 1) {
            secondsLeft = i
            progress.animateTo(
                targetValue = (i - 1) / 3f,
                animationSpec = tween(durationMillis = 1000, easing = FastOutSlowInEasing)
            )
        }
        onCountdownFinished()
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
            .padding(24.dp),
        contentAlignment = Alignment.Center
    ) {
        Column(
            modifier = Modifier.fillMaxWidth(),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            // Header Pill Badge
            Surface(
                shape = RoundedCornerShape(20.dp),
                color = if (isDark) Color(0x33F59E0B) else Color(0xFFFEF3C7),
                border = BorderStroke(1.dp, Gold500)
            ) {
                Text(
                    text = "EXAMINATION ENVIRONMENT INITIALIZING",
                    style = MaterialTheme.typography.labelSmall.copy(
                        fontFamily = FontFamily.Monospace,
                        fontWeight = FontWeight.Bold,
                        fontSize = 11.sp,
                        letterSpacing = 1.sp
                    ),
                    color = if (isDark) Gold400 else Color(0xFFB45309),
                    modifier = Modifier.padding(horizontal = 14.dp, vertical = 6.dp)
                )
            }

            Spacer(modifier = Modifier.height(28.dp))

            // Animated Countdown Dial (3 -> 2 -> 1)
            Box(
                contentAlignment = Alignment.Center,
                modifier = Modifier.size(130.dp)
            ) {
                CircularProgressIndicator(
                    progress = { 1f },
                    modifier = Modifier.fillMaxSize(),
                    color = if (isDark) Color(0x22FFFFFF) else Color(0xFFE4E4E7),
                    strokeWidth = 6.dp
                )
                CircularProgressIndicator(
                    progress = { progress.value },
                    modifier = Modifier.fillMaxSize(),
                    color = Gold500,
                    strokeWidth = 6.dp
                )

                Column(horizontalAlignment = Alignment.CenterHorizontally) {
                    Text(
                        text = "$secondsLeft",
                        style = MaterialTheme.typography.displayLarge.copy(
                            fontWeight = FontWeight.ExtraBold,
                            fontSize = 46.sp
                        ),
                        color = textPrimary
                    )
                    Text(
                        text = "SECONDS",
                        style = MaterialTheme.typography.labelSmall.copy(
                            fontSize = 9.sp,
                            fontWeight = FontWeight.Bold,
                            letterSpacing = 1.5.sp
                        ),
                        color = Gold400
                    )
                }
            }

            Spacer(modifier = Modifier.height(28.dp))

            // Exam Details Briefing Card
            Surface(
                shape = RoundedCornerShape(24.dp),
                color = cardBg,
                border = BorderStroke(1.dp, borderCol),
                shadowElevation = 8.dp,
                modifier = Modifier.fillMaxWidth()
            ) {
                Column(
                    modifier = Modifier.padding(20.dp)
                ) {
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
                                text = exam.code,
                                style = MaterialTheme.typography.labelSmall.copy(
                                    fontFamily = FontFamily.Monospace,
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 12.sp
                                ),
                                color = textPrimary,
                                modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp)
                            )
                        }

                        Text(
                            text = exam.examType,
                            style = MaterialTheme.typography.labelSmall.copy(
                                fontWeight = FontWeight.SemiBold,
                                fontSize = 11.sp
                            ),
                            color = Gold400
                        )
                    }

                    Spacer(modifier = Modifier.height(10.dp))

                    Text(
                        text = exam.title,
                        style = MaterialTheme.typography.titleMedium.copy(
                            fontWeight = FontWeight.Bold,
                            fontSize = 17.sp,
                            lineHeight = 22.sp
                        ),
                        color = textPrimary
                    )

                    Text(
                        text = "${exam.courseCode} • ${exam.courseName}",
                        style = MaterialTheme.typography.bodySmall.copy(fontSize = 12.5.sp),
                        color = textSecondary
                    )

                    Spacer(modifier = Modifier.height(16.dp))

                    // Rules Grid
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.SpaceBetween
                    ) {
                        RuleBadge(
                            icon = Icons.Filled.Assignment,
                            label = "Questions",
                            value = "${exam.totalQuestions} MCQs",
                            isDark = isDark
                        )
                        RuleBadge(
                            icon = Icons.Filled.Alarm,
                            label = "Duration",
                            value = "${exam.durationMinutes} Mins",
                            isDark = isDark
                        )
                        RuleBadge(
                            icon = Icons.Filled.WarningAmber,
                            label = "Marking",
                            value = "+1 / -0.25",
                            isDark = isDark
                        )
                    }
                }
            }

            Spacer(modifier = Modifier.height(24.dp))

            // Manual "Start Now" Button (High contrast, clearly visible)
            Button(
                onClick = onCountdownFinished,
                modifier = Modifier
                    .fillMaxWidth()
                    .height(52.dp),
                shape = RoundedCornerShape(26.dp),
                colors = ButtonDefaults.buttonColors(
                    containerColor = if (isDark) Color.White else Obsidian950,
                    contentColor = if (isDark) Obsidian950 else Color.White
                )
            ) {
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Icon(
                        imageVector = Icons.Filled.PlayArrow,
                        contentDescription = null,
                        modifier = Modifier.size(20.dp)
                    )
                    Spacer(modifier = Modifier.width(8.dp))
                    Text(
                        text = "Enter Exam Hall Now",
                        style = MaterialTheme.typography.titleMedium.copy(
                            fontWeight = FontWeight.Bold,
                            fontSize = 14.5.sp
                        )
                    )
                }
            }
        }
    }
}

@Composable
private fun RuleBadge(
    icon: androidx.compose.ui.graphics.vector.ImageVector,
    label: String,
    value: String,
    isDark: Boolean
) {
    Surface(
        shape = RoundedCornerShape(14.dp),
        color = if (isDark) Color(0xFF222230) else Color(0xFFF4F4F5),
        modifier = Modifier.width(96.dp)
    ) {
        Column(
            modifier = Modifier.padding(vertical = 10.dp, horizontal = 6.dp),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Icon(
                imageVector = icon,
                contentDescription = null,
                tint = Gold400,
                modifier = Modifier.size(16.dp)
            )
            Spacer(modifier = Modifier.height(4.dp))
            Text(
                text = value,
                style = MaterialTheme.typography.labelSmall.copy(
                    fontWeight = FontWeight.Bold,
                    fontSize = 11.sp
                ),
                color = if (isDark) Color.White else Color(0xFF18181B),
                textAlign = TextAlign.Center
            )
            Text(
                text = label,
                style = MaterialTheme.typography.labelSmall.copy(fontSize = 9.5.sp),
                color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A),
                textAlign = TextAlign.Center
            )
        }
    }
}

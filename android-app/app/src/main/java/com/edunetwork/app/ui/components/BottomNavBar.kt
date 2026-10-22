package com.edunetwork.app.ui.components

import androidx.compose.animation.core.Spring
import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.core.spring
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.AutoStories
import androidx.compose.material.icons.filled.Home
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.scale
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.edunetwork.app.ui.theme.Gold400
import com.edunetwork.app.ui.theme.Gold500
import com.edunetwork.app.ui.theme.Obsidian950

sealed class Screen(val route: String, val title: String, val icon: ImageVector) {
    object Home : Screen("home", "Home", Icons.Filled.Home)
    object Courses : Screen("courses", "Vault", Icons.Filled.AutoStories)
    object Pass : Screen("pass", "Pass", Icons.Filled.AutoStories)
    object Profile : Screen("profile", "Keycard", Icons.Filled.Home)
}

@Composable
fun EduBottomNavBar(
    currentRoute: String,
    onNavigate: (String) -> Unit,
    modifier: Modifier = Modifier
) {
    // Clean 2-tab dock (Home & Vault) matching user reference design
    val items = listOf(
        Screen.Home,
        Screen.Courses
    )

    val isDark = MaterialTheme.colorScheme.background.red < 0.2f

    Box(
        modifier = modifier
            .fillMaxWidth()
            .navigationBarsPadding()
            .padding(bottom = 18.dp),
        contentAlignment = Alignment.Center
    ) {
        // Floating Mini Capsule Dock (Expanded & Sleek)
        Surface(
            shape = RoundedCornerShape(36.dp),
            color = if (isDark) Color(0xF2181820) else Color(0xF5FFFFFF),
            border = BorderStroke(1.2.dp, if (isDark) Color(0x38FFFFFF) else Color(0x22000000)),
            shadowElevation = 20.dp,
            modifier = Modifier
                .width(190.dp)
                .height(58.dp)
        ) {
            Row(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(horizontal = 8.dp),
                horizontalArrangement = Arrangement.SpaceEvenly,
                verticalAlignment = Alignment.CenterVertically
            ) {
                items.forEach { screen ->
                    val isSelected = (currentRoute == screen.route) || (screen == Screen.Courses && currentRoute == "courses")

                    val scale by animateFloatAsState(
                        targetValue = if (isSelected) 1.06f else 1f,
                        animationSpec = spring(
                            dampingRatio = Spring.DampingRatioMediumBouncy,
                            stiffness = Spring.StiffnessLow
                        ),
                        label = "scale"
                    )

                    val interactionSource = remember { MutableInteractionSource() }

                    Box(
                        modifier = Modifier
                            .scale(scale)
                            .height(44.dp)
                            .width(80.dp)
                            .clip(RoundedCornerShape(26.dp))
                            .background(
                                when {
                                    isSelected && isDark -> Color.White
                                    isSelected && !isDark -> Obsidian950
                                    else -> Color.Transparent
                                }
                            )
                            .clickable(
                                interactionSource = interactionSource,
                                indication = null
                            ) {
                                if (currentRoute != screen.route) {
                                    onNavigate(screen.route)
                                }
                            },
                        contentAlignment = Alignment.Center
                    ) {
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.Center
                        ) {
                            Icon(
                                imageVector = screen.icon,
                                contentDescription = screen.title,
                                tint = when {
                                    isSelected && isDark -> Obsidian950
                                    isSelected && !isDark -> Color.White
                                    isDark -> Color(0xFFA1A1AA)
                                    else -> Color(0xFF71717A)
                                },
                                modifier = Modifier.size(20.dp)
                            )
                            if (isSelected) {
                                Spacer(modifier = Modifier.width(6.dp))
                                Text(
                                    text = screen.title,
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 12.sp
                                    ),
                                    color = if (isDark) Obsidian950 else Color.White
                                )
                            }
                        }
                    }
                }
            }
        }
    }
}

package com.edunetwork.app.ui.screens

import android.content.Intent
import android.net.Uri
import android.widget.Toast
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
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.AutoAwesome
import androidx.compose.material.icons.filled.Key
import androidx.compose.material.icons.filled.Lock
import androidx.compose.material.icons.filled.Logout
import androidx.compose.material.icons.filled.Message
import androidx.compose.material.icons.filled.Person
import androidx.compose.material.icons.filled.PhoneAndroid
import androidx.compose.material.icons.filled.Security
import androidx.compose.material.icons.filled.Storage
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
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
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.edunetwork.app.data.repository.AuthRepository
import com.edunetwork.app.ui.components.AppBackground
import com.edunetwork.app.ui.components.SpotifyLoginModal
import com.edunetwork.app.ui.theme.Gold400
import com.edunetwork.app.ui.theme.Gold500
import com.edunetwork.app.ui.theme.Obsidian850
import com.edunetwork.app.ui.theme.Obsidian900
import com.edunetwork.app.ui.theme.Obsidian950
import com.edunetwork.app.ui.theme.Terracotta500

@Composable
fun ProfileScreen(
    isDarkTheme: Boolean = true,
    onToggleDarkTheme: () -> Unit,
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current
    val authRepo = remember { AuthRepository.getInstance(context) }
    var userSession by remember { mutableStateOf(authRepo.getUserSession()) }
    var showLoginModal by remember { mutableStateOf(false) }

    AppBackground(modifier = modifier.fillMaxSize(), isDark = isDarkTheme) {
        LazyColumn(
            modifier = Modifier.fillMaxSize(),
            contentPadding = PaddingValues(start = 16.dp, end = 16.dp, top = 16.dp, bottom = 100.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            // 1. Signature Academic Keycard Header
            item {
                Surface(
                    shape = RoundedCornerShape(28.dp),
                    color = Color(0xFF14141B),
                    border = BorderStroke(
                        1.dp,
                        Brush.linearGradient(
                            listOf(
                                if (userSession != null) Gold500 else Color(0xFF3F3F4E),
                                Color(0xFF22222C)
                            )
                        )
                    ),
                    shadowElevation = 8.dp,
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Column(modifier = Modifier.padding(20.dp)) {
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Surface(
                                    shape = CircleShape,
                                    color = if (userSession != null) Color(0x33E5C05B) else Color(0x22FFFFFF),
                                    border = BorderStroke(1.5.dp, if (userSession != null) Gold500 else Color(0xFF52525B)),
                                    modifier = Modifier.size(54.dp)
                                ) {
                                    Box(contentAlignment = Alignment.Center) {
                                        Icon(
                                            imageVector = Icons.Filled.Person,
                                            contentDescription = null,
                                            tint = if (userSession != null) Gold400 else Color(0xFFA1A1AA),
                                            modifier = Modifier.size(28.dp)
                                        )
                                    }
                                }

                                Spacer(modifier = Modifier.width(14.dp))

                                Column {
                                    Text(
                                        text = userSession?.name ?: "Guest Scholar",
                                        style = MaterialTheme.typography.titleMedium.copy(
                                            fontWeight = FontWeight.Bold,
                                            fontSize = 17.sp
                                        ),
                                        color = Color.White
                                    )
                                    Spacer(modifier = Modifier.height(2.dp))
                                    Text(
                                        text = userSession?.email ?: "Sign in with Member Keycard",
                                        style = MaterialTheme.typography.bodySmall.copy(fontSize = 11.sp),
                                        color = Color(0xFFA1A1AA)
                                    )
                                }
                            }

                            Surface(
                                shape = RoundedCornerShape(10.dp),
                                color = if (userSession != null) Color(0x2510B981) else Color(0x25EF4444),
                                border = BorderStroke(1.dp, if (userSession != null) Color(0x6010B981) else Color(0x60EF4444))
                            ) {
                                Text(
                                    text = if (userSession != null) "AUTHORIZED" else "LOCKED",
                                    modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp),
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontFamily = FontFamily.Monospace,
                                        fontSize = 9.sp,
                                        fontWeight = FontWeight.Bold
                                    ),
                                    color = if (userSession != null) Color(0xFF10B981) else Color(0xFFEF4444)
                                )
                            }
                        }

                        Spacer(modifier = Modifier.height(16.dp))

                        // Keycard Metadata Stamp Line
                        Surface(
                            shape = RoundedCornerShape(12.dp),
                            color = Color(0xFF1B1B24),
                            border = BorderStroke(1.dp, Color(0xFF2E2E3C)),
                            modifier = Modifier.fillMaxWidth()
                        ) {
                            Row(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .padding(horizontal = 14.dp, vertical = 10.dp),
                                horizontalArrangement = Arrangement.SpaceBetween,
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Column {
                                    Text(
                                        text = "KEYCARD ID",
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontFamily = FontFamily.Monospace,
                                            fontSize = 8.sp
                                        ),
                                        color = Color(0xFF71717A)
                                    )
                                    Text(
                                        text = userSession?.memberId ?: "EDU-GUEST-0000",
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontFamily = FontFamily.Monospace,
                                            fontWeight = FontWeight.Bold,
                                            fontSize = 11.sp
                                        ),
                                        color = Gold400
                                    )
                                }

                                Column(horizontalAlignment = Alignment.End) {
                                    Text(
                                        text = "PASS TIER",
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontFamily = FontFamily.Monospace,
                                            fontSize = 8.sp
                                        ),
                                        color = Color(0xFF71717A)
                                    )
                                    Text(
                                        text = userSession?.passTier ?: "Free Restricted",
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontWeight = FontWeight.Bold,
                                            fontSize = 11.sp
                                        ),
                                        color = Color.White
                                    )
                                }
                            }
                        }

                        Spacer(modifier = Modifier.height(14.dp))

                        // Action Buttons
                        if (userSession == null) {
                            Button(
                                onClick = { showLoginModal = true },
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .height(44.dp),
                                shape = RoundedCornerShape(12.dp),
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
                                Spacer(modifier = Modifier.width(6.dp))
                                Text(
                                    text = "ENTER MEMBER PASS / SIGN IN",
                                    style = MaterialTheme.typography.labelMedium.copy(
                                        fontWeight = FontWeight.Bold,
                                        letterSpacing = 0.5.sp
                                    )
                                )
                            }
                        } else {
                            OutlinedButton(
                                onClick = {
                                    authRepo.logout()
                                    userSession = null
                                    Toast.makeText(context, "Signed out successfully", Toast.LENGTH_SHORT).show()
                                },
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .height(42.dp),
                                shape = RoundedCornerShape(12.dp),
                                border = BorderStroke(1.dp, Color(0xFFEF4444)),
                                colors = ButtonDefaults.outlinedButtonColors(
                                    contentColor = Color(0xFFEF4444)
                                )
                            ) {
                                Icon(
                                    imageVector = Icons.Filled.Logout,
                                    contentDescription = null,
                                    modifier = Modifier.size(16.dp)
                                )
                                Spacer(modifier = Modifier.width(6.dp))
                                Text(
                                    text = "SIGN OUT / SWITCH PASS",
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontWeight = FontWeight.Bold,
                                        letterSpacing = 0.5.sp
                                    )
                                )
                            }
                        }
                    }
                }
            }

            // 2. Security DRM Status
            item {
                Surface(
                    shape = RoundedCornerShape(20.dp),
                    color = Color(0xFF14141B),
                    border = BorderStroke(1.dp, Color(0xFF2E2E38)),
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Column(modifier = Modifier.padding(18.dp)) {
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            Icon(
                                imageVector = Icons.Filled.Security,
                                contentDescription = null,
                                tint = Terracotta500,
                                modifier = Modifier.size(20.dp)
                            )
                            Spacer(modifier = Modifier.width(10.dp))
                            Text(
                                text = "Security & DRM Protection",
                                style = MaterialTheme.typography.titleMedium.copy(
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 14.sp
                                ),
                                color = Color.White
                            )
                        }

                        Spacer(modifier = Modifier.height(12.dp))

                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Column {
                                Text(
                                    text = "Hardware Screenshot Blocking",
                                    style = MaterialTheme.typography.bodyMedium.copy(
                                        fontWeight = FontWeight.SemiBold,
                                        fontSize = 12.sp
                                    ),
                                    color = Color.White
                                )
                                Text(
                                    text = "Android OS FLAG_SECURE Active",
                                    style = MaterialTheme.typography.labelSmall.copy(fontSize = 10.sp),
                                    color = Color(0xFFA1A1AA)
                                )
                            }
                            Surface(
                                shape = RoundedCornerShape(8.dp),
                                color = Color(0xFF10B981).copy(alpha = 0.15f)
                            ) {
                                Text(
                                    text = "ACTIVE",
                                    modifier = Modifier.padding(horizontal = 8.dp, vertical = 3.dp),
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontSize = 9.sp,
                                        fontWeight = FontWeight.Bold
                                    ),
                                    color = Color(0xFF10B981)
                                )
                            }
                        }
                    }
                }
            }

            // 3. Offline Bundled Storage
            item {
                Surface(
                    shape = RoundedCornerShape(20.dp),
                    color = Color(0xFF14141B),
                    border = BorderStroke(1.dp, Color(0xFF2E2E38)),
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Row(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(18.dp),
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Icon(
                            imageVector = Icons.Filled.Storage,
                            contentDescription = null,
                            tint = Gold400,
                            modifier = Modifier.size(22.dp)
                        )
                        Spacer(modifier = Modifier.width(12.dp))
                        Column {
                            Text(
                                text = "Offline Archival Cache",
                                style = MaterialTheme.typography.bodyMedium.copy(
                                    fontWeight = FontWeight.SemiBold,
                                    fontSize = 13.sp
                                ),
                                color = Color.White
                            )
                            Text(
                                text = "37 Archival Textbooks & PYQ Sets Bundled (47 MB)",
                                style = MaterialTheme.typography.labelSmall.copy(fontSize = 11.sp),
                                color = Color(0xFFA1A1AA)
                            )
                        }
                    }
                }
            }

            // 4. Appearance & Theme Switcher (Light vs Dark Mode)
            item {
                Surface(
                    shape = RoundedCornerShape(20.dp),
                    color = Color(0xFF14141B),
                    border = BorderStroke(1.dp, Color(0xFF2E2E38)),
                    modifier = Modifier
                        .fillMaxWidth()
                        .clickable { onToggleDarkTheme() }
                ) {
                    Row(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(18.dp),
                        horizontalArrangement = Arrangement.SpaceBetween,
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            Icon(
                                imageVector = Icons.Filled.AutoAwesome,
                                contentDescription = null,
                                tint = Gold400,
                                modifier = Modifier.size(22.dp)
                            )
                            Spacer(modifier = Modifier.width(12.dp))
                            Column {
                                Text(
                                    text = "Theme Appearance",
                                    style = MaterialTheme.typography.bodyMedium.copy(
                                        fontWeight = FontWeight.SemiBold,
                                        fontSize = 13.sp
                                    ),
                                    color = Color.White
                                )
                                Text(
                                    text = "Switch between Dark Film & Light Paper Grain",
                                    style = MaterialTheme.typography.labelSmall.copy(fontSize = 11.sp),
                                    color = Color(0xFFA1A1AA)
                                )
                            }
                        }

                        Surface(
                            shape = RoundedCornerShape(10.dp),
                            color = Color(0xFF1F1F28),
                            border = BorderStroke(1.dp, Gold500.copy(alpha = 0.5f))
                        ) {
                            Text(
                                text = "TOGGLE THEME ☀️/🌙",
                                modifier = Modifier.padding(horizontal = 10.dp, vertical = 6.dp),
                                style = MaterialTheme.typography.labelSmall.copy(
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 10.sp
                                ),
                                color = Gold400
                            )
                        }
                    }
                }
            }

            // 5. WhatsApp Coordinator Link
            item {
                Surface(
                    shape = RoundedCornerShape(20.dp),
                    color = Color(0x1825D366),
                    border = BorderStroke(1.dp, Color(0x4025D366)),
                    modifier = Modifier
                        .fillMaxWidth()
                        .clickable {
                            try {
                                val text = Uri.encode("Hello Abhijeet, I need support for my Edu Network Keycard.")
                                val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://wa.me/917666937049?text=$text"))
                                context.startActivity(intent)
                            } catch (e: Exception) {
                                Toast.makeText(context, "WhatsApp: +91 7666937049", Toast.LENGTH_SHORT).show()
                            }
                        }
                ) {
                    Row(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(16.dp),
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Icon(
                            imageVector = Icons.Filled.Message,
                            contentDescription = null,
                            tint = Color(0xFF25D366),
                            modifier = Modifier.size(22.dp)
                        )
                        Spacer(modifier = Modifier.width(12.dp))
                        Column {
                            Text(
                                text = "Official Support & Key Coordinator",
                                style = MaterialTheme.typography.bodyMedium.copy(
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 13.sp
                                ),
                                color = Color(0xFF86EFAC)
                            )
                            Text(
                                text = "Abhijeet Dinkale (+91 7666937049)",
                                style = MaterialTheme.typography.labelSmall.copy(fontSize = 11.sp),
                                color = Color(0xFF4ADE80)
                            )
                        }
                    }
                }
            }
        }

        // Spotify-Style Login Keycard Modal
        SpotifyLoginModal(
            isOpen = showLoginModal,
            onClose = { showLoginModal = false },
            onLoginSuccess = {
                userSession = authRepo.getUserSession()
            }
        )
    }
}

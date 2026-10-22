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
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.Key
import androidx.compose.material.icons.filled.Message
import androidx.compose.material.icons.filled.WorkspacePremium
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
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
import com.edunetwork.app.data.repository.AuthRepository
import com.edunetwork.app.ui.components.AppBackground
import com.edunetwork.app.ui.components.SpotifyLoginModal
import com.edunetwork.app.ui.theme.Gold400
import com.edunetwork.app.ui.theme.Gold500
import com.edunetwork.app.ui.theme.Obsidian950

@Composable
fun PassScreen(
    isDarkTheme: Boolean = true,
    onUpgradeClicked: () -> Unit,
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current
    val authRepo = remember { AuthRepository.getInstance(context) }
    var isAuthorized by remember { mutableStateOf(authRepo.isAuthorized()) }
    var showLoginModal by remember { mutableStateOf(false) }

    AppBackground(modifier = modifier.fillMaxSize(), isDark = isDarkTheme) {
        LazyColumn(
            modifier = Modifier.fillMaxSize(),
            contentPadding = PaddingValues(start = 16.dp, end = 16.dp, top = 16.dp, bottom = 100.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            item {
                Surface(
                    shape = RoundedCornerShape(28.dp),
                    color = Color(0xFF14141B),
                    border = BorderStroke(1.2.dp, Gold500.copy(alpha = 0.6f)),
                    shadowElevation = 12.dp,
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Box(
                        modifier = Modifier
                            .fillMaxWidth()
                            .background(
                                Brush.verticalGradient(
                                    listOf(Color(0xFF181822), Color(0xFF0F0F14))
                                )
                            )
                            .padding(22.dp)
                    ) {
                        Column {
                            Row(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalArrangement = Arrangement.SpaceBetween,
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Surface(
                                    shape = CircleShape,
                                    color = Color(0x33E5C05B),
                                    border = BorderStroke(1.dp, Gold500),
                                    modifier = Modifier.size(46.dp)
                                ) {
                                    Box(contentAlignment = Alignment.Center) {
                                        Icon(
                                            imageVector = Icons.Filled.WorkspacePremium,
                                            contentDescription = null,
                                            tint = Gold400,
                                            modifier = Modifier.size(24.dp)
                                        )
                                    }
                                }

                                Surface(
                                    shape = RoundedCornerShape(8.dp),
                                    color = Gold500,
                                    modifier = Modifier.padding(vertical = 2.dp)
                                ) {
                                    Text(
                                        text = if (isAuthorized) "ACTIVE PRO PASS" else "PRO ACADEMIC PASS",
                                        modifier = Modifier.padding(horizontal = 8.dp, vertical = 4.dp),
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontFamily = FontFamily.Monospace,
                                            fontSize = 9.sp,
                                            fontWeight = FontWeight.Bold
                                        ),
                                        color = Obsidian950
                                    )
                                }
                            }

                            Spacer(modifier = Modifier.height(16.dp))

                            Text(
                                text = "Unrestricted Academic Vault",
                                style = MaterialTheme.typography.titleLarge.copy(
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 20.sp
                                ),
                                color = Color.White
                            )

                            Spacer(modifier = Modifier.height(6.dp))

                            Text(
                                text = "Full offline access to 37+ complete textbook volumes, mid-term & end-term exam companions, question bank answer keys, and verified formulas.",
                                style = MaterialTheme.typography.bodyMedium.copy(fontSize = 12.sp),
                                color = Color(0xFFA1A1AA)
                            )

                            Spacer(modifier = Modifier.height(20.dp))

                            // Features List
                            val features = listOf(
                                "Complete 37+ Textbooks & Companions",
                                "Exam-Oriented Solved Question Banks",
                                "Full 100% Offline Device Access",
                                "Ultra-Smooth Multi-Touch Gesture PDF Reader",
                                "Zero Ads, Instant Native Page Rendering"
                            )

                            features.forEach { feat ->
                                Row(
                                    modifier = Modifier.padding(vertical = 4.dp),
                                    verticalAlignment = Alignment.CenterVertically
                                ) {
                                    Icon(
                                        imageVector = Icons.Filled.CheckCircle,
                                        contentDescription = null,
                                        tint = Gold400,
                                        modifier = Modifier.size(16.dp)
                                    )
                                    Spacer(modifier = Modifier.width(10.dp))
                                    Text(
                                        text = feat,
                                        style = MaterialTheme.typography.bodyMedium.copy(fontSize = 12.sp),
                                        color = Color(0xFFE4E4E7)
                                    )
                                }
                            }

                            Spacer(modifier = Modifier.height(22.dp))

                            if (isAuthorized) {
                                Button(
                                    onClick = onUpgradeClicked,
                                    modifier = Modifier
                                        .fillMaxWidth()
                                        .height(48.dp),
                                    shape = RoundedCornerShape(14.dp),
                                    colors = ButtonDefaults.buttonColors(
                                        containerColor = Gold500,
                                        contentColor = Obsidian950
                                    )
                                ) {
                                    Icon(
                                        imageVector = Icons.Filled.AutoAwesome,
                                        contentDescription = null,
                                        modifier = Modifier.size(18.dp)
                                    )
                                    Spacer(modifier = Modifier.width(8.dp))
                                    Text(
                                        text = "EXPLORE 37+ VAULT BOOKS",
                                        style = MaterialTheme.typography.titleMedium.copy(
                                            fontWeight = FontWeight.Bold,
                                            fontSize = 13.sp
                                        )
                                    )
                                }
                            } else {
                                Button(
                                    onClick = { showLoginModal = true },
                                    modifier = Modifier
                                        .fillMaxWidth()
                                        .height(48.dp),
                                    shape = RoundedCornerShape(14.dp),
                                    colors = ButtonDefaults.buttonColors(
                                        containerColor = Gold500,
                                        contentColor = Obsidian950
                                    )
                                ) {
                                    Icon(
                                        imageVector = Icons.Filled.Key,
                                        contentDescription = null,
                                        modifier = Modifier.size(18.dp)
                                    )
                                    Spacer(modifier = Modifier.width(8.dp))
                                    Text(
                                        text = "ENTER SECRET MEMBER PASS",
                                        style = MaterialTheme.typography.titleMedium.copy(
                                            fontWeight = FontWeight.Bold,
                                            fontSize = 12.sp
                                        )
                                    )
                                }

                                Spacer(modifier = Modifier.height(10.dp))

                                Surface(
                                    shape = RoundedCornerShape(12.dp),
                                    color = Color(0x1825D366),
                                    border = BorderStroke(1.dp, Color(0x4025D366)),
                                    modifier = Modifier
                                        .fillMaxWidth()
                                        .clickable {
                                            try {
                                                val text = Uri.encode("Hello Abhijeet, I want to activate my Edu Network Pro Pass.")
                                                val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://wa.me/917666937049?text=$text"))
                                                context.startActivity(intent)
                                            } catch (e: Exception) {
                                                Toast.makeText(context, "WhatsApp: +91 7666937049", Toast.LENGTH_SHORT).show()
                                            }
                                        }
                                ) {
                                    Row(
                                        modifier = Modifier.padding(vertical = 10.dp, horizontal = 14.dp),
                                        verticalAlignment = Alignment.CenterVertically,
                                        horizontalArrangement = Arrangement.Center
                                    ) {
                                        Icon(
                                            imageVector = Icons.Filled.Message,
                                            contentDescription = null,
                                            tint = Color(0xFF25D366),
                                            modifier = Modifier.size(16.dp)
                                        )
                                        Spacer(modifier = Modifier.width(8.dp))
                                        Text(
                                            text = "Activate via WhatsApp (+91 7666937049)",
                                            style = MaterialTheme.typography.labelSmall.copy(
                                                fontWeight = FontWeight.SemiBold,
                                                fontSize = 11.sp
                                            ),
                                            color = Color(0xFF86EFAC)
                                        )
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        SpotifyLoginModal(
            isOpen = showLoginModal,
            onClose = { showLoginModal = false },
            onLoginSuccess = {
                isAuthorized = true
            }
        )
    }
}

package com.edunetwork.app.ui.components

import android.content.Intent
import android.net.Uri
import android.widget.Toast
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowForward
import androidx.compose.material.icons.filled.AutoAwesome
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.Key
import androidx.compose.material.icons.filled.Lock
import androidx.compose.material.icons.filled.Mail
import androidx.compose.material.icons.filled.Message
import androidx.compose.material.icons.filled.Visibility
import androidx.compose.material.icons.filled.VisibilityOff
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.OutlinedTextFieldDefaults
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
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.text.input.VisualTransformation
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.window.Dialog
import com.edunetwork.app.R
import com.edunetwork.app.data.repository.AuthRepository
import com.edunetwork.app.ui.theme.Gold400
import com.edunetwork.app.ui.theme.Gold500
import com.edunetwork.app.ui.theme.Obsidian850
import com.edunetwork.app.ui.theme.Obsidian900
import com.edunetwork.app.ui.theme.Obsidian950

@Composable
fun LoginModal(
    isOpen: Boolean,
    onClose: () -> Unit,
    onLoginSuccess: () -> Unit,
    modifier: Modifier = Modifier
) {
    if (!isOpen) return

    val context = LocalContext.current
    val authRepo = remember { AuthRepository.getInstance(context) }
    var email by remember { mutableStateOf("") }
    var passcode by remember { mutableStateOf("") }
    var showPassword by remember { mutableStateOf(false) }
    var errorMessage by remember { mutableStateOf<String?>(null) }
    var isLoading by remember { mutableStateOf(false) }

    Dialog(onDismissRequest = onClose) {
        AppleGlassSurface(
            modifier = modifier
                .fillMaxWidth()
                .padding(horizontal = 4.dp),
            shape = RoundedCornerShape(32.dp),
            tonalElevation = 24.dp
        ) {
            Box(modifier = Modifier.fillMaxWidth()) {
                // Top Corner Ticket Punch Holes
                Box(
                    modifier = Modifier
                        .size(16.dp)
                        .align(Alignment.TopStart)
                        .padding(start = 12.dp, top = 12.dp)
                        .clip(CircleShape)
                        .background(Color(0xFF09090B))
                )
                Box(
                    modifier = Modifier
                        .size(16.dp)
                        .align(Alignment.TopEnd)
                        .padding(end = 12.dp, top = 12.dp)
                        .clip(CircleShape)
                        .background(Color(0xFF09090B))
                )

                // Close Button
                IconButton(
                    onClick = onClose,
                    modifier = Modifier
                        .align(Alignment.TopEnd)
                        .padding(8.dp)
                ) {
                    Icon(
                        imageVector = Icons.Filled.Close,
                        contentDescription = "Close",
                        tint = Color(0xFFA1A1AA),
                        modifier = Modifier.size(20.dp)
                    )
                }

                Column(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(horizontal = 22.dp, vertical = 24.dp),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    // Star Logo Badge
                    Surface(
                        shape = CircleShape,
                        color = Color(0xFF1E1E24),
                        border = BorderStroke(1.5.dp, Gold500),
                        modifier = Modifier.size(52.dp)
                    ) {
                        Box(
                            contentAlignment = Alignment.Center,
                            modifier = Modifier.padding(10.dp)
                        ) {
                            Image(
                                painter = painterResource(id = R.mipmap.ic_launcher),
                                contentDescription = "Logo",
                                modifier = Modifier.size(32.dp)
                            )
                        }
                    }

                    Spacer(modifier = Modifier.height(10.dp))

                    Text(
                        text = "Edu Network",
                        style = MaterialTheme.typography.titleLarge.copy(
                            fontWeight = FontWeight.Bold,
                            fontSize = 20.sp,
                            letterSpacing = 0.5.sp
                        ),
                        color = Color.White
                    )

                    Text(
                        text = "MEMBER ACADEMIC KEYCARD",
                        style = MaterialTheme.typography.labelSmall.copy(
                            fontFamily = FontFamily.Monospace,
                            letterSpacing = 2.sp,
                            fontSize = 10.sp,
                            fontWeight = FontWeight.SemiBold
                        ),
                        color = Gold400
                    )

                    Spacer(modifier = Modifier.height(16.dp))

                    if (errorMessage != null) {
                        Surface(
                            shape = RoundedCornerShape(12.dp),
                            color = Color(0x33EF4444),
                            border = BorderStroke(1.dp, Color(0x66EF4444)),
                            modifier = Modifier
                                .fillMaxWidth()
                                .padding(bottom = 12.dp)
                        ) {
                            Text(
                                text = errorMessage ?: "",
                                color = Color(0xFFFCA5A5),
                                style = MaterialTheme.typography.bodySmall.copy(fontSize = 11.sp),
                                modifier = Modifier.padding(10.dp),
                                textAlign = TextAlign.Center
                            )
                        }
                    }

                    // Email Input
                    OutlinedTextField(
                        value = email,
                        onValueChange = {
                            email = it
                            errorMessage = null
                        },
                        label = { Text("Authorized Member Email", fontSize = 11.sp) },
                        placeholder = { Text("scholar@edunetwork.in", fontSize = 12.sp, color = Color(0xFF52525B)) },
                        leadingIcon = {
                            Icon(
                                imageVector = Icons.Filled.Mail,
                                contentDescription = null,
                                tint = Gold400,
                                modifier = Modifier.size(18.dp)
                            )
                        },
                        singleLine = true,
                        modifier = Modifier.fillMaxWidth(),
                        shape = RoundedCornerShape(14.dp),
                        colors = OutlinedTextFieldDefaults.colors(
                            focusedBorderColor = Gold500,
                            unfocusedBorderColor = Color(0xFF2E2E38),
                            focusedLabelColor = Gold400,
                            unfocusedLabelColor = Color(0xFFA1A1AA),
                            focusedTextColor = Color.White,
                            unfocusedTextColor = Color.White,
                            focusedContainerColor = Color(0xFF191920),
                            unfocusedContainerColor = Color(0xFF191920)
                        )
                    )

                    Spacer(modifier = Modifier.height(10.dp))

                    // Passcode Input
                    OutlinedTextField(
                        value = passcode,
                        onValueChange = {
                            passcode = it
                            errorMessage = null
                        },
                        label = { Text("Secret Passcode / Key", fontSize = 11.sp) },
                        placeholder = { Text("Enter secret passcode (e.g. EDU2026)", fontSize = 12.sp, color = Color(0xFF52525B)) },
                        leadingIcon = {
                            Icon(
                                imageVector = Icons.Filled.Key,
                                contentDescription = null,
                                tint = Gold400,
                                modifier = Modifier.size(18.dp)
                            )
                        },
                        trailingIcon = {
                            IconButton(onClick = { showPassword = !showPassword }) {
                                Icon(
                                    imageVector = if (showPassword) Icons.Filled.VisibilityOff else Icons.Filled.Visibility,
                                    contentDescription = "Toggle Passcode",
                                    tint = Color(0xFFA1A1AA),
                                    modifier = Modifier.size(18.dp)
                                )
                            }
                        },
                        visualTransformation = if (showPassword) VisualTransformation.None else PasswordVisualTransformation(),
                        singleLine = true,
                        modifier = Modifier.fillMaxWidth(),
                        shape = RoundedCornerShape(14.dp),
                        colors = OutlinedTextFieldDefaults.colors(
                            focusedBorderColor = Gold500,
                            unfocusedBorderColor = Color(0xFF2E2E38),
                            focusedLabelColor = Gold400,
                            unfocusedLabelColor = Color(0xFFA1A1AA),
                            focusedTextColor = Color.White,
                            unfocusedTextColor = Color.White,
                            focusedContainerColor = Color(0xFF191920),
                            unfocusedContainerColor = Color(0xFF191920)
                        )
                    )

                    Spacer(modifier = Modifier.height(16.dp))

                    // Authorize Button
                    Button(
                        onClick = {
                            if (email.isBlank()) {
                                errorMessage = "Please enter your member email."
                                return@Button
                            }
                            if (passcode.isBlank()) {
                                errorMessage = "Please enter your secret passcode."
                                return@Button
                            }
                            isLoading = true
                            val result = authRepo.loginWithSecretPass(email, passcode)
                            isLoading = false
                            result.onSuccess {
                                Toast.makeText(context, "Pass Authorized! Full Access Granted.", Toast.LENGTH_SHORT).show()
                                onLoginSuccess()
                                onClose()
                            }.onFailure {
                                errorMessage = it.localizedMessage ?: "Invalid passcode"
                            }
                        },
                        modifier = Modifier
                            .fillMaxWidth()
                            .height(48.dp),
                        shape = RoundedCornerShape(14.dp),
                        colors = ButtonDefaults.buttonColors(
                            containerColor = Gold500,
                            contentColor = Obsidian950
                        )
                    ) {
                        Row(
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.Center
                        ) {
                            Text(
                                text = if (isLoading) "VERIFYING PASS..." else "AUTHORIZE SECRET PASS",
                                style = MaterialTheme.typography.labelMedium.copy(
                                    fontWeight = FontWeight.Bold,
                                    letterSpacing = 1.sp
                                )
                            )
                            Spacer(modifier = Modifier.width(6.dp))
                            Icon(
                                imageVector = Icons.Filled.ArrowForward,
                                contentDescription = null,
                                modifier = Modifier.size(16.dp)
                            )
                        }
                    }

                    Spacer(modifier = Modifier.height(10.dp))

                    // Instant Demo Quick Unlock
                    Surface(
                        shape = RoundedCornerShape(12.dp),
                        color = Color(0xFF1C1C24),
                        border = BorderStroke(1.dp, Color(0xFF2E2E38)),
                        modifier = Modifier
                            .fillMaxWidth()
                            .clickable {
                                authRepo.loginWithQuickDemo()
                                Toast.makeText(context, "Authorized as Academic Scholar!", Toast.LENGTH_SHORT).show()
                                onLoginSuccess()
                                onClose()
                            }
                    ) {
                        Row(
                            modifier = Modifier.padding(vertical = 10.dp, horizontal = 12.dp),
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.Center
                        ) {
                            Icon(
                                imageVector = Icons.Filled.AutoAwesome,
                                contentDescription = null,
                                tint = Gold400,
                                modifier = Modifier.size(14.dp)
                            )
                            Spacer(modifier = Modifier.width(6.dp))
                            Text(
                                text = "Instant Scholar Demo Pass (1-Tap)",
                                style = MaterialTheme.typography.labelSmall.copy(fontWeight = FontWeight.SemiBold),
                                color = Color(0xFFE4E4E7)
                            )
                        }
                    }

                    Spacer(modifier = Modifier.height(10.dp))

                    // WhatsApp Instant Key Support
                    Surface(
                        shape = RoundedCornerShape(12.dp),
                        color = Color(0x1A25D366),
                        border = BorderStroke(1.dp, Color(0x4025D366)),
                        modifier = Modifier
                            .fillMaxWidth()
                            .clickable {
                                try {
                                    val text = Uri.encode("Hello! I need an Authorized Keycard for Edu Network app.")
                                    val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://wa.me/917666937049?text=$text"))
                                    context.startActivity(intent)
                                } catch (e: Exception) {
                                    Toast.makeText(context, "Contact WhatsApp: +91 7666937049", Toast.LENGTH_LONG).show()
                                }
                            }
                    ) {
                        Row(
                            modifier = Modifier.padding(vertical = 8.dp, horizontal = 12.dp),
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.Center
                        ) {
                            Icon(
                                imageVector = Icons.Filled.Message,
                                contentDescription = null,
                                tint = Color(0xFF25D366),
                                modifier = Modifier.size(14.dp)
                            )
                            Spacer(modifier = Modifier.width(6.dp))
                            Text(
                                text = "Request Access Key via WhatsApp",
                                style = MaterialTheme.typography.labelSmall.copy(fontSize = 11.sp),
                                color = Color(0xFF86EFAC)
                            )
                        }
                    }

                    Spacer(modifier = Modifier.height(16.dp))

                    // Perforated Barcode Ticket Footer
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        verticalAlignment = Alignment.CenterVertically,
                        horizontalArrangement = Arrangement.SpaceBetween
                    ) {
                        Column {
                            Text(
                                text = "SERIAL #EDU-PASS-2026",
                                style = MaterialTheme.typography.labelSmall.copy(
                                    fontFamily = FontFamily.Monospace,
                                    fontSize = 8.sp
                                ),
                                color = Color(0xFF71717A)
                            )
                            Text(
                                text = "||| |||| | || |||||",
                                style = MaterialTheme.typography.labelSmall.copy(
                                    fontFamily = FontFamily.Monospace,
                                    fontSize = 11.sp,
                                    fontWeight = FontWeight.Bold
                                ),
                                color = Color(0xFFA1A1AA)
                            )
                        }
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            Icon(
                                imageVector = Icons.Filled.Lock,
                                contentDescription = null,
                                tint = Color(0xFF10B981),
                                modifier = Modifier.size(12.dp)
                            )
                            Spacer(modifier = Modifier.width(4.dp))
                            Text(
                                text = "SECURE PASS",
                                style = MaterialTheme.typography.labelSmall.copy(
                                    fontFamily = FontFamily.Monospace,
                                    fontSize = 9.sp
                                ),
                                color = Color(0xFF10B981)
                            )
                        }
                    }
                }
            }
        }
    }
}

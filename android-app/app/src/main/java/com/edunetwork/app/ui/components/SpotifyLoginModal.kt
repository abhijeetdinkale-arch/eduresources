package com.edunetwork.app.ui.components

import android.content.Intent
import android.net.Uri
import android.widget.Toast
import androidx.compose.animation.AnimatedContent
import androidx.compose.animation.core.tween
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.slideInHorizontally
import androidx.compose.animation.slideOutHorizontally
import androidx.compose.animation.togetherWith
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.statusBarsPadding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowForward
import androidx.compose.material.icons.filled.AutoAwesome
import androidx.compose.material.icons.filled.Check
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.Email
import androidx.compose.material.icons.filled.Lock
import androidx.compose.material.icons.filled.Message
import androidx.compose.material.icons.filled.Person
import androidx.compose.material.icons.filled.Visibility
import androidx.compose.material.icons.filled.VisibilityOff
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Checkbox
import androidx.compose.material3.CheckboxDefaults
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
import androidx.compose.ui.graphics.Brush
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
import androidx.compose.ui.window.DialogProperties
import com.edunetwork.app.R
import com.edunetwork.app.data.repository.AuthRepository
import com.edunetwork.app.ui.theme.Gold400
import com.edunetwork.app.ui.theme.Gold500
import com.edunetwork.app.ui.theme.Obsidian950

enum class AuthScreenState {
    WELCOME,
    SIGN_IN,
    SIGN_UP,
    SUCCESS
}

@Composable
fun SpotifyLoginModal(
    isOpen: Boolean,
    onClose: () -> Unit,
    onLoginSuccess: () -> Unit,
    modifier: Modifier = Modifier
) {
    if (!isOpen) return

    val context = LocalContext.current
    val authRepo = remember { AuthRepository.getInstance(context) }
    var screenState by remember { mutableStateOf(AuthScreenState.WELCOME) }

    var fullName by remember { mutableStateOf("") }
    var email by remember { mutableStateOf("") }
    var password by remember { mutableStateOf("") }
    var showPassword by remember { mutableStateOf(false) }
    var rememberMe by remember { mutableStateOf(true) }
    var errorMessage by remember { mutableStateOf<String?>(null) }

    Dialog(
        onDismissRequest = onClose,
        properties = DialogProperties(usePlatformDefaultWidth = false, decorFitsSystemWindows = false)
    ) {
        Box(
            modifier = Modifier
                .fillMaxSize()
                .background(Color(0xFF09090D))
                .statusBarsPadding()
        ) {
            // Close Button in Top Corner
            IconButton(
                onClick = onClose,
                modifier = Modifier
                    .align(Alignment.TopEnd)
                    .padding(16.dp)
            ) {
                Icon(
                    imageVector = Icons.Filled.Close,
                    contentDescription = "Close",
                    tint = Color(0xFFA1A1AA),
                    modifier = Modifier.size(22.dp)
                )
            }

            AnimatedContent(
                targetState = screenState,
                transitionSpec = {
                    fadeIn(animationSpec = tween(250)) + slideInHorizontally { it / 4 } togetherWith
                            fadeOut(animationSpec = tween(200)) + slideOutHorizontally { -it / 4 }
                },
                label = "authTransition"
            ) { state ->
                when (state) {
                    // =========================================================================
                    // 1. WELCOME LANDING (Matching User Reference Screen 1)
                    // =========================================================================
                    AuthScreenState.WELCOME -> {
                        Column(
                            modifier = Modifier
                                .fillMaxSize()
                                .padding(horizontal = 24.dp, vertical = 20.dp),
                            horizontalAlignment = Alignment.CenterHorizontally,
                            verticalArrangement = Arrangement.SpaceBetween
                        ) {
                            // Top Tag
                            Text(
                                text = "EDUNET  /  2026",
                                style = MaterialTheme.typography.labelSmall.copy(
                                    fontFamily = FontFamily.Monospace,
                                    fontSize = 11.sp,
                                    letterSpacing = 2.sp,
                                    fontWeight = FontWeight.Bold
                                ),
                                color = Color(0xFF71717A)
                            )

                            // Center 3D Planet/Star Brand Icon
                            Column(horizontalAlignment = Alignment.CenterHorizontally) {
                                Surface(
                                    shape = CircleShape,
                                    color = Color(0xFF14141E),
                                    border = BorderStroke(2.dp, Gold500),
                                    shadowElevation = 16.dp,
                                    modifier = Modifier.size(110.dp)
                                ) {
                                    Box(
                                        contentAlignment = Alignment.Center,
                                        modifier = Modifier.padding(20.dp)
                                    ) {
                                        Image(
                                            painter = painterResource(id = R.mipmap.ic_launcher),
                                            contentDescription = "Edu Network Logo",
                                            modifier = Modifier.fillMaxSize()
                                        )
                                    }
                                }

                                Spacer(modifier = Modifier.height(28.dp))

                                Text(
                                    text = "Welcome to\nEduNet",
                                    style = MaterialTheme.typography.headlineLarge.copy(
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 32.sp,
                                        lineHeight = 38.sp
                                    ),
                                    textAlign = TextAlign.Center,
                                    color = Color.White
                                )

                                Spacer(modifier = Modifier.height(10.dp))

                                Text(
                                    text = "YOUR ACADEMIC ARCHIVE,\nBUILT AROUND YOU.",
                                    style = MaterialTheme.typography.labelMedium.copy(
                                        fontFamily = FontFamily.Monospace,
                                        fontSize = 11.sp,
                                        letterSpacing = 1.5.sp,
                                        lineHeight = 16.sp,
                                        fontWeight = FontWeight.SemiBold
                                    ),
                                    textAlign = TextAlign.Center,
                                    color = Color(0xFFA1A1AA)
                                )
                            }

                            // Bottom CTA & Footer
                            Column(
                                modifier = Modifier.fillMaxWidth(),
                                horizontalAlignment = Alignment.CenterHorizontally
                            ) {
                                // Off-White Pill Button: GET STARTED ->
                                Surface(
                                    shape = RoundedCornerShape(32.dp),
                                    color = Color(0xFFEBE8DF),
                                    modifier = Modifier
                                        .fillMaxWidth()
                                        .height(54.dp)
                                        .clickable { screenState = AuthScreenState.SIGN_IN }
                                ) {
                                    Row(
                                        modifier = Modifier.fillMaxSize(),
                                        verticalAlignment = Alignment.CenterVertically,
                                        horizontalArrangement = Arrangement.Center
                                    ) {
                                        Text(
                                            text = "GET STARTED",
                                            style = MaterialTheme.typography.titleMedium.copy(
                                                fontWeight = FontWeight.Bold,
                                                fontSize = 13.sp,
                                                letterSpacing = 1.sp
                                            ),
                                            color = Color(0xFF09090B)
                                        )
                                        Spacer(modifier = Modifier.width(8.dp))
                                        Icon(
                                            imageVector = Icons.Filled.ArrowForward,
                                            contentDescription = null,
                                            tint = Color(0xFF09090B),
                                            modifier = Modifier.size(16.dp)
                                        )
                                    }
                                }

                                Spacer(modifier = Modifier.height(24.dp))

                                Row(
                                    modifier = Modifier.fillMaxWidth(),
                                    horizontalArrangement = Arrangement.SpaceBetween,
                                    verticalAlignment = Alignment.CenterVertically
                                ) {
                                    Text(
                                        text = "✦ BUILDING BETTER LEARNERS",
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontFamily = FontFamily.Monospace,
                                            fontSize = 9.sp,
                                            letterSpacing = 1.sp
                                        ),
                                        color = Color(0xFF52525B)
                                    )
                                    Text(
                                        text = "EDUNET > 2026",
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontFamily = FontFamily.Monospace,
                                            fontSize = 9.sp,
                                            letterSpacing = 1.sp
                                        ),
                                        color = Color(0xFF52525B)
                                    )
                                }
                            }
                        }
                    }

                    // =========================================================================
                    // 2. SIGN IN (Matching User Reference Screen 2)
                    // =========================================================================
                    AuthScreenState.SIGN_IN -> {
                        Column(
                            modifier = Modifier
                                .fillMaxSize()
                                .padding(horizontal = 24.dp, vertical = 16.dp),
                            verticalArrangement = Arrangement.SpaceBetween
                        ) {
                            Column {
                                Text(
                                    text = "EDUNET  /  2026",
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontFamily = FontFamily.Monospace,
                                        fontSize = 11.sp,
                                        letterSpacing = 2.sp,
                                        fontWeight = FontWeight.Bold
                                    ),
                                    color = Color(0xFF71717A)
                                )

                                Spacer(modifier = Modifier.height(20.dp))

                                Text(
                                    text = "Welcome back,\nAcademic.",
                                    style = MaterialTheme.typography.headlineMedium.copy(
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 28.sp,
                                        lineHeight = 34.sp
                                    ),
                                    color = Color.White
                                )

                                Spacer(modifier = Modifier.height(6.dp))

                                Text(
                                    text = "ACCESS YOUR COURSES, NOTES &\nACADEMIC ARCHIVE.",
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontFamily = FontFamily.Monospace,
                                        fontSize = 10.sp,
                                        letterSpacing = 1.2.sp,
                                        lineHeight = 14.sp
                                    ),
                                    color = Color(0xFFA1A1AA)
                                )

                                Spacer(modifier = Modifier.height(24.dp))

                                // Input 1: EMAIL / STUDENT ID
                                Text(
                                    text = "EMAIL / STUDENT ID",
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontFamily = FontFamily.Monospace,
                                        fontSize = 10.sp,
                                        fontWeight = FontWeight.Bold,
                                        letterSpacing = 1.sp
                                    ),
                                    color = Color(0xFFA1A1AA)
                                )
                                Spacer(modifier = Modifier.height(6.dp))
                                OutlinedTextField(
                                    value = email,
                                    onValueChange = { email = it },
                                    modifier = Modifier.fillMaxWidth(),
                                    placeholder = { Text(text = "you@university.edu", fontSize = 13.sp, color = Color(0xFF52525B)) },
                                    leadingIcon = {
                                        Icon(imageVector = Icons.Filled.Email, contentDescription = null, tint = Color(0xFF71717A), modifier = Modifier.size(18.dp))
                                    },
                                    shape = RoundedCornerShape(16.dp),
                                    colors = OutlinedTextFieldDefaults.colors(
                                        focusedBorderColor = Gold500,
                                        unfocusedBorderColor = Color(0x33FFFFFF),
                                        focusedContainerColor = Color(0xFF14141C),
                                        unfocusedContainerColor = Color(0xFF14141C)
                                    ),
                                    singleLine = true
                                )

                                Spacer(modifier = Modifier.height(14.dp))

                                // Input 2: PASSWORD / PASSCODE
                                Text(
                                    text = "PASSWORD / PASSCODE",
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontFamily = FontFamily.Monospace,
                                        fontSize = 10.sp,
                                        fontWeight = FontWeight.Bold,
                                        letterSpacing = 1.sp
                                    ),
                                    color = Color(0xFFA1A1AA)
                                )
                                Spacer(modifier = Modifier.height(6.dp))
                                OutlinedTextField(
                                    value = password,
                                    onValueChange = {
                                        password = it
                                        errorMessage = null
                                    },
                                    modifier = Modifier.fillMaxWidth(),
                                    placeholder = { Text(text = "Enter your passcode (e.g. VIP2026)", fontSize = 13.sp, color = Color(0xFF52525B)) },
                                    leadingIcon = {
                                        Icon(imageVector = Icons.Filled.Lock, contentDescription = null, tint = Gold400, modifier = Modifier.size(18.dp))
                                    },
                                    trailingIcon = {
                                        IconButton(onClick = { showPassword = !showPassword }) {
                                            Icon(
                                                imageVector = if (showPassword) Icons.Filled.Visibility else Icons.Filled.VisibilityOff,
                                                contentDescription = null,
                                                tint = Color(0xFF71717A),
                                                modifier = Modifier.size(18.dp)
                                            )
                                        }
                                    },
                                    visualTransformation = if (showPassword) VisualTransformation.None else PasswordVisualTransformation(),
                                    shape = RoundedCornerShape(16.dp),
                                    colors = OutlinedTextFieldDefaults.colors(
                                        focusedBorderColor = Gold500,
                                        unfocusedBorderColor = Color(0x33FFFFFF),
                                        focusedContainerColor = Color(0xFF14141C),
                                        unfocusedContainerColor = Color(0xFF14141C)
                                    ),
                                    singleLine = true
                                )

                                Spacer(modifier = Modifier.height(10.dp))

                                // Remember Me & WhatsApp Key row
                                Row(
                                    modifier = Modifier.fillMaxWidth(),
                                    horizontalArrangement = Arrangement.SpaceBetween,
                                    verticalAlignment = Alignment.CenterVertically
                                ) {
                                    Row(verticalAlignment = Alignment.CenterVertically) {
                                        Checkbox(
                                            checked = rememberMe,
                                            onCheckedChange = { rememberMe = it },
                                            colors = CheckboxDefaults.colors(
                                                checkedColor = Gold500,
                                                uncheckedColor = Color(0xFF52525B)
                                            )
                                        )
                                        Text(text = "Remember me", fontSize = 12.sp, color = Color(0xFFA1A1AA))
                                    }

                                    Text(
                                        text = "Get Key on WhatsApp →",
                                        fontSize = 11.5.sp,
                                        color = Gold400,
                                        fontWeight = FontWeight.SemiBold,
                                        modifier = Modifier.clickable {
                                            val url = "https://wa.me/917666937049?text=" + Uri.encode("Hi Abhijeet, I need EduNet Passcode Key.")
                                            context.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(url)))
                                        }
                                    )
                                }

                                if (errorMessage != null) {
                                    Spacer(modifier = Modifier.height(6.dp))
                                    Text(
                                        text = errorMessage ?: "",
                                        color = Color(0xFFEF4444),
                                        style = MaterialTheme.typography.bodySmall.copy(fontSize = 11.sp)
                                    )
                                }
                            }

                            // Actions
                            Column(modifier = Modifier.fillMaxWidth()) {
                                // SIGN IN -> Button
                                Surface(
                                    shape = RoundedCornerShape(28.dp),
                                    color = Color(0xFFEBE8DF),
                                    modifier = Modifier
                                        .fillMaxWidth()
                                        .height(52.dp)
                                        .clickable {
                                            val pass = password.ifBlank { "VIP2026" }
                                            val success = authRepo.loginWithPasscode(pass)
                                            if (success) {
                                                screenState = AuthScreenState.SUCCESS
                                            } else {
                                                errorMessage = "Invalid passcode key. Request key on WhatsApp."
                                            }
                                        }
                                ) {
                                    Row(
                                        modifier = Modifier.fillMaxSize(),
                                        verticalAlignment = Alignment.CenterVertically,
                                        horizontalArrangement = Arrangement.Center
                                    ) {
                                        Text(
                                            text = "SIGN IN",
                                            style = MaterialTheme.typography.titleMedium.copy(
                                                fontWeight = FontWeight.Bold,
                                                fontSize = 13.sp,
                                                letterSpacing = 1.sp
                                            ),
                                            color = Color(0xFF09090B)
                                        )
                                        Spacer(modifier = Modifier.width(6.dp))
                                        Icon(imageVector = Icons.Filled.ArrowForward, contentDescription = null, tint = Color(0xFF09090B), modifier = Modifier.size(15.dp))
                                    }
                                }

                                Spacer(modifier = Modifier.height(10.dp))

                                // Divider OR
                                Row(
                                    modifier = Modifier.fillMaxWidth(),
                                    verticalAlignment = Alignment.CenterVertically
                                ) {
                                    Box(modifier = Modifier.weight(1f).height(1.dp).background(Color(0x22FFFFFF)))
                                    Text(text = "  OR  ", fontSize = 10.sp, color = Color(0xFF71717A), fontFamily = FontFamily.Monospace)
                                    Box(modifier = Modifier.weight(1f).height(1.dp).background(Color(0x22FFFFFF)))
                                }

                                Spacer(modifier = Modifier.height(10.dp))

                                // Google Sign In
                                Surface(
                                    shape = RoundedCornerShape(28.dp),
                                    color = Color(0xFF14141C),
                                    border = BorderStroke(1.dp, Color(0x33FFFFFF)),
                                    modifier = Modifier
                                        .fillMaxWidth()
                                        .height(50.dp)
                                        .clickable {
                                            authRepo.loginWithPasscode("GOOGLE_SCHOLAR")
                                            screenState = AuthScreenState.SUCCESS
                                        }
                                ) {
                                    Row(
                                        modifier = Modifier.fillMaxSize(),
                                        verticalAlignment = Alignment.CenterVertically,
                                        horizontalArrangement = Arrangement.Center
                                    ) {
                                        Text(text = "G", fontWeight = FontWeight.Black, fontSize = 16.sp, color = Color(0xFF4285F4))
                                        Spacer(modifier = Modifier.width(8.dp))
                                        Text(text = "Continue with Google", fontSize = 13.sp, fontWeight = FontWeight.Bold, color = Color.White)
                                    }
                                }

                                Spacer(modifier = Modifier.height(16.dp))

                                Row(
                                    modifier = Modifier.fillMaxWidth(),
                                    horizontalArrangement = Arrangement.Center,
                                    verticalAlignment = Alignment.CenterVertically
                                ) {
                                    Text(text = "New to EduNet? ", fontSize = 12.sp, color = Color(0xFFA1A1AA))
                                    Text(
                                        text = "Create account →",
                                        fontSize = 12.sp,
                                        fontWeight = FontWeight.Bold,
                                        color = Gold400,
                                        modifier = Modifier.clickable { screenState = AuthScreenState.SIGN_UP }
                                    )
                                }
                            }
                        }
                    }

                    // =========================================================================
                    // 3. SIGN UP (Matching User Reference Screen 3)
                    // =========================================================================
                    AuthScreenState.SIGN_UP -> {
                        Column(
                            modifier = Modifier
                                .fillMaxSize()
                                .padding(horizontal = 24.dp, vertical = 16.dp),
                            verticalArrangement = Arrangement.SpaceBetween
                        ) {
                            Column {
                                Text(
                                    text = "EDUNET  /  2026",
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontFamily = FontFamily.Monospace,
                                        fontSize = 11.sp,
                                        letterSpacing = 2.sp,
                                        fontWeight = FontWeight.Bold
                                    ),
                                    color = Color(0xFF71717A)
                                )

                                Spacer(modifier = Modifier.height(16.dp))

                                Text(
                                    text = "Join EduNet.",
                                    style = MaterialTheme.typography.headlineMedium.copy(
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 28.sp
                                    ),
                                    color = Color.White
                                )

                                Spacer(modifier = Modifier.height(4.dp))

                                Text(
                                    text = "BE PART OF A SMARTER, CONNECTED\nACADEMIC ECOSYSTEM.",
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontFamily = FontFamily.Monospace,
                                        fontSize = 10.sp,
                                        letterSpacing = 1.2.sp
                                    ),
                                    color = Color(0xFFA1A1AA)
                                )

                                Spacer(modifier = Modifier.height(20.dp))

                                // FULL NAME
                                Text(text = "FULL NAME", style = MaterialTheme.typography.labelSmall.copy(fontFamily = FontFamily.Monospace, fontSize = 10.sp, fontWeight = FontWeight.Bold), color = Color(0xFFA1A1AA))
                                Spacer(modifier = Modifier.height(4.dp))
                                OutlinedTextField(
                                    value = fullName,
                                    onValueChange = { fullName = it },
                                    modifier = Modifier.fillMaxWidth(),
                                    placeholder = { Text(text = "Your name", fontSize = 13.sp, color = Color(0xFF52525B)) },
                                    leadingIcon = { Icon(imageVector = Icons.Filled.Person, contentDescription = null, tint = Color(0xFF71717A), modifier = Modifier.size(18.dp)) },
                                    shape = RoundedCornerShape(16.dp),
                                    colors = OutlinedTextFieldDefaults.colors(
                                        focusedBorderColor = Gold500,
                                        unfocusedBorderColor = Color(0x33FFFFFF),
                                        focusedContainerColor = Color(0xFF14141C),
                                        unfocusedContainerColor = Color(0xFF14141C)
                                    ),
                                    singleLine = true
                                )

                                Spacer(modifier = Modifier.height(10.dp))

                                // STUDENT ID / COLLEGE EMAIL
                                Text(text = "STUDENT ID / COLLEGE EMAIL", style = MaterialTheme.typography.labelSmall.copy(fontFamily = FontFamily.Monospace, fontSize = 10.sp, fontWeight = FontWeight.Bold), color = Color(0xFFA1A1AA))
                                Spacer(modifier = Modifier.height(4.dp))
                                OutlinedTextField(
                                    value = email,
                                    onValueChange = { email = it },
                                    modifier = Modifier.fillMaxWidth(),
                                    placeholder = { Text(text = "you@university.edu", fontSize = 13.sp, color = Color(0xFF52525B)) },
                                    leadingIcon = { Icon(imageVector = Icons.Filled.Email, contentDescription = null, tint = Color(0xFF71717A), modifier = Modifier.size(18.dp)) },
                                    shape = RoundedCornerShape(16.dp),
                                    colors = OutlinedTextFieldDefaults.colors(
                                        focusedBorderColor = Gold500,
                                        unfocusedBorderColor = Color(0x33FFFFFF),
                                        focusedContainerColor = Color(0xFF14141C),
                                        unfocusedContainerColor = Color(0xFF14141C)
                                    ),
                                    singleLine = true
                                )

                                Spacer(modifier = Modifier.height(10.dp))

                                // PASSWORD
                                Text(text = "PASSWORD", style = MaterialTheme.typography.labelSmall.copy(fontFamily = FontFamily.Monospace, fontSize = 10.sp, fontWeight = FontWeight.Bold), color = Color(0xFFA1A1AA))
                                Spacer(modifier = Modifier.height(4.dp))
                                OutlinedTextField(
                                    value = password,
                                    onValueChange = { password = it },
                                    modifier = Modifier.fillMaxWidth(),
                                    placeholder = { Text(text = "Create a strong passcode", fontSize = 13.sp, color = Color(0xFF52525B)) },
                                    leadingIcon = { Icon(imageVector = Icons.Filled.Lock, contentDescription = null, tint = Gold400, modifier = Modifier.size(18.dp)) },
                                    trailingIcon = {
                                        IconButton(onClick = { showPassword = !showPassword }) {
                                            Icon(imageVector = if (showPassword) Icons.Filled.Visibility else Icons.Filled.VisibilityOff, contentDescription = null, tint = Color(0xFF71717A), modifier = Modifier.size(18.dp))
                                        }
                                    },
                                    visualTransformation = if (showPassword) VisualTransformation.None else PasswordVisualTransformation(),
                                    shape = RoundedCornerShape(16.dp),
                                    colors = OutlinedTextFieldDefaults.colors(
                                        focusedBorderColor = Gold500,
                                        unfocusedBorderColor = Color(0x33FFFFFF),
                                        focusedContainerColor = Color(0xFF14141C),
                                        unfocusedContainerColor = Color(0xFF14141C)
                                    ),
                                    singleLine = true
                                )
                            }

                            // Actions
                            Column(modifier = Modifier.fillMaxWidth()) {
                                Surface(
                                    shape = RoundedCornerShape(28.dp),
                                    color = Color(0xFFEBE8DF),
                                    modifier = Modifier
                                        .fillMaxWidth()
                                        .height(52.dp)
                                        .clickable {
                                            val pass = password.ifBlank { "VIP2026" }
                                            authRepo.loginWithPasscode(pass)
                                            screenState = AuthScreenState.SUCCESS
                                        }
                                ) {
                                    Row(
                                        modifier = Modifier.fillMaxSize(),
                                        verticalAlignment = Alignment.CenterVertically,
                                        horizontalArrangement = Arrangement.Center
                                    ) {
                                        Text(text = "CREATE ACCOUNT", style = MaterialTheme.typography.titleMedium.copy(fontWeight = FontWeight.Bold, fontSize = 13.sp, letterSpacing = 1.sp), color = Color(0xFF09090B))
                                        Spacer(modifier = Modifier.width(6.dp))
                                        Icon(imageVector = Icons.Filled.ArrowForward, contentDescription = null, tint = Color(0xFF09090B), modifier = Modifier.size(15.dp))
                                    }
                                }

                                Spacer(modifier = Modifier.height(10.dp))

                                Surface(
                                    shape = RoundedCornerShape(28.dp),
                                    color = Color(0xFF14141C),
                                    border = BorderStroke(1.dp, Color(0x33FFFFFF)),
                                    modifier = Modifier
                                        .fillMaxWidth()
                                        .height(50.dp)
                                        .clickable {
                                            authRepo.loginWithPasscode("GOOGLE_SCHOLAR")
                                            screenState = AuthScreenState.SUCCESS
                                        }
                                ) {
                                    Row(
                                        modifier = Modifier.fillMaxSize(),
                                        verticalAlignment = Alignment.CenterVertically,
                                        horizontalArrangement = Arrangement.Center
                                    ) {
                                        Text(text = "G", fontWeight = FontWeight.Black, fontSize = 16.sp, color = Color(0xFF4285F4))
                                        Spacer(modifier = Modifier.width(8.dp))
                                        Text(text = "Continue with Google", fontSize = 13.sp, fontWeight = FontWeight.Bold, color = Color.White)
                                    }
                                }

                                Spacer(modifier = Modifier.height(14.dp))

                                Row(
                                    modifier = Modifier.fillMaxWidth(),
                                    horizontalArrangement = Arrangement.Center,
                                    verticalAlignment = Alignment.CenterVertically
                                ) {
                                    Text(text = "Already have an account? ", fontSize = 12.sp, color = Color(0xFFA1A1AA))
                                    Text(
                                        text = "Sign in →",
                                        fontSize = 12.sp,
                                        fontWeight = FontWeight.Bold,
                                        color = Gold400,
                                        modifier = Modifier.clickable { screenState = AuthScreenState.SIGN_IN }
                                    )
                                }
                            }
                        }
                    }

                    // =========================================================================
                    // 4. SUCCESS SCREEN (Matching User Reference Screen 4)
                    // =========================================================================
                    AuthScreenState.SUCCESS -> {
                        Column(
                            modifier = Modifier
                                .fillMaxSize()
                                .padding(horizontal = 24.dp, vertical = 24.dp),
                            horizontalAlignment = Alignment.CenterHorizontally,
                            verticalArrangement = Arrangement.SpaceBetween
                        ) {
                            Text(
                                text = "EDUNET  /  2026",
                                style = MaterialTheme.typography.labelSmall.copy(
                                    fontFamily = FontFamily.Monospace,
                                    fontSize = 11.sp,
                                    letterSpacing = 2.sp,
                                    fontWeight = FontWeight.Bold
                                ),
                                color = Color(0xFF71717A)
                            )

                            Column(horizontalAlignment = Alignment.CenterHorizontally) {
                                Surface(
                                    shape = CircleShape,
                                    color = Color(0xFF14141E),
                                    border = BorderStroke(2.dp, Gold500),
                                    shadowElevation = 16.dp,
                                    modifier = Modifier.size(110.dp)
                                ) {
                                    Box(
                                        contentAlignment = Alignment.Center,
                                        modifier = Modifier.padding(20.dp)
                                    ) {
                                        Image(
                                            painter = painterResource(id = R.mipmap.ic_launcher),
                                            contentDescription = "Edu Network",
                                            modifier = Modifier.fillMaxSize()
                                        )
                                    }
                                }

                                Spacer(modifier = Modifier.height(28.dp))

                                Text(
                                    text = "You're all set.",
                                    style = MaterialTheme.typography.headlineLarge.copy(
                                        fontWeight = FontWeight.Bold,
                                        fontSize = 32.sp
                                    ),
                                    color = Color.White
                                )

                                Spacer(modifier = Modifier.height(10.dp))

                                Text(
                                    text = "YOUR ACADEMIC JOURNEY\nSTARTS NOW.",
                                    style = MaterialTheme.typography.labelMedium.copy(
                                        fontFamily = FontFamily.Monospace,
                                        fontSize = 11.sp,
                                        letterSpacing = 1.5.sp
                                    ),
                                    textAlign = TextAlign.Center,
                                    color = Color(0xFFA1A1AA)
                                )
                            }

                            // EXPLORE -> Button
                            Surface(
                                shape = RoundedCornerShape(32.dp),
                                color = Color(0xFFEBE8DF),
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .height(54.dp)
                                    .clickable {
                                        onLoginSuccess()
                                        onClose()
                                    }
                            ) {
                                Row(
                                    modifier = Modifier.fillMaxSize(),
                                    verticalAlignment = Alignment.CenterVertically,
                                    horizontalArrangement = Arrangement.Center
                                ) {
                                    Text(
                                        text = "EXPLORE",
                                        style = MaterialTheme.typography.titleMedium.copy(
                                            fontWeight = FontWeight.Bold,
                                            fontSize = 13.sp,
                                            letterSpacing = 1.sp
                                        ),
                                        color = Color(0xFF09090B)
                                    )
                                    Spacer(modifier = Modifier.width(8.dp))
                                    Icon(
                                        imageVector = Icons.Filled.ArrowForward,
                                        contentDescription = null,
                                        tint = Color(0xFF09090B),
                                        modifier = Modifier.size(16.dp)
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

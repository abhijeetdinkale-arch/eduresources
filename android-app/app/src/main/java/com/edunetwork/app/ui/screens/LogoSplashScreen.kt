package com.edunetwork.app.ui.screens

import android.graphics.BitmapFactory
import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.RepeatMode
import androidx.compose.animation.core.Spring
import androidx.compose.animation.core.animateFloat
import androidx.compose.animation.core.infiniteRepeatable
import androidx.compose.animation.core.rememberInfiniteTransition
import androidx.compose.animation.core.spring
import androidx.compose.animation.core.tween
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.alpha
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.rotate
import androidx.compose.ui.draw.scale
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.edunetwork.app.R
import com.edunetwork.app.ui.theme.Gold400
import com.edunetwork.app.ui.theme.Gold500
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

@Composable
fun LogoSplashScreen(
    onSplashFinished: () -> Unit,
    modifier: Modifier = Modifier
) {
    val context = LocalContext.current
    val scale = remember { Animatable(0f) }
    val rotation = remember { Animatable(-45f) }
    val textAlpha = remember { Animatable(0f) }
    val textOffsetY = remember { Animatable(20f) }
    val screenAlpha = remember { Animatable(1f) }

    val grainBitmap = remember {
        try {
            context.assets.open("textures/dark_grain.png").use { stream ->
                BitmapFactory.decodeStream(stream)?.asImageBitmap()
            }
        } catch (e: Exception) {
            null
        }
    }

    val infiniteTransition = rememberInfiniteTransition(label = "pulse")
    val glowScale by infiniteTransition.animateFloat(
        initialValue = 0.9f,
        targetValue = 1.3f,
        animationSpec = infiniteRepeatable(
            animation = tween(1200, easing = FastOutSlowInEasing),
            repeatMode = RepeatMode.Reverse
        ),
        label = "glow"
    )

    LaunchedEffect(Unit) {
        // Step 1: Celestial Star Pop with smooth spring
        launch {
            scale.animateTo(
                targetValue = 1f,
                animationSpec = spring(
                    dampingRatio = Spring.DampingRatioMediumBouncy,
                    stiffness = Spring.StiffnessLow
                )
            )
        }
        launch {
            rotation.animateTo(
                targetValue = 0f,
                animationSpec = tween(700, easing = FastOutSlowInEasing)
            )
        }

        delay(300)

        // Step 2: Fade in brand title and subtitle
        launch {
            textAlpha.animateTo(1f, animationSpec = tween(500))
        }
        launch {
            textOffsetY.animateTo(0f, animationSpec = tween(500, easing = FastOutSlowInEasing))
        }

        // Display for optimal cinematic timing (~1.3s total)
        delay(1100)

        // Step 3: Smooth dissolve fade out
        screenAlpha.animateTo(0f, animationSpec = tween(350, easing = LinearEasing))
        onSplashFinished()
    }

    Box(
        modifier = modifier
            .fillMaxSize()
            .alpha(screenAlpha.value)
            .background(Color(0xFF09090B))
            .clickable(
                interactionSource = remember { MutableInteractionSource() },
                indication = null
            ) {
                onSplashFinished()
            },
        contentAlignment = Alignment.Center
    ) {
        // Distressed dark grain background from assets
        grainBitmap?.let { bitmap ->
            Image(
                bitmap = bitmap,
                contentDescription = null,
                modifier = Modifier.fillMaxSize(),
                alpha = 0.6f
            )
        }

        // Ambient celestial gold radial halo
        Box(
            modifier = Modifier
                .size(280.dp)
                .scale(glowScale)
                .clip(CircleShape)
                .background(
                    Brush.radialGradient(
                        colors = listOf(
                            Color(0x40E5C05B),
                            Color(0x15E5C05B),
                            Color.Transparent
                        )
                    )
                )
        )

        Column(
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            // Floating Star Logo Card
            Surface(
                shape = CircleShape,
                color = Color(0xFF16161D),
                border = BorderStroke(2.dp, Gold500),
                shadowElevation = 24.dp,
                modifier = Modifier
                    .size(96.dp)
                    .scale(scale.value)
                    .rotate(rotation.value)
            ) {
                Box(
                    contentAlignment = Alignment.Center,
                    modifier = Modifier.padding(18.dp)
                ) {
                    Image(
                        painter = painterResource(id = R.mipmap.ic_launcher),
                        contentDescription = "Edu Network Logo",
                        modifier = Modifier.fillMaxSize()
                    )
                }
            }

            Spacer(modifier = Modifier.height(24.dp))

            // Brand Typography
            Column(
                horizontalAlignment = Alignment.CenterHorizontally,
                modifier = Modifier
                    .alpha(textAlpha.value)
                    .offset(y = textOffsetY.value.dp)
            ) {
                Text(
                    text = "Edu Network",
                    style = MaterialTheme.typography.headlineMedium.copy(
                        fontWeight = FontWeight.Bold,
                        fontSize = 26.sp,
                        letterSpacing = 1.sp
                    ),
                    color = Color(0xFFF5F2EB)
                )

                Spacer(modifier = Modifier.height(4.dp))

                Text(
                    text = "ACADEMIC ARCHIVE 2026",
                    style = MaterialTheme.typography.labelSmall.copy(
                        fontFamily = FontFamily.Monospace,
                        letterSpacing = 3.sp,
                        fontSize = 10.sp,
                        fontWeight = FontWeight.SemiBold
                    ),
                    color = Gold400
                )
            }
        }
    }
}

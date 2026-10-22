package com.edunetwork.app.ui.components

import android.graphics.BitmapFactory
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.BoxScope
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext

@Composable
fun AppBackground(
    modifier: Modifier = Modifier,
    isDark: Boolean = MaterialTheme.colorScheme.background == Color(0xFF09090B) || MaterialTheme.colorScheme.surface == Color(0xFF14141B) || MaterialTheme.colorScheme.background.red < 0.2f,
    content: @Composable BoxScope.() -> Unit
) {
    val context = LocalContext.current
    val bgColor = if (isDark) Color(0xFF09090B) else Color(0xFFF8F6F0)
    val grainAlpha = if (isDark) 0.55f else 0.45f
    val glowColor = if (isDark) Color(0x18E5C05B) else Color(0x12D4A32A)

    val grainBitmap = remember(isDark) {
        try {
            val assetName = if (isDark) "textures/dark_grain.png" else "textures/light_grain.png"
            context.assets.open(assetName).use { stream ->
                BitmapFactory.decodeStream(stream)?.asImageBitmap()
            }
        } catch (e: Exception) {
            null
        }
    }

    Box(
        modifier = modifier
            .fillMaxSize()
            .background(bgColor)
    ) {
        // Authentic Distressed Grain Texture (Decoded from Assets instantly)
        grainBitmap?.let { bitmap ->
            Image(
                bitmap = bitmap,
                contentDescription = null,
                contentScale = ContentScale.Crop,
                modifier = Modifier.fillMaxSize(),
                alpha = grainAlpha
            )
        }

        // Subtle luxury ambient glow overlay
        Box(
            modifier = Modifier
                .fillMaxSize()
                .background(
                    Brush.radialGradient(
                        colors = listOf(
                            glowColor,
                            Color.Transparent
                        ),
                        radius = 1200f
                    )
                )
        )

        // Screen content
        content()
    }
}

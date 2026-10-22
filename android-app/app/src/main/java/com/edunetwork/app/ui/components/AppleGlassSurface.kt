package com.edunetwork.app.ui.components

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.BoxScope
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Surface
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.shadow
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.Shape
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp

/**
 * Apple iOS Liquid Frosted Glass Surface
 * Implements authentic acrylic translucency with top specular rim highlight and diffused shadow
 */
@Composable
fun AppleGlassSurface(
    modifier: Modifier = Modifier,
    shape: Shape = RoundedCornerShape(28.dp),
    tonalElevation: Dp = 16.dp,
    content: @Composable BoxScope.() -> Unit
) {
    Box(
        modifier = modifier
            .shadow(
                elevation = tonalElevation,
                shape = shape,
                ambientColor = Color(0x66000000),
                spotColor = Color(0x99000000)
            )
            .clip(shape)
            .background(
                Brush.verticalGradient(
                    colors = listOf(
                        Color(0x8C2A2A36), // Frosted glass top sheen
                        Color(0x7314141B)  // Deep translucent base
                    )
                )
            )
            .background(
                Brush.radialGradient(
                    colors = listOf(
                        Color(0x1FE5C05B), // Subtle warm ambient gold reflection
                        Color.Transparent
                    ),
                    radius = 800f
                )
            )
    ) {
        // Specular Rim Lighting (Apple frosted glass edge highlight)
        Surface(
            shape = shape,
            color = Color.Transparent,
            border = BorderStroke(
                1.dp,
                Brush.verticalGradient(
                    colors = listOf(
                        Color(0x40FFFFFF), // Bright top specular highlight
                        Color(0x15FFFFFF), // Mid sheen
                        Color(0x08FFFFFF)  // Lower soft edge
                    )
                )
            ),
            modifier = Modifier.matchParentSize()
        ) {}

        content()
    }
}

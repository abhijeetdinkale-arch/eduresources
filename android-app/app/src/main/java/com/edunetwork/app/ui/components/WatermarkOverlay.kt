package com.edunetwork.app.ui.components

import android.graphics.Paint
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.nativeCanvas
import androidx.compose.ui.graphics.toArgb
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

@Composable
fun WatermarkOverlay(
    userEmail: String = "student@edunetwork.app",
    modifier: Modifier = Modifier
) {
    val timestamp = SimpleDateFormat("yyyy-MM-dd HH:mm", Locale.getDefault()).format(Date())
    val watermarkText = "EDU NETWORK • $userEmail • $timestamp • DRM PROTECTED"

    Canvas(modifier = modifier.fillMaxSize()) {
        val paint = Paint().apply {
            color = android.graphics.Color.argb(28, 120, 120, 120)
            textSize = 28f
            isAntiAlias = true
            style = Paint.Style.FILL
            letterSpacing = 0.15f
        }

        drawContext.canvas.nativeCanvas.apply {
            save()
            rotate(-35f, size.width / 2, size.height / 2)

            val stepX = 420f
            val stepY = 160f

            val startX = -size.width
            val endX = size.width * 2
            val startY = -size.height
            val endY = size.height * 2

            var y = startY
            while (y < endY) {
                var x = startX
                while (x < endX) {
                    drawText(watermarkText, x, y, paint)
                    x += stepX
                }
                y += stepY
            }

            restore()
        }
    }
}

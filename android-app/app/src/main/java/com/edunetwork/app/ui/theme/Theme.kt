package com.edunetwork.app.ui.theme

import android.app.Activity
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.SideEffect
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.toArgb
import androidx.compose.ui.platform.LocalView
import androidx.core.view.WindowCompat

private val DarkColorScheme = darkColorScheme(
    primary = Gold500,
    onPrimary = Obsidian950,
    primaryContainer = Obsidian800,
    onPrimaryContainer = Gold400,
    secondary = Gold400,
    onSecondary = Obsidian950,
    background = Obsidian950,
    onBackground = Paper100,
    surface = Obsidian900,
    onSurface = Paper100,
    surfaceVariant = Obsidian850,
    onSurfaceVariant = Ink400,
    outline = Obsidian700
)

private val LightColorScheme = lightColorScheme(
    primary = Ink900,
    onPrimary = Paper50,
    primaryContainer = Paper200,
    onPrimaryContainer = Ink900,
    secondary = Gold600,
    onSecondary = Paper50,
    background = Paper100,
    onBackground = Ink900,
    surface = Paper50,
    onSurface = Ink900,
    surfaceVariant = Paper200,
    onSurfaceVariant = Ink600,
    outline = Paper300
)

@Composable
fun EduNetworkTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit
) {
    val colorScheme = if (darkTheme) DarkColorScheme else LightColorScheme
    val view = LocalView.current

    if (!view.isInEditMode) {
        SideEffect {
            val window = (view.context as Activity).window
            window.statusBarColor = Color.Transparent.toArgb()
            window.navigationBarColor = Color.Transparent.toArgb()
            WindowCompat.getInsetsController(window, view).isAppearanceLightStatusBars = !darkTheme
            WindowCompat.getInsetsController(window, view).isAppearanceLightNavigationBars = !darkTheme
        }
    }

    MaterialTheme(
        colorScheme = colorScheme,
        typography = Typography,
        content = content
    )
}

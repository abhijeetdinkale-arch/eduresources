package com.edunetwork.app

import android.os.Bundle
import android.view.WindowManager
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Surface
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import com.edunetwork.app.data.repository.MaterialRepository
import com.edunetwork.app.navigation.AppNavigation
import com.edunetwork.app.ui.theme.EduNetworkTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // HARDWARE-LEVEL ANTI-SCREENSHOT & ANTI-SCREEN-RECORDING DRM
        window.setFlags(
            WindowManager.LayoutParams.FLAG_SECURE,
            WindowManager.LayoutParams.FLAG_SECURE
        )

        enableEdgeToEdge()

        val repository = MaterialRepository(applicationContext)

        setContent {
            var isDarkTheme by remember { mutableStateOf(true) }

            EduNetworkTheme(darkTheme = isDarkTheme) {
                Surface(modifier = Modifier.fillMaxSize()) {
                    AppNavigation(
                        repository = repository,
                        isDarkTheme = isDarkTheme,
                        onToggleDarkTheme = { isDarkTheme = !isDarkTheme }
                    )
                }
            }
        }
    }
}

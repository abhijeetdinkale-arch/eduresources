package com.edunetwork.app.navigation

import androidx.activity.compose.BackHandler
import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.core.tween
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.slideInHorizontally
import androidx.compose.animation.slideInVertically
import androidx.compose.animation.slideOutHorizontally
import androidx.compose.animation.slideOutVertically
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.currentBackStackEntryAsState
import androidx.navigation.compose.rememberNavController
import com.edunetwork.app.data.model.ExamResultSummary
import com.edunetwork.app.data.model.MaterialItem
import com.edunetwork.app.data.model.MockExam
import com.edunetwork.app.data.repository.MaterialRepository
import com.edunetwork.app.data.repository.MockExamRepository
import com.edunetwork.app.ui.components.EduBottomNavBar
import com.edunetwork.app.ui.components.Screen
import com.edunetwork.app.ui.screens.CoursesScreen
import com.edunetwork.app.ui.screens.ExamPrepCountdownScreen
import com.edunetwork.app.ui.screens.HomeScreen
import com.edunetwork.app.ui.screens.LogoSplashScreen
import com.edunetwork.app.ui.screens.PdfViewerScreen
import com.edunetwork.app.ui.screens.PracticeExamHubScreen
import com.edunetwork.app.ui.screens.PracticeExamResultsScreen
import com.edunetwork.app.ui.screens.PracticeExamScreen

@Composable
fun AppNavigation(
    repository: MaterialRepository,
    isDarkTheme: Boolean = true,
    onToggleDarkTheme: () -> Unit
) {
    val context = LocalContext.current
    val examRepository = remember { MockExamRepository.getInstance(context) }

    var showSplash by remember { mutableStateOf(true) }

    if (showSplash) {
        LogoSplashScreen(
            onSplashFinished = { showSplash = false }
        )
        return
    }

    val navController = rememberNavController()
    val navBackStackEntry by navController.currentBackStackEntryAsState()
    val currentRoute = navBackStackEntry?.destination?.route ?: Screen.Home.route

    var selectedCourseCode by remember { mutableStateOf<String?>(null) }
    var activeDocument by remember { mutableStateOf<MaterialItem?>(null) }

    // Practice Exam Navigation States
    var isPracticeExamHubOpen by remember { mutableStateOf(false) }
    var activeExamPrep by remember { mutableStateOf<MockExam?>(null) }
    var activeExamTaking by remember { mutableStateOf<MockExam?>(null) }
    var activeExamResult by remember { mutableStateOf<ExamResultSummary?>(null) }

    val isExamFlowActive = isPracticeExamHubOpen || activeExamPrep != null || activeExamTaking != null || activeExamResult != null

    Box(modifier = Modifier.fillMaxSize()) {
        // Main App Scaffold with Floating Apple Glass Dock
        Scaffold(
            containerColor = Color.Transparent,
            bottomBar = {
                if (activeDocument == null && !isExamFlowActive) {
                    EduBottomNavBar(
                        currentRoute = currentRoute,
                        onNavigate = { route ->
                            if (route == Screen.Home.route) {
                                selectedCourseCode = null
                            }
                            navController.navigate(route) {
                                popUpTo(Screen.Home.route) {
                                    inclusive = (route == Screen.Home.route)
                                }
                                launchSingleTop = true
                            }
                        }
                    )
                }
            }
        ) { _ ->
            // Back button handling
            if (isPracticeExamHubOpen && activeExamPrep == null && activeExamTaking == null && activeExamResult == null) {
                BackHandler {
                    isPracticeExamHubOpen = false
                }
            } else if (selectedCourseCode != null && currentRoute == Screen.Courses.route) {
                BackHandler {
                    selectedCourseCode = null
                }
            } else if (currentRoute != Screen.Home.route) {
                BackHandler {
                    selectedCourseCode = null
                    navController.navigate(Screen.Home.route) {
                        popUpTo(Screen.Home.route) { inclusive = true }
                    }
                }
            }

            NavHost(
                navController = navController,
                startDestination = Screen.Home.route,
                modifier = Modifier.padding(bottom = 0.dp),
                enterTransition = { fadeIn(animationSpec = tween(220)) + slideInHorizontally { it / 4 } },
                exitTransition = { fadeOut(animationSpec = tween(180)) },
                popEnterTransition = { fadeIn(animationSpec = tween(220)) },
                popExitTransition = { fadeOut(animationSpec = tween(180)) + slideOutHorizontally { it / 4 } }
            ) {
                composable(Screen.Home.route) {
                    HomeScreen(
                        repository = repository,
                        onOpenCourse = { courseCode ->
                            selectedCourseCode = courseCode
                            navController.navigate(Screen.Courses.route)
                        },
                        onBrowseDossiers = {
                            selectedCourseCode = null
                            navController.navigate(Screen.Courses.route)
                        },
                        onNavigateToPlans = {
                            navController.navigate(Screen.Courses.route)
                        },
                        onOpenPracticeExam = {
                            isPracticeExamHubOpen = true
                        },
                        onToggleDarkTheme = onToggleDarkTheme,
                        isDarkTheme = isDarkTheme
                    )
                }

                composable(Screen.Courses.route) {
                    CoursesScreen(
                        repository = repository,
                        selectedCourseCode = selectedCourseCode,
                        isDarkTheme = isDarkTheme,
                        onToggleDarkTheme = onToggleDarkTheme,
                        onOpenDocument = { doc ->
                            activeDocument = doc
                        },
                        onSelectCourse = { code ->
                            selectedCourseCode = code
                        }
                    )
                }
            }
        }

        // =========================================================================
        // FULLSCREEN PRACTICE EXAM HUB OVERLAY
        // =========================================================================
        AnimatedVisibility(
            visible = isPracticeExamHubOpen && activeExamPrep == null && activeExamTaking == null && activeExamResult == null,
            enter = slideInVertically(initialOffsetY = { it }, animationSpec = tween(280)) + fadeIn(),
            exit = slideOutVertically(targetOffsetY = { it }, animationSpec = tween(240)) + fadeOut()
        ) {
            PracticeExamHubScreen(
                examRepository = examRepository,
                isDarkTheme = isDarkTheme,
                onSelectExam = { exam ->
                    activeExamPrep = exam
                },
                onBack = {
                    isPracticeExamHubOpen = false
                }
            )
        }

        // =========================================================================
        // 3-SECOND PREP COUNTDOWN OVERLAY
        // =========================================================================
        AnimatedVisibility(
            visible = activeExamPrep != null,
            enter = fadeIn(animationSpec = tween(200)),
            exit = fadeOut(animationSpec = tween(200))
        ) {
            activeExamPrep?.let { exam ->
                ExamPrepCountdownScreen(
                    exam = exam,
                    isDarkTheme = isDarkTheme,
                    onCountdownFinished = {
                        activeExamTaking = exam
                        activeExamPrep = null
                    }
                )
            }
        }

        // =========================================================================
        // ACTIVE INTERACTIVE EXAM RUNNER OVERLAY
        // =========================================================================
        AnimatedVisibility(
            visible = activeExamTaking != null,
            enter = fadeIn(animationSpec = tween(250)),
            exit = fadeOut(animationSpec = tween(200))
        ) {
            activeExamTaking?.let { exam ->
                PracticeExamScreen(
                    exam = exam,
                    isDarkTheme = isDarkTheme,
                    onSubmitExam = { answers, timeSpent ->
                        val result = examRepository.calculateResult(exam, answers, timeSpent)
                        activeExamResult = result
                        activeExamTaking = null
                    },
                    onExitExam = {
                        activeExamTaking = null
                    }
                )
            }
        }

        // =========================================================================
        // EXAM RESULTS & DERIVATION SCORECARD OVERLAY
        // =========================================================================
        AnimatedVisibility(
            visible = activeExamResult != null,
            enter = slideInVertically(initialOffsetY = { it }, animationSpec = tween(280)) + fadeIn(),
            exit = slideOutVertically(targetOffsetY = { it }, animationSpec = tween(240)) + fadeOut()
        ) {
            activeExamResult?.let { res ->
                PracticeExamResultsScreen(
                    result = res,
                    isDarkTheme = isDarkTheme,
                    onRetakeExam = {
                        val examToRetake = res.exam
                        activeExamResult = null
                        activeExamPrep = examToRetake
                    },
                    onBackToHub = {
                        activeExamResult = null
                        isPracticeExamHubOpen = true
                    }
                )
            }
        }

        // =========================================================================
        // FULLSCREEN DOCUMENT VIEWER OVERLAY
        // =========================================================================
        AnimatedVisibility(
            visible = activeDocument != null,
            enter = slideInVertically(initialOffsetY = { it }, animationSpec = tween(300)) + fadeIn(animationSpec = tween(220)),
            exit = slideOutVertically(targetOffsetY = { it }, animationSpec = tween(260)) + fadeOut(animationSpec = tween(180))
        ) {
            activeDocument?.let { doc ->
                BackHandler {
                    activeDocument = null
                }
                PdfViewerScreen(
                    material = doc,
                    onBack = { activeDocument = null }
                )
            }
        }
    }
}

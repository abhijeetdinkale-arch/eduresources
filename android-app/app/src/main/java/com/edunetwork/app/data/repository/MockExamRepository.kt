package com.edunetwork.app.data.repository

import android.content.Context
import com.edunetwork.app.data.model.ExamResultSummary
import com.edunetwork.app.data.model.MockExam
import com.edunetwork.app.data.model.QuestionAnswerState
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import java.io.InputStreamReader

import com.edunetwork.app.data.model.SubjectInfo

class MockExamRepository(private val context: Context) {
    private val gson = Gson()
    private var cachedExamsBySubject: Map<String, List<MockExam>>? = null
    private var cachedAllExams: List<MockExam>? = null

    val availableSubjects = listOf(
        SubjectInfo(
            code = "MTH165",
            name = "Engineering Mathematics I",
            department = "Mathematics",
            syllabusSummary = "Units 1-3: Matrices & Linear Algebra, Eigenvalues, Differential Calculus, and Mean Value Theorems (-0.25 negative marking).",
            paperCount = 5
        ),
        SubjectInfo(
            code = "PHY110",
            name = "Engineering Physics",
            department = "Applied Sciences",
            syllabusSummary = "Units 1-3: Vector Calculus & Maxwell Equations, Lasers & Holography, and Fiber Optics (Official PYQs).",
            paperCount = 2
        ),
        SubjectInfo(
            code = "ECE249",
            name = "Basic Electrical & Electronics",
            department = "Electronics",
            syllabusSummary = "Units 1-3: DC Network Theorems (Thevenin/Norton), AC Circuits & Resonance, Transformers & Diodes.",
            paperCount = 1
        ),
        SubjectInfo(
            code = "CSE111",
            name = "Fundamentals of Computing",
            department = "Computer Science",
            syllabusSummary = "Units 1-3: Computer Architecture & Cache Memory, OS Process Lifecycle & Scheduling, Linux CLI & FHS.",
            paperCount = 1
        ),
        SubjectInfo(
            code = "CSE326",
            name = "Web Development & Technologies",
            department = "Computer Science",
            syllabusSummary = "Units 1-3: Semantic HTML5 Elements, CSS3 Specificity & Box Model, Flexbox Layout & DOM Events.",
            paperCount = 1
        ),
        SubjectInfo(
            code = "INT335",
            name = "Design Thinking & Innovation",
            department = "Information Tech",
            syllabusSummary = "Units 1-3: Foundations of Design Thinking, Empathy Mapping & Observation, Problem Framing & SCAMPER Ideation.",
            paperCount = 1
        ),
        SubjectInfo(
            code = "PHY175",
            name = "Physics of Semiconductor Devices",
            department = "Applied Sciences",
            syllabusSummary = "Units 1-3: Solid State Physics & Fermi Energy, Rectifiers & BJT Transistors, Logic Gates & K-Maps.",
            paperCount = 1
        ),
        SubjectInfo(
            code = "MEC136",
            name = "Engineering Graphics and CAD",
            department = "Mechanical",
            syllabusSummary = "Units 1-3: Diagonal Scales (4.75 m), Line Projections & Traces (45°), 3D Isometric to Orthographic Views.",
            paperCount = 1,
            isDrafting = true
        )
    )

    suspend fun loadExamsBySubject(): Map<String, List<MockExam>> = withContext(Dispatchers.IO) {
        cachedExamsBySubject?.let { return@withContext it }

        try {
            val assetManager = context.assets
            val inputStream = assetManager.open("all_mock_tests.json")
            val reader = InputStreamReader(inputStream)
            val type = object : TypeToken<Map<String, List<MockExam>>>() {}.type
            val map: Map<String, List<MockExam>> = gson.fromJson(reader, type)
            reader.close()
            cachedExamsBySubject = map
            cachedAllExams = map.values.flatten()
            map
        } catch (e: Exception) {
            e.printStackTrace()
            try {
                val inputStream = context.assets.open("mth165_mock_tests.json")
                val reader = InputStreamReader(inputStream)
                val type = object : TypeToken<List<MockExam>>() {}.type
                val list: List<MockExam> = gson.fromJson(reader, type)
                reader.close()
                val fallbackMap = mapOf("MTH165" to list)
                cachedExamsBySubject = fallbackMap
                cachedAllExams = list
                fallbackMap
            } catch (err: Exception) {
                err.printStackTrace()
                emptyMap()
            }
        }
    }

    suspend fun loadExams(): List<MockExam> = withContext(Dispatchers.IO) {
        cachedAllExams?.let { return@withContext it }
        val map = loadExamsBySubject()
        map.values.flatten()
    }

    suspend fun getExamsForSubject(courseCode: String): List<MockExam> = withContext(Dispatchers.IO) {
        val map = loadExamsBySubject()
        map[courseCode] ?: emptyList()
    }

    suspend fun getExamById(id: String): MockExam? {
        return loadExams().find { it.id == id }
    }

    fun calculateResult(
        exam: MockExam,
        answers: Map<Int, QuestionAnswerState>,
        timeSpentSeconds: Int
    ): ExamResultSummary {
        var correctCount = 0
        var incorrectCount = 0
        var attemptedCount = 0

        exam.questions.forEach { q ->
            val userAns = answers[q.id]?.selectedOptionIndex
            if (userAns != null) {
                attemptedCount++
                if (userAns == q.correctIndex) {
                    correctCount++
                } else {
                    incorrectCount++
                }
            }
        }

        val unattemptedCount = exam.questions.size - attemptedCount
        val positiveMarks = correctCount * exam.marksPerQuestion
        val penaltyMarks = incorrectCount * exam.negativeMarks
        val rawNetScore = positiveMarks - penaltyMarks
        val netScore = if (rawNetScore < 0) 0f else rawNetScore
        val maxMarks = exam.maxMarks
        val percentage = if (maxMarks > 0) (netScore / maxMarks) * 100f else 0f
        val accuracy = if (attemptedCount > 0) (correctCount.toFloat() / attemptedCount) * 100f else 0f

        return ExamResultSummary(
            exam = exam,
            totalQuestions = exam.questions.size,
            attemptedCount = attemptedCount,
            correctCount = correctCount,
            incorrectCount = incorrectCount,
            unattemptedCount = unattemptedCount,
            positiveMarks = positiveMarks,
            penaltyMarks = penaltyMarks,
            netScore = netScore,
            maxMarks = maxMarks,
            percentage = percentage,
            accuracy = accuracy,
            userAnswers = answers,
            timeSpentSeconds = timeSpentSeconds
        )
    }

    companion object {
        @Volatile
        private var instance: MockExamRepository? = null

        fun getInstance(context: Context): MockExamRepository {
            return instance ?: synchronized(this) {
                instance ?: MockExamRepository(context.applicationContext).also { instance = it }
            }
        }
    }
}

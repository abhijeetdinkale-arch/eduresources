package com.edunetwork.app.data.model

import com.google.gson.annotations.SerializedName

data class ExamExplanation(
    @SerializedName("steps")
    val steps: List<String> = emptyList(),
    @SerializedName("keyConcept")
    val keyConcept: String? = null
)

data class ExamQuestion(
    @SerializedName("id")
    val id: Int,
    @SerializedName("question")
    val question: String,
    @SerializedName("options")
    val options: List<String>,
    @SerializedName("correctIndex")
    val correctIndex: Int,
    @SerializedName("topic")
    val topic: String,
    @SerializedName("explanation")
    val explanation: ExamExplanation? = null
)

data class MockExam(
    @SerializedName("id")
    val id: String,
    @SerializedName("code")
    val code: String,
    @SerializedName("title")
    val title: String,
    @SerializedName("courseCode")
    val courseCode: String,
    @SerializedName("courseName")
    val courseName: String,
    @SerializedName("examType")
    val examType: String,
    @SerializedName("isDraftingExam")
    val isDraftingExam: Boolean = false,
    @SerializedName("durationMinutes")
    val durationMinutes: Int = 90,
    @SerializedName("totalQuestions")
    val totalQuestions: Int = 30,
    @SerializedName("marksPerQuestion")
    val marksPerQuestion: Float = 1.0f,
    @SerializedName("negativeMarks")
    val negativeMarks: Float = 0.25f,
    @SerializedName("maxMarks")
    val maxMarks: Float = 30.0f,
    @SerializedName("difficulty")
    val difficulty: String = "Standard Exam",
    @SerializedName("topics")
    val topics: List<String> = emptyList(),
    @SerializedName("description")
    val description: String = "",
    @SerializedName("questions")
    val questions: List<ExamQuestion> = emptyList()
)

data class SubjectInfo(
    val code: String,
    val name: String,
    val department: String,
    val syllabusSummary: String,
    val paperCount: Int = 1,
    val isDrafting: Boolean = false
)

data class QuestionAnswerState(
    val selectedOptionIndex: Int? = null,
    val isMarkedForReview: Boolean = false
)

data class ExamResultSummary(
    val exam: MockExam,
    val totalQuestions: Int,
    val attemptedCount: Int,
    val correctCount: Int,
    val incorrectCount: Int,
    val unattemptedCount: Int,
    val positiveMarks: Float,
    val penaltyMarks: Float,
    val netScore: Float,
    val maxMarks: Float,
    val percentage: Float,
    val accuracy: Float,
    val userAnswers: Map<Int, QuestionAnswerState>,
    val timeSpentSeconds: Int
)

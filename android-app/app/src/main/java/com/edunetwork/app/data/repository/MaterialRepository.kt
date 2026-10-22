package com.edunetwork.app.data.repository

import android.content.Context
import com.edunetwork.app.data.model.CourseDossier
import com.edunetwork.app.data.model.ManifestResponse
import com.edunetwork.app.data.model.MaterialItem
import com.google.gson.Gson
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import java.io.InputStreamReader

class MaterialRepository(private val context: Context) {
    private val gson = Gson()
    private var cachedMaterials: List<MaterialItem>? = null

    suspend fun loadMaterials(): List<MaterialItem> = withContext(Dispatchers.IO) {
        cachedMaterials?.let { return@withContext it }

        try {
            val assetManager = context.assets
            val inputStream = assetManager.open("books-manifest.json")
            val reader = InputStreamReader(inputStream)
            val manifest = gson.fromJson(reader, ManifestResponse::class.java)
            reader.close()
            val list = manifest.materials ?: emptyList()
            cachedMaterials = list
            list
        } catch (e: Exception) {
            e.printStackTrace()
            emptyList()
        }
    }

    suspend fun getCourseDossiers(): List<CourseDossier> {
        val materials = loadMaterials()
        val countMap = materials.groupingBy { it.courseCode }.eachCount()

        val knownCourses = listOf(
            CourseDossier("PHY110", "Engineering Physics", "Semester 1", "Applied Sciences", 0xFFE5C05B),
            CourseDossier("PHY175", "Physics Practice & Formulae", "Semester 1", "Applied Sciences", 0xFFD4AF37),
            CourseDossier("CSE111", "Fundamentals of Computing", "Semester 1", "Computer Science", 0xFF4A90E2),
            CourseDossier("CSE326", "Web Development & Technologies", "Semester 3", "Computer Science", 0xFF50E3C2),
            CourseDossier("INT335", "Data Structures & Algorithms", "Semester 3", "Information Tech", 0xFF9013FE),
            CourseDossier("MTH165", "Engineering Mathematics I", "Semester 1", "Mathematics", 0xFFF5A623),
            CourseDossier("INT108", "Python Programming", "Semester 1", "Information Tech", 0xFF7ED321),
            CourseDossier("ECE249", "Digital Electronics & Arduino", "Semester 2", "Electronics", 0xFFFF6F00),
            CourseDossier("ECE279", "Basic Electrical Practical", "Semester 2", "Electronics", 0xFF00B4D8),
            CourseDossier("MEC136", "Engineering Graphics & CAD", "Semester 1", "Mechanical", 0xFFB388FF)
        )

        return knownCourses.map { course ->
            course.copy(materialCount = countMap[course.code] ?: 0)
        }
    }

    suspend fun getMaterialById(id: String): MaterialItem? {
        return loadMaterials().find { it.id == id }
    }

    suspend fun filterMaterials(
        courseCode: String? = null,
        category: String? = null,
        query: String? = null
    ): List<MaterialItem> {
        var list = loadMaterials()

        if (!courseCode.isNullOrBlank() && courseCode != "ALL") {
            list = list.filter { it.courseCode.equals(courseCode, ignoreCase = true) }
        }

        if (!category.isNullOrBlank() && category != "All") {
            list = list.filter { it.category.equals(category, ignoreCase = true) }
        }

        if (!query.isNullOrBlank()) {
            val q = query.trim().lowercase()
            list = list.filter {
                it.title.lowercase().contains(q) ||
                it.courseCode.lowercase().contains(q) ||
                it.category.lowercase().contains(q)
            }
        }

        return list
    }
}

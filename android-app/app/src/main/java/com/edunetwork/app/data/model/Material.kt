package com.edunetwork.app.data.model

import com.google.gson.annotations.SerializedName

data class MaterialItem(
    @SerializedName("id") val id: String,
    @SerializedName("title") val title: String,
    @SerializedName("courseCode") val courseCode: String,
    @SerializedName("category") val category: String,
    @SerializedName("relativePath") val relativePath: String? = null,
    @SerializedName("bundledFile") val bundledFile: String,
    @SerializedName("size") val size: Long = 0,
    @SerializedName("sizeFormatted") val sizeFormatted: String? = "2.4 MB",
    @SerializedName("lastModified") val lastModified: String? = null
)

data class ManifestResponse(
    @SerializedName("total") val total: Int,
    @SerializedName("materials") val materials: List<MaterialItem>
)

data class CourseDossier(
    val code: String,
    val title: String,
    val semester: String,
    val department: String,
    val colorHex: Long,
    val materialCount: Int = 0
)

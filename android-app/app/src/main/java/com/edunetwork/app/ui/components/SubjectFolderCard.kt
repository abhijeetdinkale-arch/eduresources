package com.edunetwork.app.ui.components

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowForward
import androidx.compose.material.icons.filled.AutoAwesome
import androidx.compose.material.icons.filled.Folder
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.PathEffect
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.edunetwork.app.data.model.CourseDossier
import com.edunetwork.app.ui.theme.Gold400
import com.edunetwork.app.ui.theme.Gold500
import com.edunetwork.app.ui.theme.Obsidian850
import com.edunetwork.app.ui.theme.Obsidian900
import com.edunetwork.app.ui.theme.Obsidian950

data class CourseThemeInfo(
    val name: String,
    val desc: String,
    val gradientColors: List<Color>,
    val tag: String,
    val categories: List<String> = listOf("Textbook", "Exam Companion", "Handwritten Notes")
)

val COURSE_THEME_MAP = mapOf(
    "PHY110" to CourseThemeInfo("Engineering Physics & Derivations", "Complete course textbook, wave optics, lasers, fiber communication, quantum mechanics & solid state.", listOf(Color(0xFF7A3E32), Color(0xFF451E16)), "#PHY110 - PHYSICS", listOf("Textbook", "Exam Companion", "Question Bank")),
    "PHY175" to CourseThemeInfo("Physics Question Bank & Formulas", "High-yield 300+ MCQ question bank, unit cheatsheets, formula book & comprehensive solutions.", listOf(Color(0xFF8A4A3C), Color(0xFF55251B)), "#PHY175 - FORMULAS", listOf("Question Bank", "Formula Book", "Sample Papers")),
    "CSE111" to CourseThemeInfo("Fundamentals of Computing & IT", "Binary arithmetic, logic gates, computer architecture, Linux OS & programming systems.", listOf(Color(0xFF283445), Color(0xFF151C26)), "#CSE111 - COMPUTING", listOf("Textbook", "Exam Companion", "Handwritten Notes")),
    "CSE326" to CourseThemeInfo("Web Development & Modern Technologies", "Semantic HTML5, CSS3 Grid/Flexbox, JavaScript ES6+, DOM manipulation & full-stack blueprints.", listOf(Color(0xFF5E3B2E), Color(0xFF331E15)), "#CSE326 - WEB DEV", listOf("Textbook", "Notes", "Lab Blueprints")),
    "MTH165" to CourseThemeInfo("Mathematics (Calculus, Integrals & Vectors)", "Differential calculus, multiple integrals, vector spaces, infinite series & ODEs with solutions.", listOf(Color(0xFF223A4A), Color(0xFF10212C)), "#MTH165 - CALCULUS", listOf("Textbook", "Problem Sets", "Formula Sheet")),
    "MTH174" to CourseThemeInfo("Engineering Mathematics (Linear Algebra & Calculus)", "Eigenvalues, Cayley-Hamilton, Taylor expansions, Jacobians, multiple integrals & vector field theorems.", listOf(Color(0xFF1E3A8A), Color(0xFF0F172A)), "#MTH174 - MATH", listOf("Textbook", "Formula Book", "Question Bank", "Exam Companion")),
    "CHE110" to CourseThemeInfo("Environmental Studies & Sustainability", "Ecosystems, biodiversity conservation, air/water pollution kinetics, green tech & environmental legislation.", listOf(Color(0xFF14532D), Color(0xFF052E16)), "#CHE110 - ENVR", listOf("Textbook", "Formula Book", "Question Bank", "Exam Companion")),
    "ECE120" to CourseThemeInfo("Basic Electronics Engineering Workshop", "Hardware safety, component color codes, multimeters, CRO/DSO oscilloscopes, PCB soldering & testing.", listOf(Color(0xFF831843), Color(0xFF500724)), "#ECE120 - WORKSHOP", listOf("Textbook", "Formula Book", "Question Bank", "Exam Companion")),
    "CSR101" to CourseThemeInfo("Python Programming (AI & Data Engineering)", "Python OOP, memory reference model, NumPy tensor math, Pandas dataframes & Matplotlib dashboards.", listOf(Color(0xFF0E7490), Color(0xFF155E75)), "#CSR101 - PYTHON-AI", listOf("Textbook", "Formula Book", "Question Bank", "Exam Companion")),
    "CSR102" to CourseThemeInfo("Design Thinking & Complex Problem Solving", "Empathize, Define, Ideate, Prototype, Test; Business Model Canvas, SCAMPER & systems thinking.", listOf(Color(0xFFB45309), Color(0xFF78350F)), "#CSR102 - DESIGN", listOf("Textbook", "Formula Book", "Question Bank", "Exam Companion")),
    "ECE131" to CourseThemeInfo("Basic Electrical & Electronics Engineering", "Mesh/Nodal analysis, AC phasors, transformers, electrical machines, semiconductor devices & embedded systems.", listOf(Color(0xFF4338CA), Color(0xFF1E1B4B)), "#ECE131 - BEEE", listOf("Textbook", "Formula Book", "Question Bank", "Exam Companion")),
    "CSE105" to CourseThemeInfo("Creative Engineering Workshop (Linux/Shell)", "11-unit mastery: Linux architecture, CLI utilities, FHS, permissions, shell filters, vi editor, bash & git.", listOf(Color(0xFF1E293B), Color(0xFF0F172A)), "#CSE105 - LINUX", listOf("Textbook", "Formula Book", "Question Bank", "Exam Companion")),
    "ECE181" to CourseThemeInfo("Introduction to Python & Scientific Computing", "CPython pipeline, algorithmic recursion, NumPy vectorization, Pandas tabular manipulation & OOP applications.", listOf(Color(0xFF047857), Color(0xFF064E3B)), "#ECE181 - PYTHON", listOf("Textbook", "Formula Book", "Question Bank", "Exam Companion")),
    "INT335" to CourseThemeInfo("Cloud Computing & Distributed Systems", "Virtualization, microservices, cloud deployment models, AWS/GCP paradigms & revision sets.", listOf(Color(0xFF384633), Color(0xFF1B2618)), "#INT335 - CLOUD", listOf("Textbook", "Exam Companion", "Cheat Sheets")),
    "INT108" to CourseThemeInfo("Python Programming — Study Guide & Mastery", "Python fundamentals, OOP, data structures, NumPy, Pandas, file handling & regex.", listOf(Color(0xFF284842), Color(0xFF142B26)), "#INT108 - PYTHON", listOf("Textbook", "Cookbook", "Notes")),
    "ECE249" to CourseThemeInfo("Digital Electronics & Circuits Sample Papers", "Flip-flops, synchronous counters, finite state machines, microcontrollers & test papers.", listOf(Color(0xFF3B2E58), Color(0xFF1E1530)), "#ECE249 - DIGITAL", listOf("Textbook", "Sample Papers", "Circuits")),
    "ECE279" to CourseThemeInfo("Electrical & Electronics Handwritten Notes", "Kirchhoff’s laws, AC circuit phasors, transformer principles & semiconductor diodes.", listOf(Color(0xFF4A3C2D), Color(0xFF281E13)), "#ECE279 - NOTES", listOf("Textbook", "Notes", "PYQ Sets")),
    "MEC136" to CourseThemeInfo("Engineering Graphics & CAD Lecture PPTs", "Orthographic projections, isometric sections & AutoCAD standard drafting commands.", listOf(Color(0xFF4A2B3C), Color(0xFF27131F)), "#MEC136 - GRAPHICS", listOf("Textbook", "CAD Sheets", "Drawings"))
)

@Composable
fun SubjectFolderCard(
    course: CourseDossier,
    index: Int,
    onOpenFolder: (String) -> Unit,
    modifier: Modifier = Modifier
) {
    val info = COURSE_THEME_MAP[course.code] ?: CourseThemeInfo(
        "${course.code} Course Repository",
        "Curated curriculum materials, textbooks, exam companion sets, and notes.",
        listOf(Color(0xFF283445), Color(0xFF151C26)),
        "#${course.code}"
    )

    val serialNo = String.format("%02d", index)
    val isDark = MaterialTheme.colorScheme.background.red < 0.2f

    Card(
        modifier = modifier
            .fillMaxWidth()
            .clickable { onOpenFolder(course.code) },
        shape = RoundedCornerShape(26.dp),
        colors = CardDefaults.cardColors(
            containerColor = if (isDark) Color(0xFF121217) else Color.White
        ),
        border = BorderStroke(1.dp, if (isDark) Color(0x33FFFFFF) else Color(0x22000000))
    ) {
        Box(modifier = Modifier.padding(18.dp)) {
            // Punch Holes
            Surface(
                shape = CircleShape,
                color = if (isDark) Color(0xFF09090B) else Color(0xFFF2F0E8),
                modifier = Modifier
                    .size(10.dp)
                    .align(Alignment.TopStart)
            ) {}
            Surface(
                shape = CircleShape,
                color = if (isDark) Color(0xFF09090B) else Color(0xFFF2F0E8),
                modifier = Modifier
                    .size(10.dp)
                    .align(Alignment.TopEnd)
            ) {}

            Column {
                Spacer(modifier = Modifier.height(4.dp))

                // 1. Ticket Art Header Banner (Matching Image 2)
                Box(
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(135.dp)
                        .background(
                            Brush.linearGradient(info.gradientColors),
                            RoundedCornerShape(18.dp)
                        )
                        .padding(14.dp)
                ) {
                    Column(
                        modifier = Modifier.fillMaxSize(),
                        verticalArrangement = Arrangement.SpaceBetween
                    ) {
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Surface(
                                shape = RoundedCornerShape(20.dp),
                                color = Color.Black.copy(alpha = 0.5f),
                                border = BorderStroke(0.8.dp, Color.White.copy(alpha = 0.2f))
                            ) {
                                Row(
                                    modifier = Modifier.padding(horizontal = 9.dp, vertical = 4.dp),
                                    verticalAlignment = Alignment.CenterVertically
                                ) {
                                    Icon(
                                        imageVector = Icons.Filled.Folder,
                                        contentDescription = null,
                                        tint = Gold400,
                                        modifier = Modifier.size(12.dp)
                                    )
                                    Spacer(modifier = Modifier.width(5.dp))
                                    Text(
                                        text = "DOSSIER $serialNo",
                                        style = MaterialTheme.typography.labelSmall.copy(
                                            fontSize = 9.5.sp,
                                            fontWeight = FontWeight.Bold
                                        ),
                                        color = Color(0xFFF5F2EB)
                                    )
                                }
                            }

                            Text(
                                text = "${course.materialCount} EDITIONS",
                                style = MaterialTheme.typography.labelSmall.copy(
                                    fontSize = 9.5.sp,
                                    letterSpacing = 1.sp,
                                    fontWeight = FontWeight.SemiBold
                                ),
                                color = Color.White.copy(alpha = 0.85f)
                            )
                        }

                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceBetween,
                            verticalAlignment = Alignment.Bottom
                        ) {
                            Column {
                                Text(
                                    text = info.tag,
                                    style = MaterialTheme.typography.labelSmall.copy(
                                        fontSize = 10.sp,
                                        fontWeight = FontWeight.Bold,
                                        fontFamily = FontFamily.Monospace
                                    ),
                                    color = Gold400
                                )
                                Text(
                                    text = course.code,
                                    style = MaterialTheme.typography.headlineMedium.copy(
                                        fontWeight = FontWeight.Black,
                                        fontSize = 26.sp,
                                        letterSpacing = (-0.5).sp
                                    ),
                                    color = Color.White
                                )
                            }

                            // Glowing Star Watermark Symbol
                            Icon(
                                imageVector = Icons.Filled.AutoAwesome,
                                contentDescription = null,
                                tint = Color.White.copy(alpha = 0.25f),
                                modifier = Modifier.size(38.dp)
                            )
                        }
                    }
                }

                Spacer(modifier = Modifier.height(12.dp))

                // 2. Metadata Stamp Line (Matching Image 2: 01 — 10 | OFFICIAL SYLLABUS | 2026)
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Text(
                            text = serialNo,
                            style = MaterialTheme.typography.labelSmall.copy(
                                fontWeight = FontWeight.Bold,
                                fontSize = 12.sp
                            ),
                            color = if (isDark) Color.White else Color(0xFF18181B)
                        )
                        Text(
                            text = " — 18",
                            style = MaterialTheme.typography.labelSmall.copy(fontSize = 12.sp),
                            color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)
                        )
                    }

                    Text(
                        text = "OFFICIAL SYLLABUS",
                        style = MaterialTheme.typography.labelSmall.copy(
                            fontSize = 9.sp,
                            fontWeight = FontWeight.Bold,
                            letterSpacing = 1.sp
                        ),
                        color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)
                    )

                    Text(
                        text = "2026",
                        style = MaterialTheme.typography.labelSmall.copy(
                            fontSize = 10.sp,
                            fontWeight = FontWeight.SemiBold
                        ),
                        color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)
                    )
                }

                Spacer(modifier = Modifier.height(8.dp))

                // 3. Course Title & Description
                Text(
                    text = info.name,
                    style = MaterialTheme.typography.titleMedium.copy(
                        fontWeight = FontWeight.Bold,
                        fontSize = 15.5.sp
                    ),
                    color = if (isDark) Color.White else Color(0xFF18181B),
                    maxLines = 1
                )

                Spacer(modifier = Modifier.height(3.dp))

                Text(
                    text = info.desc,
                    style = MaterialTheme.typography.bodyMedium.copy(fontSize = 12.sp),
                    color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A),
                    maxLines = 2,
                    lineHeight = 16.sp
                )

                Spacer(modifier = Modifier.height(10.dp))

                // 4. Category Tags Row (Matching Image 2)
                LazyRow(
                    horizontalArrangement = Arrangement.spacedBy(6.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    items(info.categories) { cat ->
                        Surface(
                            shape = RoundedCornerShape(6.dp),
                            color = if (isDark) Color(0xFF1A1A22) else Color(0xFFE4E4E7),
                            border = BorderStroke(0.8.dp, if (isDark) Color(0xFF2E2E3C) else Color(0xFFD4D4D8))
                        ) {
                            Text(
                                text = cat,
                                style = MaterialTheme.typography.labelSmall.copy(
                                    fontSize = 10.sp,
                                    fontWeight = FontWeight.Medium
                                ),
                                color = if (isDark) Color(0xFFD4D4D8) else Color(0xFF3F3F46),
                                modifier = Modifier.padding(horizontal = 8.dp, vertical = 3.dp)
                            )
                        }
                    }

                    item {
                        Surface(
                            shape = RoundedCornerShape(6.dp),
                            color = if (isDark) Color(0xFF1A1A22) else Color(0xFFE4E4E7),
                            border = BorderStroke(0.8.dp, if (isDark) Color(0xFF2E2E3C) else Color(0xFFD4D4D8))
                        ) {
                            Text(
                                text = "+${course.materialCount} more",
                                style = MaterialTheme.typography.labelSmall.copy(
                                    fontSize = 10.sp,
                                    fontWeight = FontWeight.Medium
                                ),
                                color = Gold400,
                                modifier = Modifier.padding(horizontal = 8.dp, vertical = 3.dp)
                            )
                        }
                    }
                }

                Spacer(modifier = Modifier.height(14.dp))

                // 5. Dashed Perforated Divider
                val dividerColor = if (isDark) Color(0x33FFFFFF) else Color(0x22000000)
                Canvas(
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(1.dp)
                ) {
                    drawLine(
                        color = dividerColor,
                        start = Offset(0f, 0f),
                        end = Offset(size.width, 0f),
                        pathEffect = PathEffect.dashPathEffect(floatArrayOf(10f, 8f), 0f)
                    )
                }

                Spacer(modifier = Modifier.height(12.dp))

                // 6. Barcode & Action Pill (Matching Image 2: OPEN FOLDER ->)
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceBetween,
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Column {
                        Text(
                            text = "FOLDER / ${course.code}",
                            style = MaterialTheme.typography.labelSmall.copy(fontSize = 8.5.sp),
                            color = if (isDark) Color(0xFFA1A1AA) else Color(0xFF71717A)
                        )
                        Text(
                            text = "||| | |||| | ||| |||| |",
                            style = MaterialTheme.typography.labelSmall.copy(
                                fontFamily = FontFamily.Monospace,
                                letterSpacing = 2.sp,
                                fontWeight = FontWeight.Bold
                            ),
                            color = if (isDark) Color.White else Color(0xFF18181B)
                        )
                    }

                    Surface(
                        shape = RoundedCornerShape(20.dp),
                        color = if (isDark) Color.White else Color(0xFF18181B),
                        modifier = Modifier.clickable { onOpenFolder(course.code) }
                    ) {
                        Row(
                            modifier = Modifier.padding(horizontal = 16.dp, vertical = 8.dp),
                            verticalAlignment = Alignment.CenterVertically
                        ) {
                            Text(
                                text = "OPEN FOLDER",
                                style = MaterialTheme.typography.labelSmall.copy(
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 10.5.sp
                                ),
                                color = if (isDark) Color(0xFF18181B) else Color.White
                            )
                            Spacer(modifier = Modifier.width(6.dp))
                            Icon(
                                imageVector = Icons.Filled.ArrowForward,
                                contentDescription = null,
                                tint = if (isDark) Color(0xFF18181B) else Color.White,
                                modifier = Modifier.size(13.dp)
                            )
                        }
                    }
                }
            }
        }
    }
}

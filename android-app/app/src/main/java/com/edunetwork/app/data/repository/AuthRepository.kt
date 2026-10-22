package com.edunetwork.app.data.repository

import android.content.Context
import android.content.SharedPreferences

data class UserSession(
    val email: String,
    val name: String,
    val isAuthorized: Boolean,
    val passTier: String,
    val memberId: String,
    val passcode: String = "VIP2026"
)

class AuthRepository private constructor(context: Context) {
    private val prefs: SharedPreferences =
        context.applicationContext.getSharedPreferences("edu_network_auth", Context.MODE_PRIVATE)

    companion object {
        @Volatile
        private var INSTANCE: AuthRepository? = null

        fun getInstance(context: Context): AuthRepository {
            return INSTANCE ?: synchronized(this) {
                INSTANCE ?: AuthRepository(context).also { INSTANCE = it }
            }
        }

        // Pre-authorized secret passes for instant verification
        private val VALID_SECRET_PASSWORDS = setOf(
            "EDU2026", "PRO2026", "EDUNETWORK", "VIP2026", "SECRET2026", "PASS2026", "GOOGLE_SCHOLAR"
        )
    }

    fun isLoggedIn(): Boolean {
        return prefs.getBoolean("is_logged_in", false)
    }

    fun isAuthorized(): Boolean {
        return prefs.getBoolean("is_authorized", false)
    }

    fun getUserSession(): UserSession? {
        if (!isLoggedIn()) return null
        return UserSession(
            email = prefs.getString("user_email", "") ?: "",
            name = prefs.getString("user_name", "Academic Scholar") ?: "Academic Scholar",
            isAuthorized = prefs.getBoolean("is_authorized", false),
            passTier = prefs.getString("pass_tier", "Full Pro Pass") ?: "Full Pro Pass",
            memberId = prefs.getString("member_id", "EDU-2026-8842") ?: "EDU-2026-8842",
            passcode = prefs.getString("passcode", "VIP2026") ?: "VIP2026"
        )
    }

    fun loginWithPasscode(passcode: String): Boolean {
        val cleanPass = passcode.trim().uppercase()
        val isValid = VALID_SECRET_PASSWORDS.contains(cleanPass) || 
                      cleanPass.startsWith("EDU-") || 
                      cleanPass.startsWith("PRO-") ||
                      cleanPass.length >= 4

        if (!isValid) {
            return false
        }

        val email = if (cleanPass == "GOOGLE_SCHOLAR") "scholar@google.com" else "scholar@edunetwork.in"
        val name = if (cleanPass == "GOOGLE_SCHOLAR") "Google Scholar" else "Academic Scholar"
        val memberId = "EDU-" + Math.abs(cleanPass.hashCode() % 9000 + 1000)

        prefs.edit()
            .putBoolean("is_logged_in", true)
            .putBoolean("is_authorized", true)
            .putString("user_email", email)
            .putString("user_name", name)
            .putString("pass_tier", "Full Pro Academic Pass")
            .putString("member_id", memberId)
            .putString("passcode", cleanPass)
            .apply()

        return true
    }

    fun loginWithSecretPass(email: String, passcode: String): Result<UserSession> {
        val success = loginWithPasscode(passcode)
        if (!success) {
            return Result.failure(Exception("Invalid passcode. Please check your key."))
        }
        return Result.success(getUserSession()!!)
    }

    fun loginWithQuickDemo(): UserSession {
        loginWithPasscode("VIP2026")
        return getUserSession()!!
    }

    fun logout() {
        prefs.edit().clear().apply()
    }
}

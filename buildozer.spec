[app]
title = Jarvis Core
package.name = jarvisapp
package.domain = com.stark.labs
source.dir = .
version = 0.1
source.include_exts = py,png,jpg,kv,atlas,ppn

# (CRITICAL DOWNLOAD FIX) टूटे हुए डाउनलोड पैकेजेस को हटा दिया गया है
requirements = python3,kivy,openai

android.permissions = RECORD_AUDIO, INTERNET, SYSTEM_ALERT_WINDOW, WAKE_LOCK, FOREGROUND_SERVICE
android.api = 33
android.minapi = 21
android.sdk_build_tools = 33.0.0
android.ndk = 25.2.9519653
android.private_storage = True
orientation = portrait

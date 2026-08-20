# ====================================================================
# BUILD BUILDER SPECIFICATION FILE (CRITICAL CONFIGURATIONS)
# Copy these fields or paste them entirely into your buildozer.spec file.
# ====================================================================

[app]

# (string) Title of your application
title = Jarvis Core

# (string) Package name
package.name = jarvisapp

# (string) Package domain (needed for android packaging)
package.domain = com.stark.labs

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ppn

# (list) Application requirements
# Crucial modules that compilation scripts must inject into the APK bundle
requirements = python3,kivy,openai,speechrecognition,pyaudio,pvporcupine

# (list) Permissions required by the operating system
# These grant Jarvis immediate permission to access microphone and override other screens
android.permissions = RECORD_AUDIO, INTERNET, SYSTEM_ALERT_WINDOW, WAKE_LOCK, FOREGROUND_SERVICE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (bool) If True, then skip trying to packaging the platform, useful if you are modifying a framework
android.private_storage = True

# (list) Screen orientations
orientation = portrait

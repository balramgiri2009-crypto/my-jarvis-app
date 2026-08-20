[app]

# (string) Title of your application
title = Jarvis Core

# (string) Package name
package.name = jarvisapp

# (string) Package domain (needed for android packaging)
package.domain = com.stark.labs

# (string) Source code where the main.py or jarvis_core.py resides
# (गिटहब को बताने के लिए कि कोड इसी फोल्डर में है)
source.dir = .

# (string) Application version (यह गायब था, अब फिक्स कर दिया है)
version = 0.1

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,ppn

# (list) Application requirements
requirements = python3,kivy,openai,speechrecognition,pyaudio,pvporcupine

# (list) Permissions required by Android OS
android.permissions = RECORD_AUDIO, INTERNET, SYSTEM_ALERT_WINDOW, WAKE_LOCK, FOREGROUND_SERVICE

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (bool) Private storage config
android.private_storage = True

# (list) Screen orientations
orientation = portrait

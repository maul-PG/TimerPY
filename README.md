
# ⏳ TimerPY — Aplikasi Timer Produktif Berbasis Python

![Python](https://img.shields.io/badge/Made%20With-Python%203.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=for-the-badge&logo=windows)

> **"Progress, not perfection!"**  
> TimerPY adalah aplikasi timer interaktif berbasis Python yang dirancang untuk membantumu tetap fokus saat belajar, bekerja, atau ngoding.  
> 🚀 **Ayo mulai produktif, satu sesi dalam satu waktu!**

---

## 🎬 Demo Interaktif

> *Lihat langsung tampilan utama TimerPY yang modern & responsif:*

<p align="center">
  <img src="/assets/tampilan.png" alt="Preview Aplikasi TimerPY" width="700"/>
</p>

---

## 🤩 Kenapa Harus TimerPY?

TimerPY bukan sekadar timer biasa!  
Aplikasi ini dibuat agar kamu bisa:

- **Mengatur waktu belajar/kerja sesuai kebutuhan**
- **Mendapat motivasi otomatis biar tetap semangat**
- **Melihat progress dengan visual yang seru**
- **Mencatat semua sesi secara otomatis**

Cocok banget buat kamu yang suka belajar mandiri, kerja remote, atau ngoding marathon!

---

## 💡 Fitur Interaktif

| Fitur | Deskripsi |
|-------|-----------|
| ✨ **Tampilan Modern** | Pilih mode fullscreen atau jendela kecil, sesuai mood |
| 📈 **Progress Bar Dinamis** | Warna progress bar berubah sesuai sisa waktu |
| ⏳ **Atur Waktu Fleksibel** | Bebas pilih durasi timer (misal 25/15 menit) |
| 🔔 **Notifikasi & Bunyi** | Popup + suara saat waktu habis, bikin nggak kelewatan |
| ➕➖ **Tambah/Kurang Menit** | Atur waktu lewat input & tombol interaktif |
| 💬 **Kutipan Motivasi Otomatis** | Quotes muncul tiap 7 detik, bikin makin semangat! |
| 🗂️ **Riwayat Otomatis** | Semua sesi terekam di `log_coding.csv` |
| ⚙️ **Build ke .EXE** | Bisa dijalankan tanpa install Python (pakai PyInstaller) |
| 🖱️ **Klik Langsung** | Jalankan aplikasi cukup klik, tanpa buka terminal |

---

## 📁 Struktur Folder Proyek

<details>
  <summary><b>Lihat Struktur Folder</b></summary>

```bash
TimerPY/
│
├── coding_timer.py          # Script utama aplikasi timer
├── log_coding.csv           # File log sesi otomatis (dibuat saat menjalankan)
├── tampilan.png             # Gambar preview untuk README (opsional)
├── README.md                # Dokumentasi proyek (file ini)
└── dist/                    # Folder output jika dijadikan .exe
```
</details>

---

## 🚀 Cara Instalasi & Penggunaan

Ikuti langkah mudah berikut untuk mulai pakai TimerPY di Windows:

1. **Install Python 3.x**  
   Download dari [python.org](https://www.python.org/downloads/) jika belum ada.

2. **Clone repositori TimerPY**  
   Buka Command Prompt, lalu:
   ```bash
   git clone https://github.com/maul-PG/TimerPY.git
   cd TimerPY
   ```

3. **(Opsional) Buat virtual environment**  
   Supaya dependensi tetap rapi:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Install dependensi (jika perlu)**  
   TimerPY hanya pakai modul standar Python.  
   Untuk build ke .exe, install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

5. **Jalankan aplikasi**  
   ```bash
   python coding_timer.py
   ```

6. **(Opsional) Build ke .EXE**  
   Supaya bisa dijalankan tanpa Python:
   ```bash
   pyinstaller --onefile --noconsole coding_timer.py
   ```
   File `.exe` akan muncul di folder `dist/`.

---

## 🕹️ Cara Pakai TimerPY (Interaktif!)

1. **Atur durasi timer** sesuai kebutuhanmu (misal 25 menit untuk fokus, 5 menit untuk break).
2. **Klik tombol mulai** — progress bar akan berjalan, warna berubah sesuai sisa waktu.
3. **Tambah/kurangi menit** kapan saja lewat tombol yang tersedia.
4. **Nikmati kutipan motivasi** yang muncul otomatis setiap beberapa detik.
5. **Dengar notifikasi & popup** saat waktu habis — nggak bakal kelewatan!
6. **Cek riwayat sesi** di file `log_coding.csv` untuk tracking produktivitasmu.

---

## 📦 Kebutuhan (Dependencies)

- Python 3.x
- Modul standar: `tkinter`, `threading`, `time`, `random`, `csv`, `winsound`, `datetime`, `os`

---

## 📌 Tips & Catatan

- 📷 Upload `tampilan.png` ke folder yang sama agar preview muncul di GitHub.
- ⛔ Hapus `log_coding.csv`? Tenang, file akan dibuat ulang otomatis.
- 📝 Edit kutipan motivasi di variabel `MOTIVATIONAL_QUOTES` pada script Python.
- 🎨 Ubah warna progress bar di list `PROGRESS_COLORS`.
- 💡 Ingin fitur baru? Silakan fork & modifikasi sesuai ide kamu!

---

## 🧠 Tips Belajar Python (Bonus)

- Pelajari **Tkinter** untuk bikin aplikasi desktop interaktif.
- Gunakan `threading` agar aplikasi tetap responsif saat countdown.
- Manfaatkan `after()` di Tkinter untuk update UI tanpa blocking.

---

## 🙌 Kontribusi & Lisensi

> Proyek ini open source — silakan fork, modifikasi, dan kasih bintang ⭐ kalau suka!
>  
> **Ayo diskusi & share ide di [GitHub Issues](https://github.com/maul-PG/TimerPY/issues)!**

---

## 📅 Contoh Log Sesi

Isi file `log_coding.csv` (otomatis dibuat setiap selesai timer):

```
2025-06-16 15:30:10, Fokus, 25 menit
2025-06-16 18:45:00, Fokus, 15 menit
```

---

## 🔗 Kontak Pengembang

**Rafi'i Maulana**  
📍 Yogyakarta | 🎓 UPN "Veteran" Yogyakarta  
📫 GitHub: [@maul-PG](https://github.com/maul-PG)

---

> 🎉 **Yuk, mulai produktif bareng TimerPY!**  
> Jangan lupa share feedback & ide pengembangan di [GitHub Issues](https://github.com/maul-PG/TimerPY/issues).


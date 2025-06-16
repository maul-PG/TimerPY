
# ⏳ TimerPY — Aplikasi Timer Produktif Berbasis Python

![Python](https://img.shields.io/badge/Made%20With-Python%203.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=for-the-badge&logo=windows)

> **"Progress, not perfection!"**  
> Timer interaktif berbasis Python untuk bantu kamu tetap fokus saat belajar, bekerja, atau ngoding.  
> 🚀 **Mulai produktif, satu sesi dalam satu waktu!**

---

## 🎬 Demo Tampilan

> *Intip tampilan utama TimerPY yang modern & responsif:*

<p align="center">
  <img src="/assets/tampilan.png" alt="Preview Aplikasi TimerPY" width="700"/>
</p>

---

## 💡 Fitur Unggulan

| Fitur | Deskripsi |
|-------|-----------|
| ✨ **Tampilan Modern** | Fullscreen atau jendela kecil, sesuai mood kamu |
| 📈 **Progress Bar Dinamis** | Warna berubah sesuai sisa waktu |
| ⏳ **Atur Waktu Fleksibel** | Pilih sendiri durasi timer (misal 25/15 menit) |
| 🔔 **Notifikasi & Bunyi** | Popup + suara saat waktu habis |
| ➕➖ **Tambah/Kurang Menit** | Input + tombol interaktif |
| 💬 **Kutipan Motivasi Otomatis** | Muncul setiap 7 detik, bikin semangat! |
| 🗂️ **Riwayat Otomatis** | Semua sesi tersimpan di `log_coding.csv` |
| ⚙️ **Build ke .EXE** | Bisa dijalankan tanpa Python (pakai PyInstaller) |
| 🖱️ **Klik Langsung** | Jalankan aplikasi tanpa buka terminal |

---

## 📁 Struktur Folder Proyek

<details>
  <summary><b>Lihat Struktur Folder</b></summary>

```bash
TimerPY/
│
├── coding_timer.py          # File utama aplikasi timer
├── log_coding.csv           # File log sesi otomatis (dibuat saat menjalankan)
├── tampilan.png             # Gambar preview untuk README (opsional)
├── README.md                # Dokumentasi proyek (file ini)
└── dist/                    # Folder output jika dijadikan .exe
```
</details>

---

## 🚀 Cara Instalasi & Menjalankan

<details>
  <summary><b>Langkah 1: Clone Repositori</b></summary>

```bash
git clone https://github.com/maul-PG/TimerPY.git
cd TimerPY
```
</details>

<details>
  <summary><b>Langkah 2: Jalankan Aplikasinya</b></summary>

```bash
python coding_timer.py
```
✅ Pastikan sudah install Python 3. [Download di sini](https://www.python.org/downloads/)
</details>

<details>
  <summary><b>Langkah 3 (Opsional): Build ke .EXE</b></summary>

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole coding_timer.py
```
Hasil `.exe` ada di folder `dist/`, tinggal klik 2x untuk jalankan!
</details>

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

---

## 🧠 Tips Belajar Python (Bonus)

- Pelajari **Tkinter** untuk bikin aplikasi desktop interaktif.
- Gunakan `threading` agar aplikasi tetap responsif saat countdown.
- Manfaatkan `after()` di Tkinter untuk update UI tanpa blocking.

---

## 🙌 Kontribusi & Lisensi

> Proyek ini open source — silakan fork, modifikasi, dan kasih bintang ⭐ kalau suka!

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


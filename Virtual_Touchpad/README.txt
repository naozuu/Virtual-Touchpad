# GW TAU KELEN BAKAL MUAK BACA INI, KARENA GW JUGA MUAK WAKTU NYOBANYA :D

A computer-vision-based virtual touchpad that allows users to control the mouse cursor with hand gestures captured through a webcam. The index finger controls cursor movement, while a pinch gesture between the index finger and thumb performs a mouse click.

> Bahasa Indonesia tersedia pada bagian [Dokumentasi Bahasa Indonesia] dibawah

---

## English Documentation

### Project Description

Virtual Touchpad is a Python application that turns a webcam into a touchless mouse controller. It uses **MediaPipe** to detect and track hand landmarks, **OpenCV** to process and display the camera feed, and **PyAutoGUI** to control the operating system's mouse pointer.

This project is useful as a simple implementation of computer vision, human-computer interaction, and gesture-based input.

### Main Features

- Real-time hand detection through a webcam
- Mouse cursor control using the index fingertip
- Left-click action using a thumb-and-index-finger pinch
- Hand landmark visualization
- Distance indicator between the thumb and index finger
- Mirrored camera preview for more natural control
- PyAutoGUI fail-safe protection
- Press `Q` to close the application

### Technologies

- Python
- OpenCV
- MediaPipe
- PyAutoGUI

### How It Works

1. OpenCV captures video from the default webcam.
2. Each frame is flipped horizontally to create a mirror effect.
3. MediaPipe detects one hand and identifies its landmarks.
4. The index fingertip position is converted from camera coordinates to screen coordinates.
5. PyAutoGUI moves the mouse cursor to the calculated position.
6. The application calculates the distance between the thumb and index fingertip.
7. When the distance is below the click threshold, PyAutoGUI performs a left click.

The current configuration uses:

```python
cam_width, cam_height = 640, 480
click_threshold = 25
```

A smaller `click_threshold` requires the fingers to be closer together. A larger value makes the click gesture easier to trigger.

### Requirements

- Python 3
- A working webcam
- Windows, Linux, or macOS
- Camera permission enabled for Python or the terminal

### Installation

#### 1. Clone the repository

```bash
git clone https://github.com/USERNAME/virtual-touchpad.git
cd virtual-touchpad
```

Replace `USERNAME` with your GitHub username.

#### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux or macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install the required libraries

```bash
pip install opencv-python mediapipe pyautogui
```

Optional `requirements.txt` content:

```text
opencv-python
mediapipe
pyautogui
```

Install it with:

```bash
pip install -r requirements.txt
```

### Running the Application

Run the original file name:

```bash
python virtual.touchpad.py
```

For a cleaner Python file name, rename it to:

```text
virtual_touchpad.py
```

Then run:

```bash
python virtual_touchpad.py
```

### Controls

| Gesture or key | Action |
|---|---|
| Move the index finger | Move the mouse cursor |
| Pinch the thumb and index finger | Perform a left click |
| Separate the fingers after clicking | Prevent repeated clicks |
| Press `Q` | Close the application |
| Move the cursor to the upper-left screen corner | Trigger the PyAutoGUI fail-safe |

### Project Structure

```text
virtual-touchpad/
├── virtual_touchpad.py
├── README.md
└── requirements.txt
```

### Configuration

#### Change the camera

The default webcam uses index `0`:

```python
cap = cv2.VideoCapture(0)
```

When the camera does not open, try:

```python
cap = cv2.VideoCapture(1)
```

#### Change the click sensitivity

```python
click_threshold = 25
```

Example:

```python
click_threshold = 20  # More precise
click_threshold = 35  # Easier to trigger
```

#### Change detection confidence

```python
min_detection_confidence=0.7
min_tracking_confidence=0.7
```

Lower values may detect hands more easily but can reduce accuracy. Higher values may improve stability but require clearer hand visibility.

### Troubleshooting

#### The camera does not open

- Close applications that are currently using the webcam.
- Allow camera access in the operating system settings.
- Change `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)`.
- Confirm that the webcam works in another application.

#### The cursor is unstable

- Use sufficient lighting.
- Keep the hand clearly visible.
- Avoid a background with colors similar to the hand.
- Keep the hand within the camera frame.
- Add cursor smoothing in a future version.

#### The application clicks repeatedly

The current implementation performs a click whenever the finger distance remains below the threshold. Separate the thumb and index finger immediately after a click.

A future improvement can add a click-lock or debounce mechanism so one pinch produces only one click.

#### The program stops with a fail-safe error

PyAutoGUI's fail-safe is enabled:

```python
pyautogui.FAILSAFE = True
```

Moving the pointer to the upper-left corner stops mouse automation. This is a safety feature.

### Current Limitations

- Only one hand is tracked.
- Only left-click is supported.
- Cursor smoothing is not yet implemented.
- Holding the pinch gesture may produce repeated clicks.
- Scroll, drag, and right-click gestures are not yet available.

### Possible Future Improvements

- Cursor smoothing
- Single-click debounce
- Right-click gesture
- Drag-and-drop gesture
- Two-finger scrolling
- Adjustable active tracking area
- Settings interface
- Gesture calibration
- FPS display
- Multi-monitor support

### Safety

This application can control the system mouse. Keep PyAutoGUI's fail-safe enabled and close the program with `Q` when it is no longer needed.

---

## Dokumentasi Bahasa Indonesia

### Deskripsi Proyek

Virtual Touchpad adalah aplikasi Python yang mengubah webcam menjadi pengendali mouse tanpa sentuhan. Aplikasi ini menggunakan **MediaPipe** untuk mendeteksi dan melacak titik-titik tangan, **OpenCV** untuk memproses serta menampilkan kamera, dan **PyAutoGUI** untuk menggerakkan pointer mouse pada sistem operasi.

Proyek ini cocok digunakan sebagai implementasi sederhana computer vision, interaksi manusia dan komputer, serta sistem input berbasis gestur.

### Fitur Utama

- Mendeteksi tangan secara real-time melalui webcam
- Menggerakkan pointer menggunakan ujung jari telunjuk
- Melakukan klik kiri dengan gestur mencubit jari telunjuk dan ibu jari
- Menampilkan landmark atau titik-titik tangan
- Menampilkan jarak antara ibu jari dan jari telunjuk
- Tampilan kamera dicerminkan agar kontrol terasa alami
- Perlindungan fail-safe dari PyAutoGUI
- Menekan tombol `Q` untuk menutup aplikasi

### Teknologi yang Digunakan

- Python
- OpenCV
- MediaPipe
- PyAutoGUI

### Cara Kerja

1. OpenCV mengambil video dari webcam utama.
2. Setiap frame dibalik secara horizontal sehingga tampil seperti cermin.
3. MediaPipe mendeteksi satu tangan dan membaca posisi landmark tangan.
4. Posisi ujung jari telunjuk diubah dari koordinat kamera menjadi koordinat layar.
5. PyAutoGUI menggerakkan pointer mouse ke posisi tersebut.
6. Program menghitung jarak antara ujung ibu jari dan jari telunjuk.
7. Ketika jaraknya lebih kecil dari batas klik, PyAutoGUI menjalankan klik kiri.

Konfigurasi saat ini:

```python
cam_width, cam_height = 640, 480
click_threshold = 25
```

Nilai `click_threshold` yang lebih kecil membuat kedua jari harus lebih dekat. Nilai yang lebih besar membuat gestur klik lebih mudah terdeteksi.

### Persyaratan

- Python 3
- Webcam yang berfungsi
- Windows, Linux, atau macOS
- Izin akses kamera untuk Python atau terminal

### Instalasi

#### 1. Clone repository

```bash
git clone https://github.com/USERNAME/virtual-touchpad.git
cd virtual-touchpad
```

Ganti `USERNAME` dengan username GitHub milikmu.

#### 2. Membuat virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux atau macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Menginstal library

```bash
pip install opencv-python mediapipe pyautogui
```

Isi opsional untuk file `requirements.txt`:

```text
opencv-python
mediapipe
pyautogui
```

Kemudian instal dengan:

```bash
pip install -r requirements.txt
```

### Menjalankan Aplikasi

Gunakan nama file asli:

```bash
python virtual.touchpad.py
```

Agar penamaan file Python lebih rapi, ubah namanya menjadi:

```text
virtual_touchpad.py
```

Kemudian jalankan:

```bash
python virtual_touchpad.py
```

### Kontrol

| Gestur atau tombol | Fungsi |
|---|---|
| Menggerakkan jari telunjuk | Menggerakkan pointer mouse |
| Mencubit ibu jari dan jari telunjuk | Melakukan klik kiri |
| Memisahkan jari setelah klik | Mencegah klik berulang |
| Menekan `Q` | Menutup aplikasi |
| Mengarahkan pointer ke sudut kiri atas layar | Mengaktifkan fail-safe PyAutoGUI |

### Struktur Proyek

```text
virtual-touchpad/
├── virtual_touchpad.py
├── README.md
└── requirements.txt
```

### Konfigurasi

#### Mengganti kamera

Webcam utama menggunakan indeks `0`:

```python
cap = cv2.VideoCapture(0)
```

Jika kamera tidak terbuka, coba:

```python
cap = cv2.VideoCapture(1)
```

#### Mengatur sensitivitas klik

```python
click_threshold = 25
```

Contoh:

```python
click_threshold = 20  # Lebih presisi
click_threshold = 35  # Lebih mudah terpicu
```

#### Mengatur tingkat kepercayaan deteksi

```python
min_detection_confidence=0.7
min_tracking_confidence=0.7
```

Nilai lebih rendah dapat membuat tangan lebih mudah terdeteksi, tetapi hasilnya mungkin kurang stabil. Nilai lebih tinggi dapat meningkatkan kestabilan, tetapi tangan harus terlihat lebih jelas.

### Mengatasi Masalah

#### Kamera tidak terbuka

- Tutup aplikasi lain yang sedang menggunakan webcam.
- Aktifkan izin kamera pada pengaturan sistem operasi.
- Ubah `cv2.VideoCapture(0)` menjadi `cv2.VideoCapture(1)`.
- Pastikan webcam berfungsi pada aplikasi lain.

#### Pointer bergerak tidak stabil

- Gunakan pencahayaan yang cukup.
- Pastikan tangan terlihat jelas.
- Hindari latar belakang yang warnanya mirip dengan tangan.
- Pastikan tangan tetap berada di dalam frame kamera.
- Tambahkan fitur smoothing pada pengembangan berikutnya.

#### Aplikasi melakukan klik berulang

Implementasi saat ini melakukan klik selama jarak kedua jari tetap berada di bawah batas. Segera pisahkan ibu jari dan jari telunjuk setelah melakukan klik.

Pengembangan berikutnya dapat menambahkan sistem click-lock atau debounce agar satu gestur mencubit hanya menghasilkan satu klik.

#### Program berhenti karena fail-safe

Fail-safe PyAutoGUI diaktifkan:

```python
pyautogui.FAILSAFE = True
```

Menggerakkan pointer ke sudut kiri atas layar akan menghentikan otomatisasi mouse. Ini merupakan fitur keamanan.

### Keterbatasan Saat Ini

- Hanya melacak satu tangan.
- Hanya mendukung klik kiri.
- Belum menggunakan penghalus gerakan pointer.
- Menahan gestur mencubit dapat menghasilkan klik berulang.
- Belum mendukung scroll, drag, dan klik kanan.

### Rencana Pengembangan

- Penghalus gerakan pointer
- Sistem debounce untuk satu kali klik
- Gestur klik kanan
- Gestur drag-and-drop
- Scroll menggunakan dua jari
- Area pelacakan yang dapat diatur
- Antarmuka pengaturan
- Kalibrasi gestur
- Tampilan FPS
- Dukungan multi-monitor

### Keamanan

Aplikasi ini dapat mengendalikan mouse pada sistem operasi. Biarkan fitur fail-safe PyAutoGUI tetap aktif dan tutup program dengan tombol `Q` setelah selesai digunakan.

---

## License

This project is intended for educational and portfolio purposes. You may add the MIT License if you want other people to reuse and modify the project.

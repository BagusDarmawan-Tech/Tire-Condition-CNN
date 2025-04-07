# Deteksi Keausan Ban Motor dengan CNN

Proyek ini menggunakan Convolutional Neural Network (CNN) untuk mendeteksi tingkat keausan ban motor dari gambar.

## Fitur

* Klasifikasi keausan ban motor ke dalam 5 kelas:
    * Layak (0 - 5 bulan)
    * Layak (5 - 12 bulan)
    * Layak (12 - 18 bulan)
    * Rawan (18 - 24 bulan)
    * Tak Layak (lebih dari 24 bulan)
* Antarmuka web sederhana untuk mengunggah gambar dan melihat hasil prediksi.
* Menggunakan model CNN yang telah dilatih sebelumnya (16\_cnn\_model.h5).

## Instalasi

1.  **Clone repositori:**

    ```bash
    git clone [https://new.c.mi.com/rs/miuidownload/detail/device/1900996](https://new.c.mi.com/rs/miuidownload/detail/device/1900996)
    cd [nama folder repositori]
    ```

2.  **Buat virtual environment (opsional tetapi disarankan):**

    ```bash
    python -m venv venv
    venv\Scripts\activate # Windows
    source venv/bin/activate # macOS/Linux
    ```

3.  **Instal kebutuhan:**

    ```bash
    pip install Flask tensorflow numpy pillow
    ```

4.  **Siapkan folder `static/uploads/`:**

    * Pastikan folder ini ada di direktori proyek Anda. Folder ini digunakan untuk menyimpan gambar yang diunggah.

5.  **Letakkan model `16_cnn_model.h5`:**

    * Pastikan file model CNN yang telah dilatih ada di direktori proyek Anda.

6.  **Jalankan aplikasi:**

    ```bash
    python app.py
    ```

    * Buka browser web dan kunjungi `http://127.0.0.1:5000/` untuk mengakses aplikasi.

## Struktur Folder
├── app.py
├── 16_cnn_model.h5
├── static/
│   └── uploads/
├── templates/
│   └── index.html
├── README.md
├── requirements.txt

## Penjelasan File

* `app.py`: Kode aplikasi Flask.
* `16_cnn_model.h5`: Model CNN yang telah dilatih.
* `static/uploads/`: Folder untuk menyimpan gambar yang diunggah.
* `templates/index.html`: File HTML untuk antarmuka web.
* `README.md`: File dokumentasi ini.
* `requirements.txt`: Daftar kebutuhan Python.

## Dataset

Model dilatih menggunakan dataset gambar ban motor dengan berbagai tingkat keausan. Dataset tersebut di anotasi dengan memberikan label pada area ban sesuai tingkat ke ausannya.

## Penggunaan

1.  Buka aplikasi web di browser.
2.  Unggah gambar ban motor.
3.  Lihat hasil prediksi tingkat keausan ban.

## Catatan

* Pastikan semua kebutuhan telah diinstal sebelum menjalankan aplikasi.
* Aplikasi ini hanya untuk tujuan demonstrasi.
* Akurasi prediksi dapat bervariasi tergantung pada kualitas gambar dan variasi dataset pelatihan.

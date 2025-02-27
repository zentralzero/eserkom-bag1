# IA.02 Tugas Praktek Programmer - Bagian 1

Program ini adalah implementasi dari Tugas Praktik Demonstrasi Bagian 1, yang meliputi operasi tampil dan manipulasi data dalam database.

## Deskripsi

Program Bagian 1 terdiri dari 4 operasi utama:
1. Menampilkan data dari tabel basis data
2. Mengubah kolom angka menjadi simbol angka (contoh: "satu" → 1)
3. Melakukan sorting dan menentukan bilangan ganjil/genap
4. Menghapus bilangan ganjil atau genap dari database

## Persyaratan Sistem

- Python 3.6 atau lebih tinggi
- PyMySQL
- python-dotenv

## Instalasi

1. Pastikan Python sudah terpasang di sistem Anda:
   ```bash
   python --version
   ```

2. Instal dependensi yang diperlukan:
   ```bash
   pip install pymysql python-dotenv
   ```

3. Buat database MySQL:
   ```sql
   CREATE DATABASE programmer_test;
   ```

4. Buat file `.env` di direktori utama proyek dengan isi:
   ```
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=password_anda
   DB_NAME=programmer_test
   ```
   
   Sesuaikan nilai-nilai tersebut dengan konfigurasi MySQL Anda.

## Struktur Direktori

```
eserkom-bag1/
├── .env                      # Konfigurasi database
├── main.py                   # Entry point program bagian 1
├── config/
│   ├── __init__.py
│   └── database.py           # Konfigurasi koneksi database
├── models/
│   ├── __init__.py
│   └── angka_model.py        # Model untuk tabel angka
├── views/
│   ├── __init__.py
│   └── table_view.py         # View untuk menampilkan tabel
├── controllers/
│   ├── __init__.py
│   └── angka_controller.py   # Controller untuk operasi angka
└── utils/
    ├── __init__.py
    └── helpers.py            # Fungsi pembantu
```

## Cara Menjalankan

Jalankan program Bagian 1 dengan perintah:
```bash
python main.py
```

Program akan:
1. Menampilkan data awal dari tabel angka
2. Mengubah teks angka menjadi simbol angka (contoh: "satu" menjadi "1")
3. Menampilkan data yang diurutkan beserta keterangan ganjil/genap
4. Menawarkan opsi untuk menghapus bilangan ganjil atau genap

## Detail Implementasi

Program ini menggunakan arsitektur MVC (Model-View-Controller):

- **Model**: `angka_model.py` berinteraksi dengan database
- **View**: `table_view.py` menangani tampilan ke pengguna
- **Controller**: `angka_controller.py` menghubungkan model dan view

Database tabel `angka` memiliki struktur:
```sql
CREATE TABLE angka (
    id INT AUTO_INCREMENT PRIMARY KEY,
    angka VARCHAR(10) NOT NULL
);
```

## Penanganan Error

- Program akan menampilkan pesan error jika gagal terhubung ke database
- Input pengguna yang tidak valid akan ditangani dengan pesan yang sesuai

## Troubleshooting

1. **Error Koneksi Database**:
   - Pastikan server MySQL berjalan
   - Verifikasi kredensial di file `.env`
   - Periksa apakah database `programmer_test` telah dibuat

2. **Import Error**:
   - Pastikan struktur direktori sesuai
   - Periksa file `__init__.py` ada di setiap package

3. **PyMySQL Error**:
   - Coba instal ulang: `pip uninstall pymysql && pip install pymysql`
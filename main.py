#!/usr/bin/env python3
"""
Program utama untuk Bagian 1: Operasi pada tabel angka.

Author: Fazlur Rahman
Date: 25/02/27
"""

from controllers import AngkaController
from config import Database
from views import TableView


def main():
    """Fungsi utama program."""
    controller = AngkaController()
    view = TableView()
    db = Database()

    # Pastikan terhubung ke database
    if not db.connect():
        view.display_message("Gagal terhubung ke database! Program dihentikan.")
        return

    # Setup database dan tabel
    if not controller.setup_database():
        view.display_message("Gagal menyiapkan tabel! Program dihentikan.")
        db.close()
        return

    # Bagian 1-1: Menampilkan data dari tabel angka
    view.display_message("\n===== Bagian 1-1: Menampilkan Data =====")
    controller.display_data()

    # Bagian 1-2: Mengubah teks angka menjadi simbol angka
    view.display_message("\n===== Bagian 1-2: Mengubah Teks Angka Menjadi Simbol =====")
    controller.update_to_numbers()

    # Bagian 1-3: Sorting dan menentukan bilangan ganjil/genap
    view.display_message("\n===== Bagian 1-3: Sorting dan Menentukan Bilangan Ganjil/Genap =====")
    controller.display_sorted_with_odd_even()

    # Bagian 1-4: Menghapus bilangan ganjil atau genap
    view.display_message("\n===== Bagian 1-4: Menghapus Bilangan Ganjil atau Genap =====")
    controller.delete_numbers_by_type()

    # Tutup koneksi database
    db.close()
    view.display_message("\nProgram selesai.")


if __name__ == "__main__":
    main()
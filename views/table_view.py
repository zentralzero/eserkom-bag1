#!/usr/bin/env python3
"""
View untuk menampilkan data dalam bentuk tabel.

Author: Fazlur Rahman
Date: 25/02/27
"""


class TableView:
    """View untuk menampilkan data dalam bentuk tabel."""

    @staticmethod
    def display_header():
        """Menampilkan header tabel."""
        print("+----+----------+")
        print("| id | angka    |")
        print("+----+----------+")

    @staticmethod
    def display_row(id_value, angka_value):
        """
        Menampilkan baris tabel.

        Args:
            id_value: Nilai ID
            angka_value: Nilai angka
        """
        print(f"| {id_value:<2} | {angka_value:<8} |")
        print("+----+----------+")

    def display_table(self, data):
        """
        Menampilkan seluruh tabel.

        Args:
            data: Data yang akan ditampilkan
        """
        self.display_header()

        for row in data:
            self.display_row(row[0], row[1])

    @staticmethod
    def display_message(message):
        """
        Menampilkan pesan.

        Args:
            message: Pesan yang akan ditampilkan
        """
        print(message)

    @staticmethod
    def display_odd_even_header():
        """Menampilkan header tabel dengan kolom keterangan."""
        print("+----+----------+-------------+")
        print("| id | angka    | keterangan  |")
        print("+----+----------+-------------+")

    @staticmethod
    def display_odd_even_row(id_value, angka_value, keterangan):
        """
        Menampilkan baris tabel dengan kolom keterangan.

        Args:
            id_value: Nilai ID
            angka_value: Nilai angka
            keterangan: Keterangan ganjil/genap
        """
        print(f"| {id_value:<2} | {angka_value:<8} | {keterangan:<11} |")
        print("+----+----------+-------------+")

    def display_odd_even_table(self, data, odd_even_func):
        """
        Menampilkan tabel dengan keterangan ganjil/genap.

        Args:
            data: Data yang akan ditampilkan
            odd_even_func: Fungsi untuk menentukan ganjil/genap
        """
        self.display_odd_even_header()

        for row in data:
            id_value = row[0]
            angka_value = row[1]
            keterangan = odd_even_func(angka_value)
            self.display_odd_even_row(id_value, angka_value, keterangan)

    @staticmethod
    def get_delete_choice():
        """
        Mendapatkan pilihan pengguna untuk menghapus bilangan ganjil/genap.

        Returns:
            bool: True untuk menghapus ganjil, False untuk genap, None jika tidak valid
        """
        print("\nPilih jenis bilangan yang akan dihapus:")
        print("1. Bilangan Ganjil")
        print("2. Bilangan Genap")

        choice = input("Masukkan pilihan (1/2): ")

        if choice == "1":
            return True
        elif choice == "2":
            return False
        else:
            print("Pilihan tidak valid!")
            return None
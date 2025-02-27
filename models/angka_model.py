#!/usr/bin/env python3
"""
Model untuk tabel angka menggunakan PyMySQL.

Author: Fazlur Rahman
Date: 25/02/27
"""

from config.database import Database


class AngkaModel:
    """Model untuk mengelola data tabel angka."""

    def __init__(self):
        """Inisialisasi model."""
        self.db = Database()

    def get_all(self):
        """
        Mengambil semua data dari tabel angka.

        Returns:
            list: Data dari tabel angka
        """
        query = "SELECT * FROM angka"
        success, result = self.db.execute_query(query, fetch=True)

        if success:
            return result
        return []

    def update_text_to_number_to_db(self, id_value, angka_value):
        """
        Mengubah nilai teks angka menjadi simbol angka.

        Args:
            id_value (int): ID data yang akan diupdate
            angka_value (str/int): Nilai angka baru

        Returns:
            bool: True jika berhasil, False jika gagal
        """
        query = "UPDATE angka SET angka = %s WHERE id = %s"
        params = (str(angka_value), id_value)
        success, _ = self.db.execute_query(query, params)

        return success

    def get_sorted_data(self):
        """
        Mengambil data yang diurutkan berdasarkan nilai angka.

        Returns:
            list: Data yang telah diurutkan
        """
        query = "SELECT id, angka FROM angka ORDER BY CAST(angka AS SIGNED)"
        success, result = self.db.execute_query(query, fetch=True)

        if success:
            return result
        return []

    def delete_numbers_by_type(self, is_odd):
        """
        Menghapus bilangan ganjil atau genap.

        Args:
            is_odd (bool): True untuk menghapus bilangan ganjil, False untuk genap

        Returns:
            int: Jumlah baris yang dihapus
        """
        condition = "MOD(CAST(angka AS SIGNED), 2) = 1" if is_odd else "MOD(CAST(angka AS SIGNED), 2) = 0"
        query = f"DELETE FROM angka WHERE {condition}"

        success, rowcount = self.db.execute_query(query)

        if success:
            return rowcount
        return 0

    def setup_table(self):
        """
        Membuat dan mengisi tabel angka jika belum ada.

        Returns:
            bool: True jika berhasil, False jika gagal
        """
        # Buat tabel
        create_table_query = """
        CREATE TABLE IF NOT EXISTS angka (
            id INT AUTO_INCREMENT PRIMARY KEY,
            angka VARCHAR(10) NOT NULL
        )
        """
        success, _ = self.db.execute_query(create_table_query)
        if not success:
            return False

        # Periksa apakah tabel sudah ada isinya
        check_query = "SELECT COUNT(*) as count FROM angka"
        success, result = self.db.execute_query(check_query, fetch=True)

        if success and result and result[0]['count'] > 0:
            # Truncate table
            check_query = "TRUNCATE TABLE angka;"
            _, _ = self.db.execute_query(check_query, fetch=True)

        # Isi tabel dengan data awal
        insert_query = """
        INSERT INTO angka (angka) VALUES 
        ('dua'), ('empat'), ('delapan'), ('lima'), ('tujuh'),
        ('satu'), ('tiga'), ('enam'), ('sepuluh'), ('sembilan')
        """
        success, _ = self.db.execute_query(insert_query)

        return success
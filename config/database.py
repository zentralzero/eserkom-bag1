#!/usr/bin/env python3
"""
Modul untuk konfigurasi dan koneksi database menggunakan PyMySQL.

Author: Fazlur Rahman
Date: 25/02/27
"""

import pymysql
from pymysql import Error
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Database:
    """Kelas untuk mengelola koneksi dan operasi database."""

    _instance = None

    def __new__(cls):
        """
        Implementasi Singleton pattern untuk koneksi database.

        Returns:
            Database: Instance singleton dari kelas Database
        """
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._connection = None
        return cls._instance

    def connect(self):
        """
        Membuka koneksi ke database MySQL.

        Returns:
            bool: True jika berhasil terhubung, False jika gagal
        """
        if self._connection is not None and self._connection.open:
            return True

        try:
            self._connection = pymysql.connect(
                host=os.getenv("DB_HOST", "localhost"),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", ""),
                database=os.getenv("DB_NAME", "db_test"),
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )

            if self._connection.open:
                return True

        except Error as e:
            print(f"Error saat menghubungkan ke database: {e}")

        return False

    def get_connection(self):
        """
        Mendapatkan objek koneksi database.

        Returns:
            Connection: Objek koneksi MySQL jika terhubung, None jika tidak
        """
        if not self.connect():
            return None
        return self._connection

    def execute_query(self, query, params=None, fetch=False):
        """
        Menjalankan query SQL.

        Args:
            query (str): Query SQL yang akan dijalankan
            params (tuple, optional): Parameter untuk query. Default None.
            fetch (bool, optional): Apakah akan mengambil hasil query. Default False.

        Returns:
            tuple: (success, result/rowcount) - (bool, data hasil query/jumlah baris yang terpengaruh)
        """
        if not self.connect():
            return False, None

        cursor = None
        try:
            cursor = self._connection.cursor()

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            if fetch:
                result = cursor.fetchall()
                # Konversi dari dict ke tuple untuk konsistensi dengan kode asli
                tuple_result = []
                for row in result:
                    if 'id' in row and 'angka' in row:
                        tuple_result.append((row['id'], row['angka']))
                    else:
                        # Untuk query lain, biarkan dalam format dict
                        tuple_result.append(row)
                return True, tuple_result
            else:
                self._connection.commit()
                return True, cursor.rowcount

        except Error as e:
            print(f"Error saat menjalankan query: {e}")
            return False, None
        finally:
            if cursor:
                cursor.close()

    def close(self):
        """Menutup koneksi database."""
        if self._connection and self._connection.open:
            self._connection.close()
            self._connection = None

    def __del__(self):
        """Destructor untuk menutup koneksi database."""
        self.close()
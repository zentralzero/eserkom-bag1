#!/usr/bin/env python3
"""
Controller untuk operasi tabel angka.

Author: Fazlur Rahman
Date: 25/02/27
"""

from models.angka_model import AngkaModel
from views.table_view import TableView
from utils.helpers import AngkaHelper


class AngkaController:
    """Controller untuk mengelola operasi pada tabel angka."""

    def __init__(self):
        """Inisialisasi controller."""
        self.model = AngkaModel()
        self.view = TableView()
        self.helper = AngkaHelper()

    def setup_database(self):
        """
        Menyiapkan database dan tabel.

        Returns:
            bool: True jika berhasil, False jika gagal
        """
        return self.model.setup_table()

    def display_data(self):
        """Menampilkan data dari tabel angka."""
        data = self.model.get_all()
        self.view.display_table(data)

    def update_to_numbers(self):
        """Mengubah nilai teks angka menjadi simbol angka."""
        data = self.model.get_all()

        for row in data:
            id_value = row[0]
            text_value = row[1]
            number_value = self.helper.convert_text_to_number(text_value)

            self.model.update_text_to_number_to_db(id_value, number_value)

        self.view.display_message("Data berhasil diperbarui!")

        # Tampilkan data yang telah diperbarui
        self.display_data()

    def display_sorted_with_odd_even(self):
        """Menampilkan data yang diurutkan beserta keterangan ganjil/genap."""
        data = self.model.get_sorted_data()
        self.view.display_odd_even_table(data, self.helper.determine_odd_even)

    def delete_numbers_by_type(self):
        """Menghapus bilangan ganjil atau genap berdasarkan pilihan pengguna."""
        choice = self.view.get_delete_choice()

        if choice is None:
            return

        # True untuk ganjil, False untuk genap
        type_str = "ganjil" if choice else "genap"

        affected_rows = self.model.delete_numbers_by_type(choice)
        self.view.display_message(f"Berhasil menghapus {affected_rows} bilangan {type_str}.")

        # Tampilkan data yang tersisa
        self.display_data()
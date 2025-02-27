#!/usr/bin/env python3
"""
Modul helper untuk fungsi-fungsi pembantu.

Author: Fazlur Rahman
Date: 25/02/27
"""


class AngkaHelper:
    """Kelas helper untuk operasi pada angka."""

    def convert_text_to_number(self, text):
        """
        Mengkonversi teks angka menjadi angka.

        Args:
            text (str): String teks angka

        Returns:
            int: Nilai angka
        """
        conversion_dict = {
            'satu': 1,
            'dua': 2,
            'tiga': 3,
            'empat': 4,
            'lima': 5,
            'enam': 6,
            'tujuh': 7,
            'delapan': 8,
            'sembilan': 9,
            'sepuluh': 10
        }

        return conversion_dict.get(str(text).lower(), 0)

    def determine_odd_even(self, number):
        """
        Menentukan apakah angka ganjil atau genap.

        Args:
            number: Nilai angka

        Returns:
            str: 'Ganjil' atau 'Genap'
        """
        try:
            num = int(number)
            return "Ganjil" if num % 2 != 0 else "Genap"
        except ValueError:
            return "Bukan angka"
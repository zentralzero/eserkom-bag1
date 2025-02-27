#!/usr/bin/env python3
"""
Unit test untuk program Bagian 1.

Author: Fazlur Rahman
Date: 25/02/27
"""

import unittest
import sys
import io
from unittest.mock import patch, MagicMock

from models.angka_model import AngkaModel
from views.table_view import TableView
from controllers.angka_controller import AngkaController
from utils.helpers import AngkaHelper
from config.database import Database


class TestAngkaHelper(unittest.TestCase):
    """Test helper AngkaHelper."""

    def setUp(self):
        """Set up test environment."""
        self.helper = AngkaHelper()

    def test_convert_text_to_number(self):
        """Test metode convert_text_to_number."""
        self.assertEqual(self.helper.convert_text_to_number("satu"), 1)
        self.assertEqual(self.helper.convert_text_to_number("dua"), 2)
        self.assertEqual(self.helper.convert_text_to_number("tiga"), 3)
        self.assertEqual(self.helper.convert_text_to_number("empat"), 4)
        self.assertEqual(self.helper.convert_text_to_number("lima"), 5)
        self.assertEqual(self.helper.convert_text_to_number("enam"), 6)
        self.assertEqual(self.helper.convert_text_to_number("tujuh"), 7)
        self.assertEqual(self.helper.convert_text_to_number("delapan"), 8)
        self.assertEqual(self.helper.convert_text_to_number("sembilan"), 9)
        self.assertEqual(self.helper.convert_text_to_number("sepuluh"), 10)
        self.assertEqual(self.helper.convert_text_to_number("invalid"), 0)

    def test_determine_odd_even(self):
        """Test metode determine_odd_even."""
        self.assertEqual(self.helper.determine_odd_even(1), "Ganjil")
        self.assertEqual(self.helper.determine_odd_even(2), "Genap")
        self.assertEqual(self.helper.determine_odd_even(3), "Ganjil")
        self.assertEqual(self.helper.determine_odd_even(4), "Genap")
        self.assertEqual(self.helper.determine_odd_even("1"), "Ganjil")
        self.assertEqual(self.helper.determine_odd_even("2"), "Genap")
        self.assertEqual(self.helper.determine_odd_even("abc"), "Bukan angka")


class TestTableView(unittest.TestCase):
    """Test view TableView."""

    def setUp(self):
        """Set up test environment."""
        self.view = TableView()

        # Simpan stdout asli
        self.original_stdout = sys.stdout
        self.mock_stdout = io.StringIO()
        sys.stdout = self.mock_stdout

    def tearDown(self):
        """Tear down test environment."""
        # Kembalikan stdout asli
        sys.stdout = self.original_stdout

    def test_display_header(self):
        """Test metode display_header."""
        self.view.display_header()
        output = self.mock_stdout.getvalue()

        self.assertIn("+----+----------+", output)
        self.assertIn("| id | angka    |", output)

    def test_display_row(self):
        """Test metode display_row."""
        self.view.display_row(1, "satu")
        output = self.mock_stdout.getvalue()

        self.assertIn("| 1  | satu     |", output)

    def test_display_table(self):
        """Test metode display_table."""
        data = [(1, "satu"), (2, "dua")]
        self.view.display_table(data)
        output = self.mock_stdout.getvalue()

        self.assertIn("| 1  | satu     |", output)
        self.assertIn("| 2  | dua      |", output)

    def test_display_message(self):
        """Test metode display_message."""
        self.view.display_message("Test message")
        self.assertIn("Test message", self.mock_stdout.getvalue())

    def test_display_odd_even_header(self):
        """Test metode display_odd_even_header."""
        self.view.display_odd_even_header()
        output = self.mock_stdout.getvalue()

        self.assertIn("+----+----------+-------------+", output)
        self.assertIn("| id | angka    | keterangan  |", output)

    def test_display_odd_even_row(self):
        """Test metode display_odd_even_row."""
        self.view.display_odd_even_row(1, "1", "Ganjil")
        output = self.mock_stdout.getvalue()

        self.assertIn("| 1  | 1        | Ganjil      |", output)

    @patch('builtins.input', return_value='1')
    def test_get_delete_choice(self, mock_input):
        """Test metode get_delete_choice."""
        choice = self.view.get_delete_choice()
        self.assertTrue(choice)  # True untuk menghapus ganjil


class TestAngkaModelWithMock(unittest.TestCase):
    """Test model AngkaModel dengan mocking database."""

    def setUp(self):
        """Set up test environment."""
        # Mock database
        self.db_mock = MagicMock()

        # Patch constructor Database untuk mengembalikan mock
        self.patcher = patch('models.angka_model.Database')
        self.db_class_mock = self.patcher.start()
        self.db_class_mock.return_value = self.db_mock

        # Inisialisasi model
        self.model = AngkaModel()

    def tearDown(self):
        """Tear down test environment."""
        self.patcher.stop()

    def test_get_all(self):
        """Test metode get_all."""
        expected_data = [(1, "satu"), (2, "dua")]
        self.db_mock.execute_query.return_value = (True, expected_data)

        result = self.model.get_all()

        self.assertEqual(result, expected_data)
        self.db_mock.execute_query.assert_called_once_with("SELECT * FROM angka", fetch=True)

    def test_update_text_to_number(self):
        """Test metode update_text_to_number."""
        self.db_mock.execute_query.return_value = (True, 1)

        result = self.model.update_text_to_number_to_db(1, 1)

        self.assertTrue(result)
        self.db_mock.execute_query.assert_called_once_with("UPDATE angka SET angka = %s WHERE id = %s", ('1', 1))

    def test_get_sorted_data(self):
        """Test metode get_sorted_data."""
        expected_data = [(2, "2"), (1, "1")]
        self.db_mock.execute_query.return_value = (True, expected_data)

        result = self.model.get_sorted_data()

        self.assertEqual(result, expected_data)
        self.db_mock.execute_query.assert_called_once_with("SELECT id, angka FROM angka ORDER BY CAST(angka AS SIGNED)",
                                                           fetch=True)

    def test_delete_numbers_by_type_odd(self):
        """Test metode delete_numbers_by_type untuk bilangan ganjil."""
        self.db_mock.execute_query.return_value = (True, 3)

        result = self.model.delete_numbers_by_type(True)  # True untuk ganjil

        self.assertEqual(result, 3)
        self.db_mock.execute_query.assert_called_once()

    def test_delete_numbers_by_type_even(self):
        """Test metode delete_numbers_by_type untuk bilangan genap."""
        self.db_mock.execute_query.return_value = (True, 2)

        result = self.model.delete_numbers_by_type(False)  # False untuk genap

        self.assertEqual(result, 2)
        self.db_mock.execute_query.assert_called_once()


class TestAngkaControllerWithMock(unittest.TestCase):
    """Test controller AngkaController dengan mocking komponen-komponennya."""

    def setUp(self):
        """Set up test environment."""
        # Mock model, view, dan helper
        self.model_mock = MagicMock()
        self.view_mock = MagicMock()
        self.helper_mock = MagicMock()

        # Patch constructor untuk setiap komponen
        self.model_patcher = patch('controllers.angka_controller.AngkaModel')
        self.view_patcher = patch('controllers.angka_controller.TableView')
        self.helper_patcher = patch('controllers.angka_controller.AngkaHelper')

        self.model_class_mock = self.model_patcher.start()
        self.view_class_mock = self.view_patcher.start()
        self.helper_class_mock = self.helper_patcher.start()

        self.model_class_mock.return_value = self.model_mock
        self.view_class_mock.return_value = self.view_mock
        self.helper_class_mock.return_value = self.helper_mock

        # Inisialisasi controller
        self.controller = AngkaController()

        # Mock metode display_data pada controller
        self.original_display_data = self.controller.display_data
        self.controller.display_data = MagicMock()

    def tearDown(self):
        """Tear down test environment."""
        # Kembalikan metode asli display_data
        self.controller.display_data = self.original_display_data

        self.model_patcher.stop()
        self.view_patcher.stop()
        self.helper_patcher.stop()

    def test_setup_database(self):
        """Test metode setup_database."""
        self.model_mock.setup_table.return_value = True

        result = self.controller.setup_database()

        self.assertTrue(result)
        self.model_mock.setup_table.assert_called_once()

    def test_display_data(self):
        """Test metode display_data."""
        # Kembalikan metode asli untuk pengujian ini
        self.controller.display_data = self.original_display_data

        expected_data = [(1, "satu"), (2, "dua")]
        self.model_mock.get_all.return_value = expected_data

        self.controller.display_data()

        self.model_mock.get_all.assert_called_once()
        self.view_mock.display_table.assert_called_once_with(expected_data)

    def test_update_to_numbers(self):
        """Test metode update_to_numbers."""
        self.model_mock.get_all.return_value = [(1, "satu"), (2, "dua")]
        self.helper_mock.convert_text_to_number.side_effect = [1, 2]

        self.controller.update_to_numbers()

        self.model_mock.get_all.assert_called_once()
        self.assertEqual(self.helper_mock.convert_text_to_number.call_count, 2)
        self.assertEqual(self.model_mock.update_text_to_number_to_db.call_count, 2)
        self.view_mock.display_message.assert_called_once()
        self.controller.display_data.assert_called_once()

    def test_display_sorted_with_odd_even(self):
        """Test metode display_sorted_with_odd_even."""
        expected_data = [(1, "1"), (2, "2")]
        self.model_mock.get_sorted_data.return_value = expected_data

        self.controller.display_sorted_with_odd_even()

        self.model_mock.get_sorted_data.assert_called_once()
        self.view_mock.display_odd_even_table.assert_called_once_with(expected_data,
                                                                      self.helper_mock.determine_odd_even)

    def test_delete_numbers_by_type(self):
        """Test metode delete_numbers_by_type."""
        self.view_mock.get_delete_choice.return_value = True  # True untuk ganjil
        self.model_mock.delete_numbers_by_type.return_value = 3

        self.controller.delete_numbers_by_type()

        self.view_mock.get_delete_choice.assert_called_once()
        self.model_mock.delete_numbers_by_type.assert_called_once_with(True)
        self.view_mock.display_message.assert_called_once()
        self.controller.display_data.assert_called_once()


if __name__ == "__main__":
    unittest.main()
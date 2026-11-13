# import unittest

# def calculate_revenue(quantity, unit_price):
#     return quantity * unit_price


# class TestRevenue(unittest.TestCase):

#     def test_basic_revenue(self):
#         result = calculate_revenue(2, 100)
#         self.assertEqual(result, 200)

#     def test_second_revenue(self):
#         result = calculate_revenue(3, 50)
#         self.assertEqual(result, 150)

#     def test_zero_quantity(self):
#         result = calculate_revenue(0, 100)
#         self.assertEqual(result, 0)


# if __name__ == "__main__":
#     unittest.main()



import unittest

from processor import calculate_revenue, is_valid_row


class TestProcessor(unittest.TestCase):

    def test_basic_revenue(self):
        self.assertEqual(calculate_revenue(2, 100), 200)

    def test_second_revenue(self):
        self.assertEqual(calculate_revenue(3, 50), 150)

    def test_zero_quantity(self):
        self.assertEqual(calculate_revenue(0, 100), 0)

    def test_valid_row(self):
        row = {
            "product": "Keyboard",
            "quantity": "2",
            "unit_price": "100"
        }
        self.assertTrue(is_valid_row(row))

    def test_missing_data(self):
        row = {
            "product": "Keyboard",
            "quantity": "",
            "unit_price": "100"
        }
        self.assertFalse(is_valid_row(row))


if __name__ == "__main__":
    unittest.main()
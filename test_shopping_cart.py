import unittest
from shopping_cart import CalculateTotal, display_total

class TestShoppingCart(unittest.TestCase):
    def test_calculate_total(self):
        cart = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99},
            {'name': 'Item C', 'price': 8.49}
        ]
        expected_total = 10.99 + 5.99 + 8.49
        self.assertAlmostEqual(CalculateTotal(cart), expected_total)

    def test_display_total(self):
        total = 25.47
        with self.assertLogs('shopping_cart', level='INFO') as log:
            display_total(total)
            self.assertIn("Total price: 25.47", log.output[0])

if __name__ == "__main__":
    unittest.main()
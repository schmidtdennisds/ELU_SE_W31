
"""Unit tests for the shopping_cart module."""

import unittest

from shopping_cart import calculate_total, display_total


class TestShoppingCart(unittest.TestCase):
    """Test cases for shopping cart functionality."""

    def test_calculate_total(self):
        """Test the calculation of the total cart price."""
        cart = [
            {"name": "Item A", "price": 10.99},
            {"name": "Item B", "price": 5.99},
            {"name": "Item C", "price": 8.49},
        ]
        expected_total = 10.99 + 5.99 + 8.49
        self.assertAlmostEqual(calculate_total(cart), expected_total)

    def test_display_total(self):
        """Test that the total price is logged correctly."""
        total = 25.47
        with self.assertLogs("shopping_cart", level="INFO") as log:
            display_total(total)
            self.assertIn("Total price: 25.47", log.output[0])


if __name__ == "__main__":
    unittest.main()

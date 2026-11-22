
"""Calculate and log the total price of items in a shopping cart."""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("shopping_cart")


def calculate_total(cart):
    """Calculate the total price of all items in the cart."""
    total = 0
    for item in cart:
        total += item["price"]
    return total


def display_total(total):
    """Log the total price of the shopping cart."""
    logger.info("Total price: %s", total)

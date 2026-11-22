import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('shopping_cart')

def CalculateTotal(cart):
    total = 0
    for item in cart:
        total += item['price']
    return total

def display_total(Total):
    logger.info("Total price: " + str(Total))

from models import Product
from view import OutputView

class Controller:
    def __init__(self):
        pass

    def run(self):
        product = Product()
        product.set(1,"apple",100)
        ov = OutputView()
        ov.set(product)
        ov.output()
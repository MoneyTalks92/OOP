import uuid


class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return f"Product(product_name='{self.product_name}', price={self.price})"

    @staticmethod
    def get_id():
        return uuid.uuid4()[-1]


class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product_name, price):
        if product_name not in self.products:
            new_product = Product(product_name, price)
            self.products.append(new_product)

    def remove_product(self, product_name):
        for product in self.products:
            if product_name in self.products:
                self.products.remove(product)

    def display_products(self):
        for product in self.products:
            print(product)

    def sort_by_price(self, ascending=True):
        if ascending == True:
            return sorted(self.products, key=lambda product: product.price)
        else:
            return sorted(self.products,
                          key=lambda product: product.price,
                          reverse=True)


warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.add_product('USB Cable', 24.9)
warehouse.add_product('Mouse', 49.0)
for product in warehouse.sort_by_price():
    print(product)

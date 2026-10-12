class Product:
    def __init__(self, name, price, quantity):
        self.name: str = name
        self.price: int = price
        self.quantity: int = quantity

    def show(self):
        print(f"Product: {self.name}\nPrice: {str(self.price)} thb\nQuantity: {str(self.quantity)} pcs\nValue: {int(self.price)*int(self.quantity)} thb")

def show_product(product_array):
    if not product_array:
        print("No data")
        return

    highest_value = product_array[0]
    for product in product_array:
        if int(product.price) * int(product.quantity) > int(highest_value.price) * int(highest_value.quantity):
            highest_value = product

    highest_value.show()

def main():
    product_list = []
    file_name: str = "data.txt"

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for lines in file:
                data = lines.strip().split(", ")

                if len(data) == 3:
                    name, price, quantity = data
                    product = Product(name, price, quantity)
                    product_list.append(product)
    except:
        print("File not found.")

    print("----Highest Product Value----")
    show_product(product_list)


if __name__ == "__main__":
    main()
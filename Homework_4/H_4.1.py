class Product:
    """Класс, представляющий товар в магазине."""
    def __init__(self, name: str, category: str, price: float, stock: int):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def update_price(self, new_price: float):
        """Метод для изменения цены товара."""
        if new_price >= 0:
            self.price = new_price
        else:
            print("Цена не может быть отрицательной!")

    def update_stock(self, quantity: int):
        """Метод для изменения количества товара на складе."""
        if self.stock + quantity >= 0:
            self.stock += quantity
        else:
            print(f"Ошибка: Недостаточно товара '{self.name}' на складе.")

    def __str__(self):
        return f"Товар: {self.name} ({self.category}) | Цена: {self.price} грн | На складе: {self.stock} шт."


class Order:
    """Класс, представляющий заказ."""
    def __init__(self):
        self.products = []
        self.total_amount = 0.0

    def add_product(self, product: Product, quantity: int = 1):
        """Метод для добавления товара в заказ с учетом проверки склада."""
        if product.stock >= quantity:
            product.update_stock(-quantity)
            self.products.append({"product": product, "quantity": quantity})
            self.calculate_total()
            print(f"Добавлено в заказ: {product.name} x {quantity} шт.")
        else:
            print(f"Невозможно добавить товар '{product.name}': недостаточно на складе.")

    def calculate_total(self):
        """Метод для вычисления общей суммы заказа."""
        self.total_amount = sum(item["product"].price * item["quantity"] for item in self.products)
        return self.total_amount

    def __str__(self):
        items_str = ", ".join([f"{item['product'].name} ({item['quantity']} шт.)" for item in self.products])
        return f"Заказ [Товары: {items_str}] | Общая сумма: {self.total_amount} грн"


class Customer:
    """Класс, представляющий клиента магазина."""
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.orders = []

    def add_order(self, order: Order):
        """Метод для добавления нового заказа клиенту."""
        self.orders.append(order)
        print(f"Клиент {self.name} успешно оформил новый заказ.")

    def __str__(self):
        return f"Клиент: {self.name} ({self.email}) | Количество заказов: {len(self.orders)}"


# ==========================================
# Демонстрация работы системы (Задание 2)
# ==========================================
if __name__ == "__main__":
    print("--- 1. Создание товаров ---")
    p1 = Product(name="Плюшевый мишка", category="м'яка іграшка", price=350.0, stock=10)
    p2 = Product(name="Конструктор LEGO", category="конструктор", price=1200.0, stock=5)
    print(p1)
    print(p2)

    print("\n--- 2. Создание клиента ---")
    customer = Customer(name="Иван Иванов", email="ivan@example.com")
    print(customer)

    print("\n--- 3. Создание заказа и добавление товаров ---")
    order1 = Order()
    order1.add_product(p1, quantity=2)
    order1.add_product(p2, quantity=1)

    print("\n--- 4. Привязка заказа к клиенту ---")
    customer.add_order(order1)

    print("\n--- 5. Проверка изменения состояния после заказа ---")
    print(p1)
    print(p2)
    print(order1)
    print(customer)
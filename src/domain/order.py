class Order:
    """Represents a single order line for a menu item.

    Validations:
    - `menu_name` must be a non-empty string.
    - `quantity` must be a positive integer (> 0).
    - `price` must be a non-negative integer (>= 0).
    """

    def __init__(self, menu_name: str, quantity: int, price: int):
        if not isinstance(menu_name, str) or not menu_name.strip():
            raise ValueError("menu_name must be a non-empty string")

        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("quantity must be a positive integer")

        if not isinstance(price, int) or price < 0:
            raise ValueError("price must be a non-negative integer")

        self.menu_name = menu_name
        self.quantity = quantity
        self.price = price

    def subtotal(self) -> int:
        """Return the subtotal for this order (quantity * price)."""
        return self.quantity * self.price
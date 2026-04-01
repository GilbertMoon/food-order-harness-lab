from typing import List

from src.domain.order import Order


class OrderService:
    """Service for creating and querying orders."""

    def __init__(self):
        self.orders: List[Order] = []

    def create_order(self, menu_name: str, quantity: int, price: int) -> Order:
        """Create an Order (validated by `Order`) and store it.

        Raises ValueError if the provided values are invalid.
        Returns the created `Order` instance.
        """
        order = Order(menu_name, quantity, price)
        self.orders.append(order)
        return order

    def list_orders(self) -> List[Order]:
        """Return a shallow copy of stored orders."""
        return list(self.orders)

    def calculate_total(self) -> int:
        """Return the sum of all order subtotals."""
        return sum(o.subtotal() for o in self.orders)
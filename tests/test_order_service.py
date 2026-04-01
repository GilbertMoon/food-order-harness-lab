from src.service.order_service import OrderService


def test_create_order():
    service = OrderService()
    order = service.create_order("김밥", 2, 4000)

    assert order.menu_name == "김밥"
    assert order.quantity == 2
    assert order.price == 4000


def test_calculate_total():
    service = OrderService()
    service.create_order("김밥", 2, 4000)
    service.create_order("라면", 1, 5000)

    assert service.calculate_total() == 13000
from src.service.order_service import OrderService


def main() -> None:
	svc = OrderService()

	# Add two orders
	svc.create_order("Bibimbap", 2, 9000)
	svc.create_order("Kimchi Stew", 1, 7500)

	# Print all orders
	print("Orders:")
	for o in svc.list_orders():
		print(f"- {o.menu_name}: quantity={o.quantity}, price={o.price}, subtotal={o.subtotal()}")

	# Print total price
	total = svc.calculate_total()
	print(f"Total price: {total}")


if __name__ == "__main__":
	main()
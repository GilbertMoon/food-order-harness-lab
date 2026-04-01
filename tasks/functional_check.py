import os
import sys
from pathlib import Path

# ensure repository root is on sys.path so `src` package can be imported
repo_root = str(Path(__file__).resolve().parents[1])
sys.path.insert(0, repo_root)

from src.service.order_service import OrderService


def run_checks():
    svc = OrderService()
    svc.create_order("Bibimbap", 2, 9000)
    svc.create_order("Kimchi Stew", 1, 7500)

    orders = svc.list_orders()
    assert len(orders) == 2
    assert orders[0].menu_name == "Bibimbap"
    assert orders[1].menu_name == "Kimchi Stew"

    total = svc.calculate_total()
    assert total == 2 * 9000 + 1 * 7500

    # validation checks
    try:
        svc.create_order("", 1, 100)
        raise SystemExit("Validation failed: empty menu_name allowed")
    except ValueError:
        pass

    try:
        svc.create_order("A", 0, 100)
        raise SystemExit("Validation failed: quantity <= 0 allowed")
    except ValueError:
        pass

    try:
        svc.create_order("A", 1, -1)
        raise SystemExit("Validation failed: negative price allowed")
    except ValueError:
        pass

    print("FUNCTIONAL_CHECK: OK")


if __name__ == "__main__":
    run_checks()

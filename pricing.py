def calculate_discount(price: float, discount_percent: float) -> float:
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount must be between 0 and 100")
    return round(price * (1 - discount_percent / 100), 2)


def format_currency(amount: float, currency: str = "USD") -> str:
    return f"{currency} {amount:,.2f}"

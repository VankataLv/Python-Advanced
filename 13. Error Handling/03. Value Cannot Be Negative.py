class ValueCannotBeNegative(Exception):
    """Number is negative"""
    pass


amount = ""
for _ in range(5):
    amount = float(input())
    if amount <= 0:
        raise ValueCannotBeNegative("Number cannot be negative")

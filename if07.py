def main(a):
    if a>0 and a%2==1:
        return "positive odd number"
    elif a>0 and a%2==0:
        return "positive even number"
    elif a<0 and a%2==1:
        return "negative odd number"
    elif a<0 and a%2==0:
        return "negateve even number"
    elif a==0:
        return "the number is zero"
print(main(-8))
"""
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
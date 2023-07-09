def main(a):
    if a%2==1 and a//100==0 and not a//10==0 and not a//1==0:
        return "two-digit odd number"
    elif a%2==0 and a//100==0 and not a//10==0 and not a//1==0:
        return "two-digit even number"
    elif a%2==1 and a//1000==0 and not a//100==0 and not a//10==0 and not a//1==0:
        return "three-digit odd number"
    elif a%2==0 and  a//000==0 and not a//100==0 and not a//10==0 and not a//1==0:
        return "three-digit even number"
print(main(999))
"""
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
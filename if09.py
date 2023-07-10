def main(a):
    c=a%10
    b=a//10
    d=c*10+b
    if a>=d:
        return True
    return False
print(main(55))
"""
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
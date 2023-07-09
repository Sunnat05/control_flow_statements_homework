def main(a):
    a=int(input())
    if a>0:
        print(a+1)
    else: print(a)
    """
    If the number is positive, increase it to 1, else leave unchanged.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else unchanged.
    """
    return a
print(main(4))
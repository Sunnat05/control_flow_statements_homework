def main(a,b,c):
    s=0
    if a>0:
        s+=1
    if b>0:
        s+=1
    if c>0:
        s+=1
    return s
print(main(2,-4,9))
"""
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
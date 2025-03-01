def main(temp):
    if temp<0:
        return "Freezing"
    elif 1<=temp<=10:
        return "Very Cold"
    elif 11<=temp<=20:
        return "Cold"
    elif 21<=temp<=30:
        return "Normal"
    elif 31<=temp<=40:
        return "Hot"
    elif temp>40:
        return "Very Hot"
print(main(42))
"""
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
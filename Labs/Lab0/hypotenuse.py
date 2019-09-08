import math


def calculate_hypotenuse(a, b):
    """
    Return the hypotenuse of two arguments.
    :param a: first user input
    :param b: second user input
    :return: √(a ∗ ∗2 + b ∗ ∗2)
    """
    return math.sqrt(a**2 + b**2)


def main():
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    print(calculate_hypotenuse(num1, num2))


if __name__ == "__main__":
    main()


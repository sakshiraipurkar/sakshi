def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    Parameters:
    n (int): The number for which to calculate the factorial.

    Returns:
    int: The factorial of the number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = 5
print(f"The factorial of {number} is {factorial(number)}")

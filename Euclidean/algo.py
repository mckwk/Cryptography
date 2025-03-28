def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_multiple(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result


if __name__ == "__main__":
    # Example usage for two integers
    num1 = 56
    num2 = 98
    print(f"GCD of {num1} and {num2}: {gcd(num1, num2)}")

    # Example usage for multiple integers
    numbers = [56, 98, 42, 84]
    print(f"GCD of {numbers}: {gcd_multiple(numbers)}")
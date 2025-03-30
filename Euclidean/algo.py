def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_multiple(numbers):
    result = numbers[0] # start with the first number in the list
    for num in numbers[1:]:
        result = gcd(result, num) # compute for the current result and the next number
    return result


if __name__ == "__main__":
    # two integers
    num1 = 56
    num2 = 98
    print(f"GCD of {num1} and {num2}: {gcd(num1, num2)}")

    # multiple integers
    numbers = [56, 98, 42, 84]
    print(f"GCD of {numbers}: {gcd_multiple(numbers)}")
    # have a nice day :)
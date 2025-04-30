def classify_even_odd(numbers):
    return {
        'even': [n for n in numbers if n % 2 == 0],
        'odd': [n for n in numbers if n % 2 != 0]
    }

print("Classify even/odd:", classify_even_odd([1, 2, 3, 4, 5, 6]))


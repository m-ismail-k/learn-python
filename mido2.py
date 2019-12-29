numbers = [1, 2, 7, 9, 10, 20, 4324, 54, 3]


def even_numbers(data):
    return [number if number % 2 == 0 else None for number in data]


cift = even_numbers(numbers)
print(cift)

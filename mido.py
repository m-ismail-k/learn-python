numbers = [1, 2, 7, 9, 10, 20, 4324, 54, 3]


def even_numbers(data):
    even = []
    for number in data:
        if number % 2 == 0:
            even.append(number)
    return even


cift = even_numbers(numbers)
print(cift)

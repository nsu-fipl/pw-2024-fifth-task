def fizzbuzz(start, end):
    result = []
    for i in range(start, end):
        if i % 3 == 0:
            result.append('Fizz')
        if i % 5 == 0:
            result.append('Buzz')
        elif i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        else:
            result.append(str(i))
    return result


if __name__ == '__main__':
    print(fizzbuzz(1, 16))
import fizzbuzz as fb

def test_start_bigger_than_end():
    assert fb.fizzbuzz(4, 1) == []

def test_three_divisor():
    assert fb.fizzbuzz(3, 4) == ['Fizz']

def test_five_divisor():
    assert fb.fizzbuzz(5, 6) == ['Buzz']

def test_three_and_five_divisor():
    assert fb.fizzbuzz(15, 16) == ['FizzBuzz']

def test_ordinary_number():
    assert fb.fizzbuzz(2, 3) == ['2']

def test_all_fizzbuzz():
    assert fb.fizzbuzz(10, 16) == ['Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
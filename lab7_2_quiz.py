# Napisz generator perfect_numbers() bez żadnych argumentów,
# który generuje kolejne liczby doskonałe. Liczba doskonała to taka,
# która jest równa sumie wszystkich swoich dzielników właściwych
# (tj. wszystkich dzielników oprócz samej siebie).
# Na przykład, 6 jest liczbą doskonałą (1 + 2 + 3 = 6).

def perfect_numbers():
    """Generator function for perfect numbers."""
    num = 1
    while True:
        if is_perfect(num):
            yield num
        num += 1

def is_perfect(number):
    """Check if a number is perfect."""
    return sum(divisor for divisor in range(1, number) if number % divisor == 0) == number

# Testing the generator function
gen = perfect_numbers()
perfects = [next(gen) for _ in range(3)]
print(perfects == [6, 28, 496])

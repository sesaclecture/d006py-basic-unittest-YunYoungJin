def is_even_or_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
def calc_mean(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    return None

def find_max(numbers):
    if numbers:
        return max(numbers)
    return None
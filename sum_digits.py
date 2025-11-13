def sum_digits(n):
    # Base case
    if len(str(n)) == 1 or n == 0:
        print(n)
        return n 
    
    digits = [int(d) for d in str(n)]
    print(digits)
    print(sum(digits))
    
    return sum_digits(sum(digits))

print(sum_digits(123456789))

def fibonachi(n):
    if n <= 1:
        return n
    else:
        a = fibonachi(n-1) + fibonachi(n-2)
        # print(a)
        return a

print(fibonachi(10)) 

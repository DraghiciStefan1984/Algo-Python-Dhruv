
def reverse(s):
    if len(s)<=1:
        return s
    else:
        return s[len(s)-1]+reverse(s[1:len(s)-1])

def fibonacci(i):
    if i<=2:
        return 1
    return fibonacci(i-1)+fibonacci(i-2)
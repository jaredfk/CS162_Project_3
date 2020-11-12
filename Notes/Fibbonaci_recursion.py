'''Fibbonaci recursion'''

'''
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
Start with 0 and 1 (at index 0 and 1 respectively).
Then for any element fibo(k), we find it by adding fibo(k-1) + fibo(k-2)

Leads to lots of extra calcualtions if not stored, an advanced technique for later.

fibo(6) = f(5) + f(4)
f(5) = f(4) + f(3)
f(4) = f(3) + f(2)
f(3) = f(2) + f(1)
f(2) = f(1) + f(0)
f(1) = 1
f(0) = 0
'''

def fibo(current_value: int) -> int:
    '''Calculate fibo of current value and return that value, or return -1 if there is an error'''
    if current_value == 0:
        return 0
    elif current_value == 1:
        return 1
    elif current_value < 0:
        return -1

    #else all integers greater than 1, so it will calculate
    #f(6) = f(5) + f(4): this is specific, lets make it generic
    return fibo(current_value - 1) + fibo(current_value - 2)

def main():
    for number in range(6):
        print(fibo(number))

if __name__ == '__main__':
    #main()
    print(fibo(10))
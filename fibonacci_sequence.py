"""
This script will take an input number n and generates
the Fibonacci sequence up to that number
"""

n = int(input("Give me a number..."))

def fibonacci_sequence(p):
    fibo_seq = [0]
    for i in range(p):
        if len(fibo_seq) == 1:
            fibo_seq.append(1)
        else:
            fibo_seq.append(fibo_seq[i] + fibo_seq[i-1])
    return fibo_seq

def main():
    print(fibonacci_sequence(n))

if __name__ == '__main__':
    main()

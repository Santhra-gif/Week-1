def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

def main():
    print("Welcome to the Fibonacci Sequence Generator!")
    n = int(input("Enter the number of terms you want in the Fibonacci sequence: "))
    print(f"Fibonacci Sequence up to {n} terms:")
    fibonacci(n)

if __name__ == "__main__":
    main()

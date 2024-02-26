# Recursion Two - Branch
# Fibonacci Number: F(n) = F(n - 1) + F(n - 2)  f(0) = 0, F(1) = 1

int fib(int n){
    if (n <= 1){
        return n
    }
    return fib(n - 1) + fib(n - 2)
}
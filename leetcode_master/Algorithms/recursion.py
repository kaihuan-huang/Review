# One-Branch Recursion
int factorial(int n){
    if (n <= 1){
        return 1
    }
    return n * factorial(n - 1)
}

# None Recursion solutions:
int res = 1
while n > 1{
    res = res * n
    n -= 1   
}
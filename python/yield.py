def factorial_r(n):
    if n==1:
        return 1
    return n * factorial_r(n-1)


if __name__=="__main__":
    print(factorial_r(5))

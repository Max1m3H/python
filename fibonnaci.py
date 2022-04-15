def fibonnaci(n: float) -> float:
    if n<=1:
        return n
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)


def fibo(n: float, a=0) -> float:
    if n<=1:
        return n + a
    else:
        return fibo(n-1) + fibo(n-2)

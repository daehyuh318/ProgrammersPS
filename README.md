# ProgrammersPS
ProgrammersPS

약수와 소수의 차이

약수

```python
def get_divisor(n):
    data = []

    for i in range(1, n // 2 + 1): # sqrt
        if n % i == 0:
            data.append(i)
    data.append(n)
    return data

print(get_divisor(8))
```

소수

```python
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
```

def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

a = int(input('Saisissez un nombre : '))

while a != 0:
    if est_premier(a):
        print(a, "est un nombre premier")
    a -= 1

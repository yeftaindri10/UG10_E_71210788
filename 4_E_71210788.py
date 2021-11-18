a = int(input("Masukkan bilangan 1 : "))
b = int(input("Masukkan bilangan 2 : "))
c = int(input("Masukkan bilangan 3 : "))

if a > b and a > c and b > c:
    print('\nUrutan bilangan yang terkecil adalah', c, b, a)
elif a > b and a > c and b < c:
    print('\nUrutan bilangan yang terkecil adalah', b, c, a)
elif b > a and b > c and a > c:
    print('\nUrutan bilangan yang terkecil adalah', c, a, b)
elif b > a and b > c and a < c:
    print('\nUrutan bilangan yang terkecil adalah', a, c, b)
elif c > a and c > b and b > a:
    print('\nUrutan bilangan yang terkecil adalah', a, b, c)
else:
    print('\nUrutan bilangan yang terkecil adalah', b, a, c)
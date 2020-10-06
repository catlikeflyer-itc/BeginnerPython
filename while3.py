n = int(input("Edad del niño/niña: "))
dinero = 10

while dinero <= 1000:
    dinero *= 2
    n += 1

print(f"Tendra {n} años cuando exceda $1000, y recibira ${dinero}")

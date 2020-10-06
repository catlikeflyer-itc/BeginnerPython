def count_a(string):
    counter = 0

    for letter in string.lower():

        if letter == "a":
            counter += 1

    return counter

print(count_a(input("Escriba string con A: ")))

# Alternativa print(input("string: ").count('a'))
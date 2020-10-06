# Version con iteracion
num = input(">>>")
suma = 0

for i in num:
    if i == "-":
        suma += 0
    else:
        suma += int(i)

print(suma)

#%%
# Version mas corta
num = input()

if num.startswith('-'):
    print(sum(map(int, num[1:])))
    
else:
    print(sum(map(int, num)))


# %%

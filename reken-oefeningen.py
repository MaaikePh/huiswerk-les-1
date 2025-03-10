### Laat python 2 getallen optellen en het resultaat printen
#  5 + 3 = 8

print(5+3) #resultaat is: 8

### Laat python 2 getallen vermenigvuldigen en het resultaat printen
#  3 * 4 = 12

print(3*4) #resultaat is: 12

### Geef nu het resultaat weer in een string. Waar de getallen en het resultaat in staan.

getal1 = 3
getal2 = 4
product = getal1 * getal2

print(f'De uitkomst van {getal1} keer {getal2} is {product}.')
#resultaat is: De uitkomst van 3 keer 4 is 12.

### Laat python de wortel van een getal berekenen en het resultaat printen
# De wortel van 16 is 4
# Tip gebruik ** om de wortel te berekenen

print(int(16**0.5)) #resultaat is: 4

### Laat python de rest van een deling berekenen en het resultaat printen
#  De rest van 10 / 3 is 1

print(10%3) #resultaat is: 1

### Maak een calculator die 2 getallen optelt, aftrekt, vermenigvuldigd en deelt
# Gebruik hiervoor input om de getallen te vragen
# Voer getal 1 in: 5
# Voer getal 2 in: 3
# 5 + 3 = 8
# 5 - 3 = 2
# 5 * 3 = 15
# 5 / 3 = 1.6666666666666667

getal1 = int(input("Voer getal 1 in: "))
getal2 = int(input("Voer getal 2 in: "))
optelsom = getal1 + getal2
aftreksom = getal1 - getal2
product = getal1 * getal2
deling = getal1 / getal2

print(f'Als je de getallen optelt krijg je {optelsom}, als je de getallen van elkaar aftrekt krijg je {aftreksom}, '
      f'als je de getallen vermenigvuldigd krijg je {product} en als je de getallen door elkaar deelt krijg je {deling}.')
#resultaat is: Als je de getallen optelt krijg je 8, als je de getallen van elkaar aftrekt krijg je 2, als je de getallen vermenigvuldigd krijg je 15 en als je de getallen door elkaar deelt krijg je 1.6666666666666667.

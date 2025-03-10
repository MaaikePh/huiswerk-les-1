# geef 2 getallen op en kijk of ze gelijk zijn
# 5 en 5 zijn gelijk
# 5 en 3 zijn niet gelijk

getal1 = 5
getal2 = 3

print(getal1 == getal1) #resultaat is True
print(getal1 != getal2) #resultaat is True

# geef 2 getallen op en kijk of getal1 groter is dan getal2
# 5 is groter dan 3
# 3 is niet groter dan 5

getal1 = 5
getal2 = 3
is_groter = "groter" if getal1 > getal2 else "lager"
niet_groter = "niet groter" if getal2 < getal1 else "groter"
print(f"{getal1} is {is_groter} dan {getal2}.")
#resultaat is: 5 is groter dan 3.
print(f"{getal2} is {niet_groter} dan {getal1}.")
#resultaat is: 3 is niet groter dan 5.

# geef 2 getallen op en kijk of getal1 kleiner is dan getal2 of gelijk aan getal2
# 5 is kleiner dan 3
# 3 is kleiner dan 5
# 5 is niet kleiner dan 5

getal1 = 5
getal2 = 3
print(getal1 <= getal2) #resultaat is: False
print(getal2 <= getal1) #resultaat is: True
print(getal1 <= getal1) #resultaat is: True

# Kijk of een string gelijk is aan een andere string
# John is gelijk aan John
# John is niet gelijk aan Doeg

naam = "John"
print(naam == naam) #True
naam2 = "Doeg"
print(naam == naam2) #False
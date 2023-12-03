n = int(input("Bitte die Höhe der Pyramide eingeben: "))

for i in range(0, n):
    indentation = (n - i - 1) * " "
    stars = "*" * (2 * i + 1)
    print(indentation + stars)

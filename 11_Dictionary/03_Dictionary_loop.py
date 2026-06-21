car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'color': 'Red',
    'year': 1974
}

# print(car)

# for x in car:
#     print(x)


# Return only values
for y in car.values():
    print(y)


# Return only keys
for z in car.keys():
    print(z)


# Return both key:value in pair = items()
for a, b in car.items():
    print(f"{a}: {b}")
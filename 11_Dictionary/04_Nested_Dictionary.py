child1 = {
    'name': 'Emil',
    'year': 2004
}

child2 = {
    'name': 'Tobias',
    'year': 2007
}

child3 = {
    'name': 'Linus',
    'year': 2011
}

family = {
    'child1': child1,
    'child2': child2,
    'child3': child3
}

print(family['child1'])
print(family['child1']['name'])


for x, y in family.items():
    print(f"{x}: {y}")


for a, b in family.items():
    print(a)

    # for c in b:
    #     print(c+ ':', b[c])

    for d in b:
        print(d)
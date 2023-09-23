def age_assignment(*names, **ages):
    db = {}
    for name in names:
        first_let = name[0]
        age = ages[first_let]
        db[name] = age

    db = sorted(db.items(), key=lambda x: x[0])
    return "\n".join([f"{n} is {a} years old." for n, a in db])

# print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
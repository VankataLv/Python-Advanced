def start_spring(**kwargs):
    db = {}
    for key, value in kwargs.items():
        if value not in db:
            db[value] = []
        db[value].append(key)
    db = dict(sorted(db.items(), key=lambda x: (-len(x[1]), x[0])))
    sorted_d = {}
    for key, value in db.items():
        value = sorted(value)
        sorted_d[key] = value
    result = ""
    for key, value in sorted_d.items():
        result += f"{key}:\n"
        for el in value:
            result += f"-{el}\n"
    return result


# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower", }
# print(start_spring(**example_objects))

# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))

# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))
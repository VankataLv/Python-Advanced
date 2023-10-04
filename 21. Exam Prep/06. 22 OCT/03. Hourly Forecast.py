def forecast(*args):
    weather_db = {"Sunny": [],
                  "Cloudy": [],
                  "Rainy": []}
    for el in args:
        weather_db[el[1]].append(el[0])
    weather_to_pop =[]
    for k, v in weather_db.items():
        if len(v) == 0:
            weather_to_pop.append(k)
    for weather in weather_to_pop:
        weather_db.pop(weather)
    result = ""
    for k, v in weather_db.items():
        v.sort()
        for city in v:
            result += f"{city} - {k}\n"
    return result

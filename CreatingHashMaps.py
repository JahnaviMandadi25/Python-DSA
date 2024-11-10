from collections import defaultdict

colour_name = defaultdict(list)

colours = ["white", "black", "red", "green", "yellow", "blue", "magenta", "cyan"]
flowers = ["Rose", "lilly", "lotus", "sunflower", "Jasmine"]
cars = ["mini", "tesla", "bmw", "toyota"]

colour_name["DiffNames"] += colours
colour_name["DiffFlowers"] += flowers
colour_name["Diffcars"] += cars

for keys in colour_name.keys():
    print(keys)


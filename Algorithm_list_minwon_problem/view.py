buildings = [0, 0, 3, 5, 2, 4, 9, 0, 6, 4, 0, 6, 0, 0]
result = 0
view_building = 0
for i in range(2, len(buildings) - 2):
    if buildings[i] > buildings[i - 1] and buildings[i] > buildings[i - 2] and buildings[i] > buildings[i + 1] and \
            buildings[i] > buildings[i + 2]:
        max_building = max(buildings[i - 1], buildings[i - 2], buildings[i + 1], buildings[i + 2])
        view_building = buildings[i] - max_building
        result += view_building

print(result)
weight = int(input())
height = int(input())
weight_kg = 0.453592 * weight
height_m = 0.025 * height
height_m2 = height_m * height_m
body_mass_index = weight_kg / height_m2
print('{0:.2f}'.format(body_mass_index))
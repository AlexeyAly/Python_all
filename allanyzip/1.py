countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]


for i in range(len(countries)):
    print(f"{list(zip(capitals, countries, population))[i][0]}is the capital of {list(zip(capitals, countries, population))[i][1]}, population equal {list(zip(capitals, countries, population))[i][2]} people.")

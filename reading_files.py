# country_file = open("countries.txt", "r")
# print(country_file.readlines())
# country_file.close()

country_file = open("countries.txt", "r")
for line in country_file:
    print(line)
country_file.close()
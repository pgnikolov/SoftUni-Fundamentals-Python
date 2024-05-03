# Using dictionary comprehension, write a program that receives country names on the first line,
# separated by comma and space ", ", and their corresponding capital cities on the second line
# (again separated by comma and space ", "). Print each country with its capital on a separate
# line in the following format: "{country} -> {capital}".

countries = [con for con in input().split(", ")]
capitals = [cap for cap in input().split(", ")]

cc_dict = dict(zip(countries, capitals))

# for k, v in cc_dict.items():
#     print(f"{k} -> {v}")
[print(f"{k} -> {cc_dict[k]}") for k in cc_dict]

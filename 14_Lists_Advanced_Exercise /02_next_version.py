# You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}".
# Your task is to print the next version. For example, if the current version
# is "1.3.4", the next version will be "1.3.5".
# The only rule is that the numbers cannot be greater than 9. If it happens, set the current number
# to 0 and increase the previous number. For more clarification, see the examples below.

cur_version = input().split(".")
cur_version_int = int("".join(cur_version))
next_version_int = cur_version_int + 1
next_version_list = list(str(next_version_int))
next_version_str = ".".join(next_version_list)

print(next_version_str)

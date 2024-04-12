fire_cells = input().split("#")
water = int(input())

total_effort = 0
total_fire = 0
cells_done = []

for i in range(len(fire_cells)):
    single_fire = fire_cells[i].split(" = ")
    if single_fire[0] == "High" and 81 <= int(single_fire[1]) <= 125:
        if water >= int(single_fire[1]):
            water -= int(single_fire[1])
            total_fire += int(single_fire[1])
            total_effort += int(single_fire[1]) * 0.25
            cells_done.append((single_fire[1]))
        else:
            pass
    elif single_fire[0] == "Medium" and 51 <= int(single_fire[1]) <= 80:
        if water >= int(single_fire[1]):
            water -= int(single_fire[1])
            total_fire += int(single_fire[1])
            total_effort += int(single_fire[1]) * 0.25
            cells_done.append((single_fire[1]))
        else:
            pass
    elif single_fire[0] == "Low" and 1 <= int(single_fire[1]) <= 50:
        if water >= int(single_fire[1]):
            water -= int(single_fire[1])
            total_fire += int(single_fire[1])
            total_effort += int(single_fire[1]) * 0.25
            cells_done.append((single_fire[1]))
        else:
            pass


print("Cells:")
for cell in cells_done:
    print(f" - {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")

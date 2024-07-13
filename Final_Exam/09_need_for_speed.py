n = int(input())
cars = {}

for _ in range(n):
    car_info = input().split('|')
    cars[car_info[0]] = {'mileage': int(car_info[1]), 'fuel': int(car_info[2])}

while True:
    command = input()
    if command == 'Stop':
        break
    info = command.split(' : ')
    if info[0] == 'Drive':
        car, distance, needed_fuel = info[1], int(info[2]), int(info[3])
        if needed_fuel > cars[car]['fuel']:
            print('Not enough fuel to make that ride')
        else:
            cars[car]['fuel'] -= needed_fuel
            cars[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
            if cars[car]['mileage'] >= 100000:
                print(f"Time to sell the {car}!")
                cars.pop(car)
    elif info[0] == 'Refuel':
        car, fuel_to_fill = info[1], int(info[2])
        if cars[car]['fuel'] + fuel_to_fill > 75:
            print(f"{car} refueled with {abs(cars[car]['fuel'] - 75)} liters")
            cars[car]['fuel'] = 75
        else:
            cars[car]['fuel'] += fuel_to_fill
            print(f"{car} refueled with {fuel_to_fill} liters")
    elif info[0] == 'Revert':
        car, distance_revert = info[1], int(info[2])
        if cars[car]['mileage'] - distance_revert < 10000:
            cars[car]['mileage'] = 10000
            continue
        else:
            cars[car]['mileage'] -= distance_revert
            print(f"{car} mileage decreased by {distance_revert} kilometers")

for car in cars:
    print(f'{car} -> Mileage: {cars[car]["mileage"]} kms, Fuel in the tank: {cars[car]["fuel"]} lt.')

def find_destinations(ds):
    destinations = []
    i = 0
    while i < len(ds):
        if ds[i] in '=/':
            start_marker = ds[i]
            i += 1
            start = i
            while i < len(ds) and ds[i].isalpha():
                i += 1
            end = i
            if i < len(ds) and ds[i] == start_marker and end - start >= 3:
                destination = ds[start:end]
                if destination[0].isupper():
                    destinations.append(destination)
        else:
            i += 1

    travel_points = sum(len(destination) for destination in destinations)
    destinations_str = ', '.join(destinations)

    return f"Destinations: {destinations_str}\nTravel Points: {travel_points}"


dest = input()
print(find_destinations(dest))

import re


def locate_items(text):
    results = []
    pattern = re.compile(r'([\*\^]+)([a-zA-Z\s]+)([\*\^]+)([^a-zA-Z0-9\s]+)([\d\.\-\s,]+)')

    for match in pattern.finditer(text):
        item_name = match.group(2).strip()
        coords = match.group(5).strip()
        if len(item_name) >= 6 and item_name.replace(" ", "").isalpha() and coords.count(',') == 1:
            results.append(f"Located {item_name} at coordinates {coords}.")
    if results:
        for result in results:
            print(result)
    else:
        print("No matching items found.")


input_text = input()

locate_items(input_text)

tickets = input().split(", ")
symbols = ('@', '#', '$', '^')
correct_ticket_len = 10


def find_most_symbols(ticket):
    return max({s: ticket.count(s) for s in symbols}.items(), key=lambda x: x[1])[0]


def find_most_in_a_row(ticket, symbol):
    return max([len(run) for run in "".join([symbol if char == symbol else " " for char in ticket]).split()] or [0])


for ticket in tickets:
    ticket = ticket.strip()

    if len(ticket) != 20:
        print("invalid ticket")
        continue

    type_symbol = find_most_symbols(ticket[:correct_ticket_len])
    winnings = min([find_most_in_a_row(ticket[:correct_ticket_len], type_symbol),
                    find_most_in_a_row(ticket[correct_ticket_len:], type_symbol)])

    if winnings == 10:
        print(f'ticket "{ticket}" - 10{type_symbol} Jackpot!')

    elif winnings >= 6:
        print(f'ticket "{ticket}" - {winnings}{type_symbol}')

    else:
        print(f'ticket "{ticket}" - no match')

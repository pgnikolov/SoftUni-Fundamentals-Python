class Party:
    def __init__(self):
        self.people = []


party_members = Party()
while True:
    name = input()
    if name == "End":
        break
    else:
        party_members.people.append(name)

print(f"Going: {', '.join(party_members.people)}")
print(f"Total: {len(party_members.people)}")


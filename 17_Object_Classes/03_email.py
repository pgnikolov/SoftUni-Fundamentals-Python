class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []

while True:
    info = input()
    if info == "Stop":
        break
    else:
        infos = info.split(' ')
        sender = infos[0]
        receiver = infos[1]
        content = infos[2]
        email = Email(sender, receiver, content)
        emails.append(email)

indexes_sent = list(map(lambda x: int(x), input().split(', ')))

for i in range(len(emails)):
    if i in indexes_sent:
        emails[i].send()
    print(emails[i].get_info())


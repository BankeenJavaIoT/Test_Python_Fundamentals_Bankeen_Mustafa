recipients = ['b44  44 4rt    ', 'W0u uuT3R', '     4l 3x', ' K  3 n 4n', '54R4h']
new_recipients = list()
for recipient in recipients:
    recipient = recipient.replace('4', 'a').replace('0', 'o').replace('3', 'e').replace('5', 's')
    recipient = recipient.replace(' ', '')
    recipient = recipient.capitalize()
    new_recipients.append(recipient)
print(new_recipients)
# recipients = new_recipients

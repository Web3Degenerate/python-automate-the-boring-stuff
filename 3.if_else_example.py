password = 'swordfish'

if password == 'swordfish':
    print('Access granted.')
else:
    print('Wrong password.')



name = 'Bob'
age = 3000

if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice kiddo')
elif age > 2000:
    print('Unlike you, Alice is not an undead importal vampire')
elif age >100:
    print('You are not Alice granny')


# blank string is falsy as is 0 and 0.0
print('Enter your name')
name = input()
if name != '':
    print('Thank you for entering your name ' + name)
else:
    print('ERROR DETECTED: Name not found.')
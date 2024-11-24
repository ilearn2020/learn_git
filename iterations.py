friends = ['dylan', 'alastair', 'miles', 'alex']
friends_upper = []
friends_with_a_upper = []

for x in friends:
    friends_upper.append(x.upper())

friends_upper_2 = [ xx.upper()  for xx in friends]


print(friends)
print(friends_upper)
print('friends', friends_upper_2)

for x in friends:
    if 'a' in x:
        friends_with_a_upper.append(x.upper())


friends_with_a_upper_2 = [ ff.upper() for ff in friends if 'a' in ff]

print(friends_with_a_upper)
print(friends_with_a_upper_2)

addresses = {
    'dylan' : 'appleton',
    'alastair' : 'botley',
    'miles' : 'cornwall',
    'alex' : 'argentina'}

for xx in addresses:
    print(xx)
    print(addresses[xx])

for xx,yy in addresses.items():
    print(xx,yy)
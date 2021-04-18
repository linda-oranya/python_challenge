data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],
        ['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
        ['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
        ['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
        ['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
        ['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
        ['D5', 98], ['D6', 32]]

# How many sites are there?
field_list = []
for item in data:
    field_list.append(item[0])
print('The number of sites is:', len(field_list))

# How many birds were counted at the 7th site?
print('The number of birds counted at the 7th  site is:', data[6][1])

# How many birds were counted at the last site?
print('The number of birds counted at last site is:', data[-1][1])

# What is the total number of birds counted across all sites?
bird_list = []
for item in data:
    bird_list.append(item[1])
print('The total number of birds counted across all sites is:', sum(bird_list))

# What is the average number of birds seen on a site?
average_bird = sum(bird_list) / len(bird_list)
print('The average number of birds seen on a site is:', average_bird)

# What is the total number of birds counted on sites with codes beginning with C?
listed = []
for item in data:
    if item[0].startswith('C'):
        listed.append(item[1])
print('Total number of birds counted on sites with codes beginning with C is:', sum(listed))

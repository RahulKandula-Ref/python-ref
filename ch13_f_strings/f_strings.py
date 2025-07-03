person = 'Rahul'
coins = 3


print('\n' + person + ' has ' + str(coins) + ' with him. I am talking about ' + person + '.')


print('\n %s has %s with him. I am talking about %s.' % (person, coins, person))


print('\n {} has {} with him. I am talking about {}.'.format(person, coins, person))


print('\n {0} has {1} with him. I am talking about {0}.'.format(person, coins))



print('\n {person} has {coins} with him. I am talking about {person}.'.format(person = person, coins = coins))


player = {
    'person': 'rahul',
    'coins': 3
}
print('\n {person} has {coins} with him. I am talking about {person}.'.format(**player))




# f-strings
print(f"\n {player['person']} has {coins} with him and yes I am talking about {person}")

for n in range(1,11):
    print(f"2.1414 multiplied by {n} is {2.1414 * n:.2f}")


for n in range(1,11):
    print(f"{n} divided by 4 in percentage is : {n / 4:.0%}")
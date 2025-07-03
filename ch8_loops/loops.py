# while loop

value = 0

while value <= 10:
    value += 1
    if value > 20:
        break
    if value % 2 is 0:
        continue
    print(value)
else:
    print('value at this point is ' + str(value))


# for loop
names_arr = ["rishi", "nihi", "sravya", "rahul"]
for s in names_arr:
    if s is 'sravya':
        break
    print(s)

for s in 'sravya':
    print(s)


# ranges
for i in range(2):
    print(i)

for i in range(3, 7):
    print(i)


for n in range(5, 21, 5):
    print(n)
else:
    print('Printed out the table of 5')


# nested loops
actions = ["codes", "sleeps", "eats", "plays"]

for n in names_arr:
    for a in actions:
        if a is 'codes' and n is not 'rahul':
            continue
        print(n + " " + a + ".")
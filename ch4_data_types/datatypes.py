import math

## STRINGS DATA TYPES

# literal assignment
first = 'rahul'
last = 'kumar'

# concat
full = first + ' ' + last

# constructor and casting
birth_year = str(1986)

print(type(birth_year))
print(type('is this ' + birth_year) == str)
print(isinstance(full, str))



# multi line
para = '''
This is a multi line paragraph.  
of my first novel.  
            Should come with up a good opening line here.

And the rest of the book can follow!
'''
print(para)


# escaping and spl characters
opening_line = 'Hey! I\'m back from work !\t Said noone.\n\n Everyone in the room started swiveling their heads\\sniffed as well.'
print(opening_line)


# few string methods
# build a menu
print('')
print('menu'.upper().center(20, '='))
print('coffee'.title().ljust(16, '.') + '$1'.rjust(4))
print('meals'.title().ljust(16, '.') + '$10'.rjust(4))
print('dessert'.title().ljust(16, '.') + '$8'.rjust(4))

print('')

# string indices
print(first[0])
print(first[-1])
print(first[0:-1])
print(first[0:])


print('')
# some boolean returning methods on string
print(first.startswith('r'))
print(first.endswith('r'))



print('')

## BOOLEAN DATA TYPES

aBoolean = True
some_x = bool(False)
print(type(aBoolean))
print(isinstance(some_x, bool))


print('')

## NUMBER types

quantity = int(10)
price = float(23.33)
compl_val = complex(5 + 2j)
print(compl_val.real)
print(compl_val.imag)

# built in fns 
print(abs(quantity * -1))
print(round(price))
print(round(price, 1))


# fns from math module
print(math.pi)
print(round(math.pow(price, 2), 2))
print(math.ceil(quantity))

# casting a string to a num
print('')
zipcode = '1001'
zip_val = int(zipcode)
print(type(zip_val))
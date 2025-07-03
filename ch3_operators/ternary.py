some_num = 500

# if some_num >= 42:
#     print('you are close to the actual answer')
# else:
#     print('try harder')
    
hint = 'you are close' if some_num <= 50 and some_num >=40 else 'try harder'

print(hint)
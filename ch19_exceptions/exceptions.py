x = "2"
try:
    if not type(x) is str:
        raise ValueError("X is not declared as str")
    y = int(x)
except NameError:
    print('Declar X for a start')
except Exception as err:
    print(err)
else:
    y += 10
    print(y)
finally:
    print('Reached end of program!')
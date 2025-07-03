# this is global scope
# do not put anything here
# better to enclose everything in a fn

color = 'blue'

def main_fn():

    print(color)

    def update_global_color():
        global color
        color = 'navy blue'

    update_global_color()
    print(color)

    def greet(*names):
        print('Greeting ' + str(len(names)) + ' people.')
        for n in names:
            print('Hello ' + n)
        # interesting
        color = 'purple'
        print(color)

        def update_this_color():
            nonlocal color
            color = 'super glue'

        update_this_color()    
        print(color + '\n')

    greet('rahul', 'rishi', 'sravya')


# start the program
main_fn()
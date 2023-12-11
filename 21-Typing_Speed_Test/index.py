from time import *
import random as r

# to calculate error
def mistake(string, user_input):
    error = 0
    for i in range(len(string)):
        try:
            if string[i] != user_input[i]:
                error += 1
        except:
            error += 1
    return error

# to calculate word per second
def typing_speed(starting_time, ending_time, user_input):
    # to calculate total time taken
    total_time = ending_time - starting_time
    # to round of the total time taken
    time_R = round(total_time, 2)
    # to calculate speed
    speed = len(user_input) / time_R

    return round(speed)


list_string = ['this is apple', 'its color is red', 'this is orange',
        'its color is orange']

while True:
    string = r.choice(list_string)
    print('\ngiven:',string)
    starting_time = time()

    user_input = input('---------------start typing or Enter q to quit---------------\n')

    if user_input == 'q':
        print('\nThanks\n')
        break
    else:
        ending_time = time()

        speed = typing_speed(starting_time, ending_time,user_input)
        error = mistake(string,user_input)
        print(f'Typing Speed =  {speed} w/s  -  Mistakes = {error}\n')
        print('-------------------------------------------------')


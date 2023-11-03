import random

def definition_free_row():
    arr = []
    number_row = 1
    random_param = 0
    N = 10
    M = 5
    for i in range(N):
        row = []
        for j in range(M):
            random_param = random.random()
            if random_param >= 0.5:
                row.append('X')
            else:
                row.append('O')
        print(f'{number_row } {row}')
        number_row = number_row + 1
        print()
        arr.append(row)
    return arr

def check_free_place():
    number_free_row = 1
    print(f'People {people}')
    if people>5:
        print('You will not be able to sit together!')
    else:
        if people == 1:
            for i in definition_free_row():
                free_places = 0
                for j in i:
                    if j == 'O':                       
                        free_places += 1
                if free_places > 0:
                    print(i)
                    print(f'There are {free_places} empty seats in the {number_free_row} row')
                    print()
                number_free_row += 1
            if free_places == 0:
                print(f'There are no more places available for {people} people!')
        if people == 2:
            for i in definition_free_row():
                free_places = 0
                for j in i:
                    if j == 'O':                       
                        free_places += 1 
                if free_places > 1:
                    print(i)
                    print(f'There are {free_places} empty seats in the {number_free_row} row')
                    print()
                number_free_row += 1
            if free_places < 2:
                print(f'There are no more places available for {people} people!')
        if people == 3:
            for i in definition_free_row():
                free_places = 0
                for j in i:
                    if j == 'O':                       
                        free_places += 1 
                if free_places > 2:
                    print(i)
                    print(f'There are {free_places} empty seats in the {number_free_row} row')
                    print()
                number_free_row += 1
            if free_places < 3:
                print(f'There are no more places available for {people} people!')
        if people == 4:
            for i in definition_free_row():
                free_places = 0
                for j in i:
                    if j == 'O':                       
                        free_places += 1 
                if free_places > 3:
                    print(i)
                    print(f'There are {free_places} empty seats in the {number_free_row} row')
                    print()
                number_free_row += 1
            if free_places < 4:
                print(f'There are no more places available for {people} people!')
        if people == 5:
            for i in definition_free_row():
                free_places = 0
                for j in i:  
                    if j == 'O':                       
                        free_places += 1 
                if free_places > 4:
                    print(i)
                    print(f'There are {free_places} empty seats in the {number_free_row} row')
                    print()
                number_free_row += 1    
            if free_places != 5:
                print(f'There are no more places available for {people} people!')

def check_free_together():
    
    if people == 1:
        number_free_row = 1
        for i in definition_free_row():
            free_places = 0
            for j in i:
                if j == 'O':
                    free_places += 1            
            if free_places > 0:
                print(i)
                print(f'There are {free_places} empty seats in the {number_free_row} row')
                print()
            number_free_row += 1
        if free_places == 0:
            print(f'There are no more places available for {people} people!')

    if people == 2:
        number_free_row = 1
        for i in definition_free_row():
            free_places = 0
            count = 0
            check = False
            for j in i:
                if j == 'O':
                    free_places += 1         
            for place in i:
                if place=='O':
                    count += 1
                    if count==people:
                        check = True
                        break
                elif place=='X':
                    count = 0
            if free_places > 1 and check==True:
                print(i)
                print(f'There are {free_places} empty seats in the {number_free_row} row')
                print()
            number_free_row += 1
        if free_places < 2:
            print(f'There are no more places available for {people} people!')

    if people == 3:
        number_free_row = 1
        for i in definition_free_row():
            free_places = 0
            count = 0
            check = False
            for j in i:
                if j == 'O':
                    free_places += 1         
            for place in i:
                if place=='O':
                    count += 1
                    if count==people:
                        check = True
                        break
                elif place=='X':
                    count = 0
            if free_places > 2 and check==True:
                print(i)
                print(f'There are {free_places} empty seats in the {number_free_row} row')
                print()
            number_free_row += 1
        if free_places < 3:
            print(f'There are no more places available for {people} people!')

    if people == 4:
        number_free_row = 1
        for i in definition_free_row():
            free_places = 0
            count = 0
            check = False
            for j in i:
                if j == 'O':
                    free_places += 1         
            for place in i:
                if place=='O':
                    count += 1
                    if count==people:
                        check = True
                        break
                elif place=='X':
                    count = 0
            if free_places > 3 and check==True:
                print(i)
                print(f'There are {free_places} empty seats in the {number_free_row} row')
                print()
            number_free_row += 1
        if free_places < 4:
            print(f'There are no more places available for {people} people!')

    if people == 5:
        number_free_row = 1
        for i in definition_free_row():
            free_places = 0
            count = 0
            check = False
            for j in i:
                if j == 'O':
                    free_places += 1         
            for place in i:
                if place=='O':
                    count += 1
                    if count==people:
                        check = True
                        break
                elif place=='X':
                    count = 0
            if free_places > 4 and check==True:
                print(i)
                print(f'There are {free_places} empty seats in the {number_free_row} row')
                print()
            number_free_row += 1
        if free_places < 5:
            print(f'There are no more places available for {people} people!')

def go_program():
    global people 
    people = int(input('How many people? '))
    if people == 1:
        check_free_place()
    else:
        together = input('Would you like to sit together on the same row?  Y/N ')
        if together == 'N':
            check_free_place()
        elif people==1 and together == 'Y':
            check_free_place()
        elif together == 'Y':
            check_free_together()
        else:
            print('The command was entered incorrectly! Make a choice between Y and N ')

go_program()
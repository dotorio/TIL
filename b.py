number_of_buttons = int(input())
buttons = list(map(int, input().split()))
number_of_person  = int(input())
for person in range(number_of_person):
    gender, start = map(int, input().split())
    if gender == 1:
        for x in range(number_of_buttons):
            if (x+1) % start == 0:
                if buttons[x] == 0:
                    buttons[x] = 1
                else:
                    buttons[x] = 0
    else:

        for y in range(number_of_buttons):
            if start-y == 0 or start+y == number_of_buttons+1:
                break
            if buttons[start-y-1] == buttons[start+y-1]:
                        
                if buttons[start-y-1] == 1:
                    buttons[start-y-1] = 0
                    buttons[start+y-1] = 0
                else:
                    buttons[start-y-1] = 1
                    buttons[start+y-1] = 1
            else:
                break
        

for z in range(0, len(buttons), 20):
        
    print(' '.join(map(str, buttons[z:z+20])))


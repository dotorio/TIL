import random

continue_game = True
while continue_game:
    print('-------------------------------------')
    print('숫자 야구 게임에 오신 것을 환영합니다!')
    print('컴퓨터의 숫자를 9회 이내로 맞춰주세요.')
    print('3자리, 4자리, 5자리 게임이 가능합니다.')
    print('각 자릿수는 중복되지 않습니다.')
    print('당신은 과연 컴퓨터를 이길 수 있을까요?')
    game_start = False
    while not game_start:
        print('-------------------------------------')
        game_num = input('원하시는 자리를 입력해주세요 : ')
        if not game_num or game_num not in '345' or len(game_num) != 1:
            print("3, 4, 5 중 원하는 자릿수를 입력하여 게임을 시작하세요.")
        else:
            game_start = True
    
    secret_num = ''.join(random.sample('0123456789', int(game_num)))
    num = 1
    while True:
        if num == 10:
            print('-------------------------------------')
            print('당신은 컴퓨터에게 패배하였습니다 메롱메롱')
            print('정답은', secret_num, '였습니다 ㅋㅋ')
            while True:
                if_continue = input('다시 도전하시겠습니까? y/n : ')
                if if_continue == 'n':
                        continue_game = False
                        print('게임을 종료합니다. 다음에 또 봐요!')
                        break
                elif if_continue == 'y':
                    break
                else:
                    print("다시 도전하려면 y, 종료하려면 n을 입력하세요.")           
            break
        else:
            print('-------------------------------------')
            print('지금은', num, '회입니다.')
            user_guess = input("숫자를 추측하세요 : ")
            if not user_guess or not user_guess.isdigit():
                print("올바른 형식의 입력이 아닙니다. 다시 시도하세요.")
                continue
            elif len(user_guess) != int(game_num):
                print("게임의 자릿수에 맞게 입력해주세요.")
                continue
            elif len(user_guess) != len(set(user_guess)):
                print("자릿수가 중복되지 않게 입력해주세요.")
                continue
            strikes = 0
            balls = 0
            for i in range(int(game_num)):
                if user_guess[i] == secret_num[i]:
                    strikes += 1
                elif user_guess[i] in secret_num:
                    balls += 1
            if strikes == int(game_num):
                print("축하합니다! 컴퓨터에게 승리했습니다!")
                while True:
                    if_continue = input('다시 도전하시겠습니까? y/n : ')
                    if if_continue == 'n':
                        continue_game = False
                        print('게임을 종료합니다. 다음에 또 봐요!')
                        break
                    elif if_continue == 'y':
                        break
                    else:
                        print("다시 도전하려면 y, 종료하려면 n을 입력하세요.")           
                break
            elif strikes and balls:
                print(strikes, '스트라이크', balls, '볼') 
            elif not strikes and not balls:
                print('아웃!')                 
            elif not balls:
                print(strikes, '스트라이크')
            else:
                print(balls, '볼')  
            num += 1    
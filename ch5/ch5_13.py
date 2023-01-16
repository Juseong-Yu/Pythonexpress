import random

def dice_game():
    print('========== dice_game() 호출 ==========')

    human = random.randint(1,6)
    computer = random.randint(1,6)

    print('인간: 주사위값=',human)
    print('컴퓨터: 주사위값=',computer)
    
    if human > computer:
        print('인간 승리')
    elif human < computer:
        print('컴퓨터 승리')
    else:
        print('비김')
    
    print('========== dice_game() 복귀 ==========\n\n')

while True:
    dice_game()
    stop = input('중단할까요? y/n\n')
    if stop == 'y':
        break
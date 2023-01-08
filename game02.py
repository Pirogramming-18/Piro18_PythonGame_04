"""
~ 게임 룰 ~
병뚜껑 안에 적힌 숫자를 맞히는 게임.
1~50까지의 숫자 중 하나씩 돌아가면서 선택.
정답이 선택한 숫자보다 높으면 Up! 낮으면 Down!
누구라도 맞힐 때까지 진행.
맞힌 사람 빼고 전원 한 잔 마시기!
"""

import random


userList_Name = ['혜원', '성일', '민지', '창진'] #샘플

def game02():
    player_list = userList_Name
    loser_list = player_list
    
    print("업앤다운 게임을 고르셨군요! 게임 시작~\n병뚜껑 안쪽에 적혀 있는 숫자를 맞혀 보세요! 1부터 50까지의 정수 중에 있습니다!")
    num_list = list(range(1, 51)) #편의를 위해 1~50 숫자 리스트 만들기
    answer = random.randint(1, 50) #정답 숫자 랜덤으로 선택

    while True:
        while True:
            try:
                my_num = input("{}의 선택은: ".format(userList_Name[0]))
                if my_num.isdigit == False or int(my_num) not in num_list:
                    raise Exception
            except:
                print("다시 입력해주세요!")
            else:
                break
        my_num = int(my_num)

        if my_num == answer:
            print("˗ˋˏ 와 ˎˊ˗ 맞았습니다! {} 빼고 모두 한잔해~".format(userList_Name[0]))
            loser_list.remove(userList_Name[0])
            break
        elif my_num < answer:
            del num_list[:num_list.index(my_num)+1]
            print("음... {}보다 Up!".format(str(my_num)))
            #print(num_list)
        elif my_num > answer:
            del num_list[num_list.index(my_num):]
            print("음... {}보다 Down!".format(str(my_num)))
            #print(num_list)

        n = 1
        for i in range(len(player_list)-1):
            num_choice = random.choice(num_list)
            num = num_choice
            print("{}의 선택은: {}".format(player_list[n], num))
            if num == answer:
                print("˗ˋˏ 와 ˎˊ˗ 맞았습니다! {} 빼고 모두 한잔해~".format(player_list[n]))
                loser_list.remove(player_list[n])
                break
            elif num < answer:
                del num_list[:num_list.index(num)+1]
                print("음... {}보다 Up!".format(str(num)))
                #print(num_list)
            elif num > answer:
                del num_list[num_list.index(num):]
                print("음...{}보다 Down!".format(str(num)))
                #print(num_list)
            n += 1
        if num == answer: break
        
    print("~~~~~게임 끝!!~~~~~")
    print(loser_list) #확인용
    
game02()
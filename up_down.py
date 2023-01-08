"""
~ 게임 룰 ~
병뚜껑 안에 적힌 숫자를 맞히는 게임.
1~50까지의 숫자 중 하나씩 돌아가면서 선택.
정답이 선택한 숫자보다 높으면 Up! 낮으면 Down!
누구라도 맞힐 때까지 진행.
맞힌 사람 빼고 전원 한 잔 마시기!
"""

import random

userList_Name = ['혜원', '성일', '민지', '창진'] #샘플. 나중에 지워야 함

def up_down():
    player_list = userList_Name
    loser_list = player_list
    
    print("Up&Down 게임을 고르셨군요! 병뚜껑 안쪽에 적혀 있는 숫자를 맞혀 보자!")
    print("정답자 뺴고 전원 한잔 마시는 지옥의 게임... 1부터 50까지의 정수 중에 답이 있으니 맞혀 보세요~!")
    num_list = list(range(1, 51)) #편의를 위해 1~50 숫자 리스트 만들기
    answer = random.randint(1, 50) #정답 숫자 랜덤으로 선택

    while True:
        while True:
            try:
                my_num = input("{}의 선택은?? ".format(player_list[0]))
                if my_num.isdigit == False or int(my_num) not in num_list:
                    raise Exception
            except:
                print("잘 생각해보고 다시 입력해주세요!")
            else:
                break
        my_num = int(my_num)

        if my_num == answer:
            if len(player_list) == 2:
                print("˗ˋˏ 와 ˎˊ˗ 맞았습니다!")
                print("아 누가 술을 마셔~ {}(이)가 술을 마셔~ {}👏👏 👏👏 {}👏👏 👏👏 원~~샷!!!".format(player_list[1], player_list[1][0], player_list[1][1]))
            else:
                print("˗ˋˏ 와 ˎˊ˗ 맞았습니다!")
                print("{} 빼고 모두 마~셔 마~셔 ٩( ᐛ )و 네발로 기~어~ (งᐖ)ว".format(player_list[0]))
            loser_list.remove(player_list[0])
            break
        elif my_num < answer:
            del num_list[:num_list.index(my_num)+1]
            print("음... {}보다 Up!".format(str(my_num)))
        elif my_num > answer:
            del num_list[num_list.index(my_num):]
            print("음... {}보다 Down!".format(str(my_num)))

        n = 1
        for i in range(len(player_list)-1):
            num_choice = random.choice(num_list)
            num = num_choice
            print("{}의 선택은?? {}".format(player_list[n], num))
            if num == answer:
                if len(player_list) == 2:
                    print("˗ˋˏ 와 ˎˊ˗ 맞았습니다!")
                    print("아 누가 술을 마셔~ {}(이)가 술을 마셔~ {}👏👏 👏👏 {}👏👏 👏👏 원~~샷!!!".format(player_list[0], player_list[0][0], player_list[0][1]))
                else:
                    print("˗ˋˏ 와 ˎˊ˗ 맞았습니다!")
                    print("{} 빼고 모두 마~셔 마~셔 ٩( ᐛ )و 네발로 기~어~ (งᐖ)ว".format(player_list[n]))
                loser_list.remove(player_list[n])
                break
            elif num < answer:
                del num_list[:num_list.index(num)+1]
                print("음... {}보다 Up!".format(str(num)))
            elif num > answer:
                del num_list[num_list.index(num):]
                print("음...{}보다 Down!".format(str(num)))
            n += 1
        if num == answer: break
        
    print("~~~~~게임 끝!!~~~~~")
    print(loser_list) #확인용 #나중에 지워야 함
    
up_down()
'''병뚜껑 꼬리 날리기
게임 설명
1. 병뚜껑 수명 설정 (수명은 10~20 사이)
2. 본인(me)부터 시작해서 돌아가면서 병뚜껑 치기
3. 플레이어가 약하게(1), 적당히(2), 세게(3) 치기를 설정
4. 게임을 종료시킨 플레이어의 옆 사람을 진 사람으로 설정 
4. 진 사람 출력, 리스트 값 반환
'''

import random

pre_userList=['혜원','성일','민지','창진']
userList_Name=pre_userList

def Game(userList_Name):

    #병뚜껑 수명 설정
    cap_life=random.randint(10,20)

    # 뚜껑 수명 0 이하 시 게임 종료
    while 1:
        print('타격 데미지는 약,중,강 1,2,3 순으로 1에서 3사이 값을 적어주세요') # 병뚜껑 타격 데미지 설정 약: 1 중: 2 강: 3
        me_hit=int(input('병뚜껑을 얼마나 세게 칠지? 너의 힘을 보여줘!💪: '))

        # 사용자가 입력한 숫자가 1부터 3까지의 숫자가 아니면 경고 메시지를 출력
        if me_hit < 1 :
          print("너무 약하게 때린거 아닌가요?🤨")
          continue
        elif me_hit > 3:
          print("손가락 부러질라구~😟")
          continue
      
        # 사용자의 입력을 총 합에서 뺌
        cap_life -= me_hit

        #데미지 알려주기
        if me_hit == 1 :
          print("{0}은(는) 약하게 타격!".format(userList_Name[0]))
        elif me_hit == 2:
          print("{0}은(는) 적당히 타격!".format(userList_Name[0]))
        elif me_hit == 3:
          print("{0}은(는) 강하게 타격!".format(userList_Name[0]))
        # 총 합이 0 이하가 되면 게임 종료
        if cap_life <= 0:
          print("게임 종료! {0} 탈락!🥳".format(userList_Name[1]))
          loser=[]
          loser.append(userList_Name[1])
          return loser


        for i in range(len(userList_Name)-1): # me 제외 인원 수만큼 반복 
          others_hit = random.randint(1,3) # 컴퓨터가 입력할 데미지를 임의로 생성

          cap_life -= others_hit 

          if others_hit == 1 :
            print("{0}은(는) 약하게 타격!".format(userList_Name[i+1]))
          elif others_hit == 2:
            print("{0}은(는) 적당히 타격!".format(userList_Name[i+1]))
          elif others_hit == 3:
            print("{0}은(는) 강하게 타격!".format(userList_Name[i+1]))

          if cap_life <= 0: 
            if i+2==len(userList_Name): #유저 리스트의 마지막 인원이 선택되면 맨 앞 인원을 반환
              print("게임 종료! {0} 탈락!🥳".format(userList_Name[0]))
              loser=[]
              loser.append(userList_Name[0])
              return loser
            else: #이외는 바로 옆 인원을 반환
              print("{0} 탈락!".format(userList_Name[i+2]))
              loser=[]
              loser.append(userList_Name[i+2])
              return loser

print((Game(userList_Name)))
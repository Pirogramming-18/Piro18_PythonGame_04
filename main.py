import random
import sys
from timing_game import timing_game
from up_down import up_down
#from subway import*

pre_userList=['혜원','성일','민지','창진']
#user_info={}
final_userList=[]
userList_Name=[]
limit_list=[2,4,6,8,10]
Me=''


def before_game():
    print('가보자고🐬💨')
    Me=input('이름이 뭐에요? : ')

    print(Me)
    print("===========소주기준 당신의 주량은?=============")
    print("1. 소주 0.5병(2잔)")
    print('2. 소주 0.5~1병(4잔)')
    print('3. 소주 1~1.5병(6잔)')
    print('4. 소주 1.5~2병(8잔)')
    print('5. 소주 2병 이상(10잔)')
    print("==============================================")

    while 1:
        try:
            limit=int(input('당신의 치사량(주량은) 어느정도인가요?(1~5 사이 선택!):'))
            if not 1<=limit <=5:raise Exception
                
        except:
            print('1~5사이 정수를 입력해주세여..')
        else:
            print("{}님 당신의 치사량은 {}잔으로 입력하셨습니다!\n".format(Me,limit_list[limit-1]))
            user_info={}
            user_info['name']=Me
            user_info['limit']=limit_list[limit-1]
            user_info['drink']=0
            user_info['life']=user_info['limit']-user_info['drink']
            final_userList.append(user_info)
            userList_Name.append(Me)
            break
        
    while True:
        try:
            friend_num=int(input('함께 취할 친구들은 얼마나 필요하나요? 최대 3명 입니다: '))
            if not 1<=friend_num <=3:raise Exception
                
        except:
            print('1~3사이 정수를 입력해주세여..')
        else:
            
            user_select_list=[]
            for i in range(friend_num):
                x=random.randint(0,len(pre_userList)-1)
                #user는 여러명 중복해서 선택하면 안되니까 중복이면 다시 뽑기
                while x in user_select_list:
                    x=random.randint(0,len(pre_userList)-1)
                user_select_list.append(x)
                l=limit_list[random.randint(0,4)]        
                print('오늘 함께 취할 친구는 {}입니다! (치사량: {})'.format(pre_userList[x],l))
                
                user_info={}#?왜 비워줘야하지?
                user_info['name']=pre_userList[x]
                user_info['limit']=l
                user_info['drink']=0
                user_info['life']=user_info['limit']-user_info['drink']

                final_userList.append(user_info)
                userList_Name.append(user_info['name'])

            break
    return Me
        

def show_state():
    print('\n')
    for user in final_userList:
        print('{}는 지금까지 {}잔 마셨지롱~ 치사량까지 {} 남았슴다 '.format(user['name'],user['drink'],user['life']))


def show_game():
    print("\n========오늘의 ALCohol Game=============")
    print('1. 눈치게임 !')
    print('2. 업다운 게임 !')
    print('3. 지하철 게임 !')
    print('4.')
    

def select_game(user,Me):
    while True:
        try: 
            if user['name']==Me:
                select=int(input("술게임 진행중!{}(이)가 좋아하는 랜덤 게임~무슨게임? 게임 스타트!: ".format(user['name'])))
            else:
                p=input('술게임 진행중! 다른사람의 턴입니다. 그만하고 싶으면 "e"을, 계속하고 싶으면 아무키나 눌러줘요:')
                if p=='e':
                    return 0
                
                select=random.randint(1,2)
                print('술게임 진행중!{}(이)가 좋아하는 랜덤 게임~무슨게임? 게임 스타트!:{}'.format(user['name'],select))
                
            if not 1<=select<=2:
                raise Exception()
        
        except: print("1에서 4사이 정수 중에 골라보시라구..\n")
        else:
            print('{}님이 게임을 선택했습니다!\n'.format(user['name']))
            return select
        
# 한판 한 후 게임결과 계산
def calc_life(loser_list):
    for user in final_userList:
        for i in range(len(loser_list)):
            if user['name']==loser_list[i]:
                user['drink']+=1
                user['life']=user['limit']-user['drink']
                
#치사량 도달 체크
def check_life(final_userList):
    for user in final_userList:
        if user['life']==0:
            print(" 안타깝게도 {}(이)가 치사량에 도달했습니다..꿈나라로 잘가길...".format(user['name']))
            print("술게임은 끝~ 안녕 ! ! ! 🐬")
            sys.exit()
     
         
#게임 시작
def main():
    Me=before_game()
        
    show_state()
    while True:
        for user in final_userList:
            select=0
            show_game()
        
            #게임선택
            select=select_game(user,Me)
            
            if select==0:
                print('오키 쉬도록 합시다~ 다음에 봐요 안녕~')
                sys.exit()
            
            # 개별 게임 진행      
            if select==1:
                loser_list=timing_game(userList_Name)
                
            elif select==2:
                loser_list=up_down(userList_Name)
                
            elif select==3:
                print('3번게임')
                #loser_list=subwayGame(userList_Name)
                
            elif select==4:
                print('4번게임')
        
            calc_life(loser_list)#게임 결과 점수 계산 
            show_state() #현재 상태 출력
            check_life(final_userList) #치사량 도달 체크
            
main()



    
        
import random
from game01 import game01

pre_userList=['혜원','성일','민지','창진']
#user_info={}
final_userList=[]
userList_Name=[]
limit_list=[2,4,6,8,10]
Me=''


def before_game():
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
            print("{}님 당신의 치사량은 {}잔으로 입력하셨습니다!".format(Me,limit_list[limit-1]))
            user_info={}
            user_info['name']=Me
            user_info['limit']=limit_list[limit-1]
            user_info['drink']=0
            user_info['life']=0
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
                user_info['life']=0

                final_userList.append(user_info)
                userList_Name.append(user_info['name'])

            break
        

def show_state():
    for user in final_userList:
        print('{}는 지금까지 {}잔 마셨지롱~ 치사량까지 {} 남았슴다 '.format(user['name'],user['drink'],user['life']))


def show_game():
    print("========오늘의 ALCohol Game=============")
    print('1.')
    print('2.')
    print('3.')
    print('4.')
    print('5.')

def select_game():
    try:
        select=int(input("술게임 진행중!{}(이)가 좋아하는 랜덤 게임~무슨게임? 게임 스타트!: "))
        
        if not 1<=select<=4:
            raise Exception()
    
    except: print("1에서 5사이 정수 중에 골라보시라구..")
    else:
        print('{}님이 게임을 선택했습니다!'.format(Me))
        return select
        

         
#게임 시작
def main():
    before_game()
    
    show_state()
    for user in final_userList:
        select=0
        show_game()
        if user['name']==Me:
            select=select_game()
        else:
            select=random.randint(1,5)
        
        if select==1:
           print('1')
        

before_game()
game01.game01(userList_Name)
    
        
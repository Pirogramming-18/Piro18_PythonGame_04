import random
from collections import deque


def timing_game(user_list,Me):
    max_num=len(user_list)
    print("눈치게임을 고르셨군요! 바로 시작")
    
    game_user_list=[]
    
    #눈치게임 순서 번호 랜덤으로 부여    
    list=[] #중복체크용
    for user in user_list:
        if user==Me:
            x=int(input('몇번째로 일어나고 싶어요? (1~{}사이 고르기): '.format(len(user_list))))
        else: x=random.randint(1,max_num)
        
        #중복허용 x 코드-->>>팀원들 물어보고 결정!
        #while x in list:
        #    x=random.randint(1,max_num)
        #list.append(x) 
        
        users={}
        users['name']=user
        users['num']=x
        game_user_list.append(users)
    
    double_list=[]#동시에 일어난 사람들 리스트
    #동시에 일어선 ver      
    for k in range(1,max_num+1):
        for i in range(0,max_num):
            if k==game_user_list[i]['num']:double_list.append(game_user_list[i]['name'])
        if len(double_list)>1:break #중복인 유저가있다면 for문 탈출
        else:double_list=[] #다시 리스트 비운 후 중복유저 체크
    if double_list:
        for user in double_list:
            print('{}(이)가 동시에 일어났습니다!'.format(user))
        print("이분들은 탈락~")
        return double_list
    
    #마지막 사람이 지는 ver(동시 x)
    line_list=[]
    deq=deque(game_user_list)
    
    for i in range(1,max_num+1):
        q=deq.popleft()
        
        while i!=q['num']:

            deq.append(q)
            q=deq.popleft()
        line_list.append(q['name'])

    
    loser=''
    for i in range(max_num):
        print("{}: {} !".format(line_list[i],i+1))
        if (i+1)==max_num:
            loser=line_list[i]
            
    
            
    else: print('\n{}님이 마지막에 일어나서 졌습니다!'.format(loser))
    
    loser_list=[]
    loser_list.append(loser)
    
    return loser_list
    
    
        
#print("return:",timing_game(['혜원','민지',"성일","창진"],"혜원"))   
        
    
    
    
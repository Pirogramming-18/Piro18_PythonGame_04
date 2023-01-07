import random
from collections import deque


def game01(user_list):
    max_num=len(user_list)
    print("눈치게임을 고르셨군요! 바로 시작")
    
    game_user_list=[]
    
    #눈치게임 순서 번호 랜덤으로 부여
    
    list=[] #중복체크용
    for user in user_list:
        x=random.randint(1,max_num)
        while x in list:
            x=random.randint(1,max_num)
        list.append(x) 
        
        users={}
        users['name']=user
        users['num']=x
        game_user_list.append(users)
  

        
    #동시에 일어선 ver->근데 이거 할지말지 좀 고민해봐야함
    # for i in range(0,num):
    #     for j in range(i+1,num):
    #         if game_user_list[i]['num']==game_user_list[j]['num']:
    #             print("{} {}이 동시에 일어섰다! 탈락!".format(game_user_list[i]['name'],game_user_list[j]['name']))
    #             return game_user_list[i]['name'],game_user_list[j]['name']
    
 
    #마지막 사람이 지는 ver
    line_list=[]
    deq=deque(game_user_list)
    print(deq)
    for i in range(1,max_num+1):
        q=deq.popleft()
        
        while i!=q['num']:

            deq.append(q)
            q=deq.popleft()
        line_list.append(q['name'])
    
 
        
    # line_list=[]
    # for user in game_user_list:
    #     if user['num']==1:
    #         line_list.append(user['name'])
    #         print(user['name'])
    #     elif user['num']==2:
    #         line_list.append(user['name'])
    #     elif user['num']==3:
    #         line_list.append(user['name'])
    #     elif user['num']==4:
    #         line_list.append(user['name'])

    loser=''
    for i in range(max_num):
        print("{}: {} !".format(line_list[i],i+1))
        if (i+1)==max_num:
            loser=line_list[i]
            
    print('\n{}님이 마지막에 일어나서 졌습니다!'.format(loser))
    return loser
    
    
        
            
game01(['혜원','민지',"성일","창진"])   
        
    
    
    
# Subway Game

import requests # for API requests
from bs4 import BeautifulSoup 
import random # Computer 랜덤 확률
import time  # 시간 제한용
from threading import Thread, Event
event = Event() # 이벤트 객체
answer = 0 # 전역변수 : 답안


def subwayGame(name_list):

    key = '4a48476c4d7869783130366346516651'  # API key

    print("🚎 지하철~ 지하철~~!    지하철~ 지하철~~~ 🚎")
    print("🚎 몇호선~~ 몇호선~!    몇호선~ 몇호선??? 🚎 \n")
    
    while True:
        try:
            print("1~9호선, 수인분당선만 가능합니다!")
            line_no = input("지하철 호선을 입력하세요! 1~9호선은 해당 숫자, 수인분당선은 0을 입력하세요. ex) 2 : ")

            if not line_no.isdigit() or 0 > int(line_no) or int(line_no) > 9:
                raise Exception("숫자 1에서 9까지만 입력해주세요.")

            break
        except Exception as e:
            print(e)
    
    if int(line_no) == 0:
        line_no = '수인분당선'
        url = "http://openapi.seoul.go.kr:8088/" + \
        key + "/xml/SearchSTNBySubwayLineInfo/1/500/ / /" + line_no
        print("\n")
        print("🚎 수인분당선~ 수인분당선! 수인분당선~ 수인분당선!! 🚎")
    
    else:
        url = "http://openapi.seoul.go.kr:8088/" + \
        key + "/xml/SearchSTNBySubwayLineInfo/1/500/ / /0" + line_no + "호선"
        print("\n")
        print(f'🚎 {line_no}호선~ {line_no}호선! {line_no}호선~ {line_no}호선!! 🚎')

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "xml")

    stationList = [nm.string for nm in soup.find_all('STATION_NM')]

    # play the game
    result = playGame(stationList, name_list)
    
    result_li = []
    result_li.append(result)
    print(f'{result}(이)가 한 잔 마십니다~\n')
    return result_li


def playGame(stationList, name_list):
    # 전역 변수
    global answer
    global event

    result = 0 # 리턴할 결과값(str)
    time_limit = 5 # 시간 제한

    # thread용 변수 생성
    threads = ['th'+str(i) for i in range(0, len(stationList))]
    j = -1 # for threads
    k = 0 # for name_list
    turns = len(name_list)

    while len(stationList) != 0:
    # Start the game thread (데몬 쓰레드)
        j += 1
        if k == turns:
            k = 0

        # player 차례
        if k == 0:
            print(f"제한 시간 {time_limit}초!")
            threads[j] = Thread(target=subThread, args=(name_list, ), daemon=True)
            threads[j].start()

            # 시간이 지나는 main 쓰레드
            timer = 0
            while timer <= time_limit:
                time.sleep(0.1)
                if event.is_set():
                    break 
                timer += 0.1

            if event.is_set() and answer in stationList:
                print("정답!!")
                event.clear()
                stationList.remove(answer)
                k += 1 # 차례 넘기기

            elif event.is_set() and answer not in stationList:
                print("그거 이미 했거나, 틀렸어요~!")
                return name_list[0]

            elif event.is_set() == False:
                print('\n')
                print("시간 초과!")
                return name_list[0]

        # computer 차례
        else:
            print(f'{name_list[k]}의 차례 ... ', end='')
            
            prob = random.randint(0, 100)

            # 컴퓨터가 맞추는 경우 -> (100 - prob)%
            if prob >= 10:
                time.sleep(0.4)
                print('쿵! ', end='')
                time.sleep(0.4)
                print('짝!! ', end='')
                time.sleep(0.8)
                pick = random.randint(0, len(stationList)-1)
                print(f'{stationList[pick]}!')
                stationList.remove(stationList[pick])

                if (k-1) == turns: 
                    k = 0
                else:
                    k += 1             

            # 컴퓨터가 틀리는 경우
            else:
                time.sleep(0.4)
                print('쿵... ', end='')
                time.sleep(0.4)
                print('짝...... ', end='')
                time.sleep(0.8)
                print("몰라!!! 내가 이걸 어떻게 알아!!")
                time.sleep(0.7)
                print(f'아 ~~ {name_list[k]}(이)가 틀렸어요... 어쩌겠어.. 마셔야지.. 마셔 마셔~~ \n')
                
                result = name_list[k]
                break


    if len(stationList) == 0:
        print("와 이걸 어떻게 다하셨어요? 뭐... 이러면 시작한 사람이 마시는거 아시죠?")
        return name_list[0]

    print("게임 끝!")
    return result


def subThread(name_list):
    global answer
    global event
    answer = input(f"{name_list[0]}(플레이어)의 입력 차례, 역을 입력해주세요! : ")
    event.set()
    return


name_list = ['성일', '혜원', '민지', '창진'] # 임시
subwayGame(name_list)
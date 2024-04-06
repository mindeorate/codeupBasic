while True: #계속 반복
    try:
        a = int(input())
        if a == 0: 
            break #0이면 종료
        print(a)
    except ValueError: #오류날 경우
           pass # 무시

'''
마스크를 쓰지 않고는 밖을 다니면 안 되는 코로나19 시대입니다.
코로나19가 장기화되면서 코로나 블루라는 말이 나올 정도로 우울한 사람들이 많아지고 있습니다.

세계적인 전기자동차 회사 경영자인 '얼른 마스크'씨는
자신의 전기자동차를 타는 고객들이 조금이라도 행복할 수 있기를 바라며
판매하는 전기자동차 번호판 일련번호 4자리를 행복 수(happy number)로 채우고자 합니다.

행복 수는 각 자릿수의 제곱의 합으로 변환하는 과정을 반복할 때 언젠가는 1에 도달하는 수입니다.
예로, 13 → 1x1 + 3x3 = 10 → 1x1 + 0x0 = 1이므로 13은 행복 수입니다.

행복 수가 아닌 것은 슬픈(sad) 수 또는 불행(unhappy) 수라고 불립니다.
예로, 4 → 4x4 = 16 → 1x1 + 6x6 = 37 → 3x3 + 7x7 = 58 → ... → 4 로 순환하여 결코 1에 도달할 수 없으니 4는 슬픈 수입니다.

문제
'얼른 마스크'씨 회사 전기자동차의 일련번호가 될 수 있는 1 ~ 9999 범위의 행복 수는 모두 몇 개이고
그 총합은 얼마인지 구하는 프로그램을 작성해서 보내주세요 작성하세요.

입력
각 범위의 최댓값을 한 줄에 하나씩 입력으로 받습니다. 최종적으로 구하고자 하는 범위의 최댓값은 9999이므로 소스코드 안에 하드코딩 해도 됩니다.
9
99

출력
범위와 행복 수의 개수 그리고 총합을 아래와 같이 출력합니다.
1 ~ 9 범위의 행복 수는 2개이고 총합은 8입니다.
1 ~ 99 범위의 행복 수는 19개이고 총합은 924입니다.
'''

import time
from tqdm import tqdm

a = 9999
result_list = []

# 숫자로
def happy_number(num):
    start = time.time()  # 시작 시간 저장
    for i in tqdm(range(num)):
        input_num = i + 1
        sum_pow_num = input_num
        sum_pow_lsit = []

        for j in range(999):
            thousand, hundred, ten, one = digit(sum_pow_num)
            sum_pow_num = pow_num(thousand, hundred, ten, one)     
            # print(j, sum_pow_lsit)

            if sum_pow_num == 1:
                result_list.append(input_num)
                break
            elif sum_pow_num in sum_pow_lsit:
                break

            sum_pow_lsit.append(sum_pow_num)

    print(f'sum : {sum(result_list)}, length : {len(result_list)}, sum * length : {sum(result_list) * len(result_list)}')
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
    # return num

def digit(input_num):
    ten, hundred, thousand = 0, 0, 0
    if input_num >= 1000:
        thousand = (input_num // 1000)
    if input_num >= 100:
        hundred = (input_num % 1000) // 100
    if input_num >= 10:
        ten = (input_num % 100) // 10
    one = (input_num % 10) // 1
    # print(thousand, hundred, ten, one)

    return thousand, hundred, ten, one
    

def pow_num(thousand, hundred, ten, one):
    tho_pow_num = pow(thousand, 2)
    hun_pow_num = pow(hundred, 2)
    ten_pow_num = pow(ten, 2)
    one_pow_num = pow(one, 2)
    # print(tho_pow_num, hun_pow_num, ten_pow_num, one_pow_num)

    sum_pow_num = tho_pow_num + hun_pow_num + ten_pow_num + one_pow_num

    # return tho_pow_num, hun_pow_num, ten_pow_num, one_pow_num
    return sum_pow_num

happy_number(a)



#####################################################################

# 문자로
def happy_number2(num):
    count = 0
    sum_num = 0    
    start = time.time()  # 시작 시간 저장
    for i in tqdm(range(num)):
        sum_pow_lsit = []
        if happy_or_unhappy_num(i+1, sum_pow_lsit):
            count += 1
            sum_num += (i + 1)
    print(count * sum_num)
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

def happy_or_unhappy_num(num, sum_pow_lsit):
    key_num = 0

    for i in str(num):
        key_num += (pow(int(i), 2))
    
    if key_num == 1:
        return True
    elif key_num in sum_pow_lsit:
    # elif key_num == 4:
        return False
    else:
        sum_pow_lsit.append(key_num)
        # print(sum_pow_lsit)
        return happy_or_unhappy_num(key_num, sum_pow_lsit)

happy_number2(a)

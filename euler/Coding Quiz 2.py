'''
우리말을 쓰는 평범한 사람이라면 1억원 1조원을 일억원, 일조원이라 하지 억원, 조원이라 읽지는 않습니다. 
반면에 1만원, 1천원, 1백원의 경우는 일만원, 일천원, 일백원이라 하지 않고 만원, 천원, 백원, 십원이라 읽습니다. 
또한 '80,270원'처럼 금액의 표기는 천단위로 콤마를 찍지만 실제로 읽을 때는 '팔만 이백칠십원'처럼 만단위로 분리하여 읽습니다.

"배조스님의 계좌에서 사이냅소프트님의 계좌로 일조 사천 일백 팔십 오억 원을 이체합니다. 동의하시면 1번을..."

계좌이체 음성안내의 부자연스러운 금액 표현과 띄어읽기가 거슬렸던 암아존 배조스씨를 위해 이체금액을 한글로 자연스럽게 읽을 수 있는 프로그램을 작성해서 보내주세요 작성하세요. 
프로그래밍 언어는 가장 자신있는 것을 사용하세요.

입력
암아존 배조스님의 은행 이체한도는 100조원으로 설정돼 있으므로 입력 금액의 범위는 1원에서 100조원까지입니다.
모든 금액은 천단위 구분자인 콤마가 표시돼있고 금액단위인 원으로 끝납니다.
예로 아래와 같은 입력이 가능하고 입력은 별도 파일에서 읽어와도 되고, 소스코드안에 포함시켜도 됩니다.
물론 UI를 만들어 사용자로부터 직접 입력 받아도 좋습니다.

1원
80,270원
111,111원
1,234,567,890원
100,000,000,000,000원

출력
각각의 입력에 대하여 만단위로 띄어쓰기 구분된 자연스러운 한글읽기를 출력합니다.
위 예의 출력은 다음과 같습니다.

일원
팔만 이백칠십원
십일만 천백십일원
십이억 삼천사백오십육만 칠천팔백구십원
백조원
'''

num_list = {1 : '일', 2 : '이', 3 : '삼', 4 : '사', 5 : '오', 6 : '육', 7 : '칠', 8 : '팔', 9 : '구', 0 : ''}
unit_list = {1 : '', 2 : '십', 3 : '백', 4 : '천', 
             5 : '만', 6 : '십만', 7 : '백만', 8 : '천만', 
             9 : '억', 10 : '십억', 11 : '백억', 12 : '천억', 
             13 : '조', 14 : '십조', 15 : '백조', 16 : '천조'}

a = '111,111,111,111,111원'

amount_lists = ['1원', '4원', '8원', '9원', '10원', '17원', '79원', '80원', '95원', '205원', '809원', '851원', '878원', '2,000원','2,800원', 
               '7,008원', '8,174원', '9,718원', '45,150원', '50,000원', '69,700원', '382,915원', '431,409원', '921,500원', '5,003,052원',
               '5,039,670원', '6,835,623원', '8,000,000원', '10,000,003원', '35,100,000원', '39,997,777원', '90,021,015원', '93,275,690원', 
               '403,197,000원', '459,176,461원', '730,080,000원', '999,999,000원', '6,887,000,000원', '7,000,020,000원', '7,700,000,500원', 
               '7,848,761,270원', '38,048,620,625원', '57,000,000,000원', '74,778,562,249원', '97,417,165,814원', '101,000,120,000원', 
               '343,000,000,000원', '458,807,907,862원', '872,818,015,000원', '6,278,000,015,000원', '7,991,000,844,000원', '9,000,400,000,675원', 
               '22,018,914,675,100원', '78,196,000,000,000원', '85,000,904,224,858원', '95,000,000,404,918원']

def num_to_txt(amount):
    # result = []
    trillion_num = []
    shillion_num = []
    ten_thousand = []
    won___number = []

    amount_num = amount[:-1].replace(',', '')

    for i, num in enumerate(amount_num):
        # if num == '0':
        #     continue
        if len(amount_num) - i > 12: # 조
            if num == '1' and len(amount_num) - i != 13:
                trillion_num.append(unit_list[len(amount_num) - 12 - i])
            elif num != '0':
                trillion_num.append(num_list[int(num)] + unit_list[len(amount_num) - 12 - i])
            if len(amount_num) - i == 13 and trillion_num:
                trillion_num.append(unit_list[13])

        if len(amount_num) - i <= 12 and len(amount_num) - i > 8: # 억
            if num == '1' and len(amount_num) - i != 9:
                shillion_num.append(unit_list[len(amount_num) - 8 - i])
            elif num != '0':
                shillion_num.append(num_list[int(num)] + unit_list[len(amount_num) - 8 - i])
            if len(amount_num) - i == 9 and shillion_num:
                shillion_num.append(unit_list[9])

        if len(amount_num) - i <= 8 and len(amount_num) - i > 4: # 만
            if num == '1' and len(amount_num) - i != 5:
                ten_thousand.append(unit_list[len(amount_num) - 4 - i])
            elif num != '0':
                ten_thousand.append(num_list[int(num)] + unit_list[len(amount_num) - 4 - i])

            if len(amount_num) - i == 5 and ten_thousand:
                ten_thousand.append(unit_list[5])

        if len(amount_num) - i <= 4 and len(amount_num) - i > 0: # 일
            if num == '1' and len(amount_num) - i != 1:
                won___number.append(unit_list[len(amount_num) - 0 - i])
            elif num != '0':
                won___number.append(num_list[int(num)] + unit_list[len(amount_num) - 0 - i])
            # if len(amount_num) - i == 1:
            #     won___number.append('원')

    if len(ten_thousand) == 2 and ten_thousand[0] == num_list[1]:
        ten_thousand = [ten_thousand[1]]

    # print(f'input : {a}, {amount_num}, len : {len(amount_num)}')
    # print(f'result : {result}, result len : {len(result)}')

    # temp = ''
    # temp = ''.join(result)
    # print(f'temp : {temp}')

    # for num_string in [unit_list[5], unit_list[9], unit_list[13]]:
    #     temp = temp.replace(num_string, num_string + ' ')

    # print(f'temp : {temp}')

###################################################################################################

    # print(trillion_num)
    # print(shillion_num)
    # print(ten_thousand)
    # print(won___number)
    temp = trillion_num + shillion_num + ten_thousand + won___number
    # print(temp)
    temp = ''.join(temp)
    # print(temp)

    for num_string in [unit_list[5], unit_list[9], unit_list[13]]:
        temp = temp.replace(num_string, num_string + ' ')

    if temp[-1] == ' ':
        result = temp[:-1] + '원'
    else:
        result = temp + '원'
    # print(f'result : {result}')

    return result


############################################################


def answer(num_to_txt, amount_lists):
    print('list_len : ', len(amount_lists))
    answer = 0

    for i, amount_list in enumerate(amount_lists):
        # print(i)
        # print('amount_list :', amount_list)
        result = num_to_txt(amount_list)
        # print('result      : ', result)
        temp = result.split(' ')
        # print('temp        : ', temp)
        temp_num = 0

        for st_num in temp:
            # print(st_num, len(st_num))
            temp_num = temp_num + len(st_num)
        # print('temp_num : ', temp_num, 'temp_len : ', len(temp))
        
        answer = answer + (temp_num * len(temp))
        # print('answer : ', answer)
        # print('\n')

    print('answer : ', answer)

answer(num_to_txt, amount_lists)


############################################################


add_str = { 3:'조 ', 7:'억 ', 11:'만 ', }
read_text = ["", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
t = ["천", "백", "십", ""]
def read_num(numstr) :
    numstr = numstr[:-1].replace(",","")
    num = int(numstr, 10)
    if not (1 <= num <= 100000000000000) :
        return "이체범위를 벗어났습니다"
    numstr = numstr.rjust(16, '0')
    kr_buf = []
    for idx, ch in enumerate(numstr) :
        n = int(ch , 10)
        if n > 0 :
            kr_buf.append( read_text[ n ] + t[ idx % 4  ] )
        if (idx in add_str) and int(numstr[idx-3:idx+1], 10) > 0 :
            kr_buf.append( add_str[idx] )
    # kr_str = "".join(kr_buf).strip() + "원"
    kr_str = "".join(kr_buf).strip().replace("일천", "천").replace("일백", "백").replace("일십", "십") + "원" # 천단위 예외 처리
    if ("십일만" not in kr_str) and ("백일만" not in kr_str) and ("천일만" not in kr_str) : # 만단위 예외 처리
        kr_str = kr_str.replace("일만", "만")
    return kr_str

# answer(read_num, amount_lists)













############################################################
############################################################
############################################################
############################################################
############################################################








# a = '999,999,999,999,999원'
# unit = {'1' : '일', '2' : '이', '3' : '삼', '4' : '사', '5' : '오', '6' : '육', '7' : '칠', '8' : '팔', '9' : '구', '0' : ''}
# unit2 = {0 : '원', 1 : '십', 2 : '백', 3 : '천', 4 : '만', 5 : '억', 6 : '조'}

# def tts(amount):
#     result = []
#     # amount_num = amount[:-1].replace(',', '')
#     amount_num = amount[:-1].split(',')

#     for i, num in enumerate(amount_num):
#         if (len(amount_num) - i) == 1: # 1~100
#             for j, separate_num in enumerate(num):
#                 if len(num) == 3: # 3자리수
#                     if separate_num == '1' and j != 2:
#                         result.append(unit2[2-j])
#                     else:
#                         result.append(unit[separate_num] + unit2[2-j])
#                 elif len(num) == 2: # 2자리수
#                     if separate_num == '1' and j != 1:
#                         result.append(unit[separate_num] + unit2[1-j])
#                     else:
#                         result.append(unit[separate_num] + unit2[1-j])
#                 elif len(num) == 1: # 1자리수
#                     result.append(unit[separate_num] + unit2[0-j])
                

#         elif (len(amount_num) - i) == 2: # 천~10만
#             temp_num = 0
#             for j, separate_num in enumerate(num):
#                 if len(num) == 3: # 3자리수
#                     if separate_num == '1' and j == 0:
#                         result.append(unit2[1])
#                         temp_num = temp_num + 1
#                     elif separate_num == '1' and j == 2:
#                         result.append(unit2[3])
#                         temp_num = temp_num + 1
#                     elif j == 0:
#                         result.append(unit[separate_num] + unit2[1 - j])
#                         temp_num = temp_num + 1
#                     else:
#                         result.append(unit[separate_num] + unit2[4 - j + temp_num])
#                 elif len(num) == 2: # 2자리수
#                     if separate_num == '1' and j != 1:
#                         result.append(unit2[4-j])
#                     else:
#                         result.append(unit[separate_num] + unit2[4-j])
#                 elif len(num) == 1: # 1자리수
#                     if separate_num == '1':
#                         result.append(unit2[3])
#                     else:
#                         result.append(unit[separate_num] + unit2[3])
                


#         # elif len(amount_num) == 3: # 100백만~1억
#         # elif len(amount_num) == 4: # 10억~천억
#         # elif len(amount_num) == 5: # 1~100조


#         # for j in num:
#         #     if j in unit:
#         #         amount_len = len(amount_num)
#         #         result.append(unit[j])

#     print(result)

# tts(a)
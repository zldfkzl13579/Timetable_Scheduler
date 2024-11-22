import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def find_common_elements(dict_list):
    result_dict = {}
    for key in dict_list[0].keys():
        nan_dict_found = False
        common_elements = set(dict_list[0][key]) if dict_list[0][key] else set()
        for dt in dict_list[1:]:
            if dt[key]:
                common_elements.intersection_update(set(dt[key]))
            else:
                nan_dict_found = True

        result_dict[key] = sorted(map(int, common_elements)) if not nan_dict_found else []
    return result_dict


def yesorno(i):
    while True:
        response = input('다음 타임테이블을 작성하시겠습니까?(y/n): ').lower()
        if response == 'y':
            print(f'{i + 1}번째 타임 테이블 작성을 시작합니다.')
            return False
        elif response == 'n':
            print('타임 테이블 작성을 종료합니다.')
            return True
        else:
            print('다시 입력해 주세요.')


def makehistplot(dict_list):
    dayslist = {key: [] for key in dict_list[0].keys()}
    all_days_data = []
    for dt in dict_list:
        for key in dt.keys():
            if dt[key]:
                dayslist[key].extend(map(int, dt[key]))
                all_days_data.extend(map(int, dt[key]))
    plt.figure(figsize=(10, 8))
    for i, (key, values) in enumerate(dayslist.items()):
        plt.subplot(4, 2, i + 1)
        plt.hist(values, bins=24, range=(0, 23), alpha=0.7, color='skyblue', edgecolor='black')
        plt.title(key)
        plt.xlabel('시간대')
        plt.ylabel('빈도수')
        plt.xticks(range(1, 24))
    plt.subplot(4, 2, 8)
    plt.hist(all_days_data, bins=24, range=(0, 23), alpha=0.7, color='skyblue', edgecolor='black')
    plt.title('모든 요일')
    plt.xlabel('시간대')
    plt.ylabel('빈도수')
    plt.xticks(range(1, 24))
    plt.tight_layout()
    plt.show()


def get_free_times_on_days(day_name):
    while True:
        daydata = input(f"{day_name}의 비어있는 시간을 입력하세요 : ")
        if not daydata:
            return []
        try:
            return sorted(map(int, set(daydata.replace(" ", "").split(','))))
        except ValueError:
            print("잘못된 입력입니다. 숫자를 콤마로 구분하여 입력하세요.")


print('----주의사항----')
print('시간은 24시간제이며, 1시간 간격으로 입력하고, 콤마로 구분하세요')
print('0에서 23까지의 정수만 입력하세요')
print('예시로 0,1,2,3,4,5,6,7,8,11,12,17,18,19,20을 입력하면,')
print('0~9시, 11~13시, 17~21시에 수업 없음을 의미합니다.')
print('만일 타임 테이블 작성중 실수로 값을 잘못 입력해 수정이 필요한 경우, 숫자가 아닌 다른 값(문자 등)을 입력하면 됩니다.')
print('----타임테이블 제작 시작----')
print('1번째 타임 테이블 작성을 시작합니다.')
timetable_all = []
i = 0
while True:
    mondata = get_free_times_on_days('월요일')
    tuedata = get_free_times_on_days('화요일')
    weddata = get_free_times_on_days('수요일')
    thudata = get_free_times_on_days('목요일')
    fridata = get_free_times_on_days('금요일')
    satdata = get_free_times_on_days('토요일')
    sundata = get_free_times_on_days('일요일')
    timetable_dict = {'월요일': mondata, '화요일': tuedata, '수요일': weddata, '목요일': thudata, '금요일': fridata, '토요일': satdata, '일요일': sundata}
    timetable_all.append(timetable_dict)
    i += 1
    if yesorno(i):
        break


result = find_common_elements(timetable_all)
print("\n공통 비어있는 시간:")
for day, times in result.items():
    print(f"{day}: {times}")
makehistplot(timetable_all)
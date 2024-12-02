import sys
import os

# 상위 디렉토리를 모듈 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# file_read 모듈 가져오기
import file_read
# input 파일을 읽기 위한 메서드 호출(param: 날짜)
lines = file_read.read_input_file("2")

answer = 0

# 전체 리스트 반복
for line in lines:
    # 한 줄에 있는 숫자를 숫자형 리스트로 변환
    num_list = [int(i) for i in line.split()]
    # num_list 길이
    len_list = len(num_list)
    
    # 증가, 감소 | 증가: True, 감소: False
    is_increasing = None

    # 리스트의 유효성을 판단
    for i in range(len_list - 1):
        diff = num_list[i+1] - num_list[i]

        # 초기 방향 설정
        if is_increasing is None:
            is_increasing = diff > 0
        else:
            # 방향이 바뀌면 중단
            if is_increasing != (diff > 0):
                break

        # 차이가 범위를 벗어나면 중단
        if not (0 < abs(diff) <= 3):
            break
    else:
        # 루프가 정상 종료된 경우에만 answer 증가
        answer += 1
        
print(answer)
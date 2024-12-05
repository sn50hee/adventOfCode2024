import sys
import os

# 상위 디렉토리를 모듈 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# file_read 모듈 가져오기
import file_read
# input 파일을 읽기 위한 메서드 호출(param: 날짜)
lines = file_read.read_input_file("5")

# 규칙 리스트와 업데이트 리스트 분리
split_index = lines.index("\n")
rules_result = lines[:split_index]
updates_result = lines[split_index + 1:]

# 규칙 리스트를 튜플 리스트로 변환
rules = [tuple(map(int, line.split('|'))) for line in rules_result]
# 업데이트 리스트를 2차원 리스트로 변환
updates = [list(map(int, line.split(','))) for line in updates_result]

# 중앙값 계산 메서드
def find_mid(update_list):
    mid_index = len(update) // 2
    return update[mid_index]

answer = 0
# 업데이트 리스트 반복
for update in updates:
    # 해당 업데이트를 딕셔너리 형태로 변환(page(key): index(value))
    positions = {page: index for index, page in enumerate(update)}
    
    # 조건에 맞는 규칙 찾기
    for p1, p2 in rules:
        if not (p1 in positions and p2 in positions):
            continue
        if positions[p1] > positions[p2]:
            break
    else:
        answer += find_mid(update)

print(answer)
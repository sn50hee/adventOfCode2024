import sys
import os

# 상위 디렉토리를 모듈 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# file_read 모듈 가져오기
import file_read
# input 파일을 읽기 위한 메서드 호출(param: 날짜)
lines = file_read.read_input_file("1")

# 왼쪽 목록 생성
left_list = [int(i.split()[0]) for i in lines]
# 오른쪽 목록 생성
right_list = [int(i.split()[1]) for i in lines]

# 정렬
left_list.sort()
right_list.sort()

# 총 거리 계산
answer = sum(abs(left - right) for left, right in zip(left_list, right_list))

print(answer)
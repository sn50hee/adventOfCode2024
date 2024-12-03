import sys
import os

# 상위 디렉토리를 모듈 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# file_read 모듈 가져오기
import file_read
# input 파일을 읽기 위한 메서드 호출(param: 날짜)
lines = file_read.read_input_file("3")

# 정규식 사용을 위하여 re 모듈 import
import re

mul_list = []
answer = 0
# mul(숫자,숫자) 형식 패턴 지정
pattern = r"mul\(\d+,\d+\)"

# input 파일 반복
for line in lines:
    # mul_list에 패턴과 일치하는 문자열 추가
    mul_list.extend(re.findall(pattern, line))

for mul in mul_list:
    # 숫자를 찾아 리스트에 저장
    num_list = re.findall(r"\d+", mul)
    # 숫자1 * 숫자2를 정답에 더하기
    answer += int(num_list[0]) * int(num_list[1])
print(answer)
import sys
import os

# 상위 디렉토리를 모듈 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# file_read 모듈 가져오기
import file_read
# input 파일을 읽기 위한 메서드 호출(param: 날짜)
lines = file_read.read_input_file("4")

# 찾을 문자열
xmas = "XMAS"
# 세로 크기
rows_count = len(lines)
# 가로 크기
cols_count = len(lines[0])

# 방향 (dx, dy)
directions = [
    (0, 1),   # 오른쪽
    (0, -1),  # 왼쪽
    (1, 0),   # 아래
    (-1, 0),  # 위
    (1, 1),   # 대각선 오른쪽 아래
    (-1, -1), # 대각선 왼쪽 위
    (1, -1),  # 대각선 왼쪽 아래
    (-1, 1)   # 대각선 오른쪽 위
]

answer = 0

# 세로 탐색(y축 좌표)
for r in range(rows_count):
    # 가로 탐색(x축 좌표)
    for c in range(cols_count):
        # 탐색 방향
        for dx, dy in directions:
            # XMAS 찾기
            for i in range(4):
                # 현재 탐색 위치
                nr = r + i*dx
                nc = c + i*dy
                # 현재 위치가 좌표를 벗어나거나 문자와 맞지 않으면 해당 좌표 탐색 종료
                if nr < 0 or nr >= rows_count or nc < 0 or nc >= cols_count or lines[nr][nc] != xmas[i]:
                    break
            # 반복문이 정상적으로 종료됐으면 1 추가
            else:
                answer += 1

print(answer)
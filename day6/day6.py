import sys
import os

# 상위 디렉토리를 모듈 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# file_read 모듈 가져오기
import file_read
# input 파일을 읽기 위한 메서드 호출(param: 날짜)
lines = file_read.read_input_file("6")

# 세로 크기
rows_count = len(lines)
# 가로 크기
cols_count = len(lines[0])

# 방향에 따른 이동 좌표
directions = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}
# 방향 순서: 오른쪽으로 90도 회전
turn_order = ['^', '>', 'v', '<']

guard_pos, guard_dir = None, None
# 경비원의 위치와 방향 탐색
for r in range(rows_count):
    for c in range(cols_count):
        if lines[r][c] in directions:
            # 위치
            guard_pos = (r, c)
            # 방향
            guard_dir = lines[r][c]
            break
        
# 방문한 위치 집합
visited = set()
visited.add(guard_pos)

# 좌표를 벗어날 때까지 반복
while 0 <= guard_pos[0] < rows_count and 0 <= guard_pos[1] < cols_count:
    # 현재 위치와 방향
    r, c = guard_pos
    dr, dc = directions[guard_dir]
    
    # 이동할 위치
    nr, nc = r + dr, c + dc
    # 이동 가능
    if 0 <= nr < rows_count and 0 <= nc < cols_count and lines[nr][nc] != '#':
        guard_pos = (nr, nc)
        visited.add(guard_pos)
    # 이동 불가하면 오른쪽으로 회전
    elif 0 <= nr < rows_count and 0 <= nc < cols_count and lines[nr][nc] == '#':
        current_index = turn_order.index(guard_dir)
        guard_dir = turn_order[(current_index + 1) % 4]
    else:
        guard_pos = (nr, nc)

# 결과 출력
print(len(visited))
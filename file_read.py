import os

# input_file: 날짜
def read_input_file(input_file):
    # 현재 파일의 디렉토리 경로 정보 저장
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # "디렉토리 경로\day1_input" 형식의 문자열 생성(input.txt 파일과 py 파일이 같은 디렉토리에 존재해야 함)
    filename = os.path.join(current_dir, f'day{input_file}',f'day{input_file}_input.txt')
    # 파일 오픈
    f = open(filename, 'r')
    # 파일을 읽고 리스트에 저장
    lines = f.readlines()
    # 파일 닫기
    f.close()
    return lines
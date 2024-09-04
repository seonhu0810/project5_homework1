from configparser import ConfigParser

def read_config(filename='app.ini', section='mysql'):
    # INI 파일 파싱을 처리할 ConfigParser 객체를 생성
    config = ConfigParser()

    # 지정된 INI 설정 파일을 읽어옴
    config.read(filename)

    # 설정 데이터를 저장할 빈 딕셔너리를 초기화
    data = {}

    # 지정된 섹션이 INI 파일에 존재하는지 확인
    if config.has_section(section):
        # 지정된 섹션 내의 모든 키-값 쌍을 가져옴
        items = config.items(section)

        # 키-값 쌍을 딕셔너리에 추가
        for item in items:
            data[item[0]] = item[1]
    else:
        # 지정된 섹션을 찾을 수 없으면 예외 발생
        raise Exception(f'{section} 섹션이 {filename} 파일에 존재하지 않습니다')
    
    # 설정 데이터가 담긴 딕셔너리를 반환
    return data

if __name__ == '__main__':
    # 기본 섹션('mysql')의 설정을 'app.ini' 파일에서 읽어옵니다
    config = read_config()

    # 얻어진 설정을 출력
    print(config)
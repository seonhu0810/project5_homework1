from mysql.connector import MySQLConnection, Error
from config import read_config

def connect(config):
    """ MySQL 데이터베이스에 연결"""
    conn = None
    try:
        print('MySQL 데이터베이스에 연결 중...')
        conn = MySQLConnection(**config)
        
        if conn.is_connected():
            print('연결이 성공적으로 이루어졌습니다.')
        else:
            print('연결이 실패했습니다.')

    except Error as error:
        # 연결 중 오류가 발생하면 오류 메시지를 출력
        print(error)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            # 연결을 닫고 종료 메시지를 출력
            print('연결이 종료되었습니다.')

if __name__ == '__main__':
    # 설정 파일에서 설정을 읽어옴
    config = read_config()
    # 읽어온 설정을 사용하여 데이터베이스에 연결
    connect(config)
from mysql.connector import MySQLConnection, Error
from config import read_config

def query_with_fetchone(config):
    # 커서와 연결 변수 초기화
    cursor = None
    conn = None

    try:
        # 제공된 설정을 사용하여 MySQL 데이터베이스에 연결
        conn = MySQLConnection(**config)
        
        # 데이터베이스와 상호작용할 커서를 생성
        cursor = conn.cursor()
        
        # 'books' 테이블에서 모든 행을 가져오는 SELECT 쿼리를 실행
        cursor.execute("SELECT * FROM books")

        # 첫 번째 행을 가져옴
        row = cursor.fetchone()

        # 모든 행을 순회하며 출력
        while row is not None:
            print(row)
            row = cursor.fetchone()

    except Error as e:
        # 쿼리 실행 중 오류가 발생하면 오류 메시지를 출력
        print(e)

    finally:
        # 커서와 연결을 'finally' 블록에서 닫음
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    # 'config' 모듈에서 데이터베이스 설정을 읽어옴
    config = read_config()
    
    # 얻은 설정을 사용하여 쿼리 실행 
    query_with_fetchone(config)


from mysql.connector import MySQLConnection, Error
from config import read_config

def query_with_fetchall():
    try:
        # 데이터베이스 설정을 읽어옴
        config = read_config()
        
        # 제공된 설정을 사용하여 MySQL 데이터베이스에 연결
        conn = MySQLConnection(**config)
        
        # 데이터베이스와 상호작용할 커서를 생성합니다
        cursor = conn.cursor()
        
        # 'books' 테이블에서 모든 행을 조회하는 SELECT 쿼리를 실행
        cursor.execute("SELECT * FROM books")
        
        # 결과 집합에서 모든 행을 가져옴
        rows = cursor.fetchall()

        # 쿼리에서 반환된 총 행의 수를 출력
        print('Total Row(s):', cursor.rowcount)
        
        # 모든 행을 순회하며 출력
        for row in rows:
            print(row)
        return rows

    except Error as e:
        # 쿼리 실행 중 오류가 발생하면 오류 메시지를 출력
        print(e)

    finally:
        # 커서와 연결을 'finally' 블록에서 닫아 이를 보장
        cursor.close()
        conn.close()

if __name__ == '__main__':
    # 조회 쿼리를 실행할 때 설정을 직접 읽어옴
    query_with_fetchall()

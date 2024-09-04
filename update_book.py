from mysql.connector import MySQLConnection, Error
from config import read_config

def update_book(book_id, title):
    # 데이터베이스 설정을 읽어옴
    config = read_config()

    # 쿼리와 데이터를 준비
    query = """ UPDATE books
                SET title = %s
                WHERE id = %s """

    data = (title, book_id)

    affected_rows = 0  # 영향을 받은 행의 수를 저장할 변수를 초기화

    try:
        # 데이터베이스에 연결
        with MySQLConnection(**config) as conn:
            # 책 제목을 업데이트
            with conn.cursor() as cursor:
                cursor.execute(query, data)

                # 영향을 받은 행의 수를 가져옴
                affected_rows = cursor.rowcount

            # 변경 사항을 커밋
            conn.commit()

    except Error as error:
        # 오류가 발생하면 오류 메시지를 출력
        print(error)

    return affected_rows  # 영향을 받은 행의 수를 반환

if __name__ == '__main__':
    # '37'번 ID를 가진 책의 제목을 'The Giant on the Hill *** TEST ***'로 업데이트
    affected_rows = update_book(37, 'The Giant on the Hill *** TEST ***')
    print(f'영향을 받은 행의 수: {affected_rows}')

import mysql.connector

# 데이터베이스 연결을 저장할 변수 초기화
conn = None

try:
    # MySQL 데이터베이스에 연결 시도
    conn = mysql.connector.connect(host='localhost', 
                                   port=3306,
                                   database='pub',
                                   user='<user>',
                                   password='<password>')
    
    # 연결이 성공적으로 이루어졌는지 확인
    if conn.is_connected():
        print('MySQL 데이터베이스에 연결되었습니다')

except mysql.connector.Error as e:
    # 연결 오류가 발생하면 오류 메시지를 출력
    print(e)

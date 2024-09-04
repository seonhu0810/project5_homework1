from flask import Flask, render_template, redirect
from fetchall import query_with_fetchall
from insertData import insert_book
from updateData import update_book
from deleteData import delete_book

app = Flask(__name__)

@app.route('/')
def index():
    # 데이터베이스에서 모든 데이터를 가져와서 'list.html' 템플릿에 전달
    datas = query_with_fetchall()
    return render_template('list.html', datas=datas)

@app.route('/insert/<title>/<isbn>')
def insert(title, isbn):
    # 주어진 제목과 ISBN으로 책을 데이터베이스에 삽입
    insert_book(title, isbn)
    # 삽입 후 홈 페이지로 리다이렉트
    return redirect('/')

@app.route('/update/<int:id>/<title>')
def update(id, title):
    # 주어진 ID를 가진 책의 제목을 업데이트
    affected_rows = update_book(id, title)
    # 업데이트된 행의 수를 출력
    print(f'영향을 받은 행의 수: {affected_rows}')
    # 업데이트 후 홈 페이지로 리다이렉트
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    # 주어진 ID를 가진 책을 삭제
    affected_rows = delete_book(id)
    # 삭제된 행의 수를 출력
    print(f'영향을 받은 행의 수: {affected_rows}')
    # 삭제 후 홈 페이지로 리다이렉트
    return redirect('/')

if __name__ == '__main__':
    # 디버깅 모드로 Flask 애플리케이션을 실행
    app.run(debug=True)

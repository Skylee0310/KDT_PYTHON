# Application Factory 기반의 Flask Server 구동

# 모듈 로딩
from flask import Flask, render_template, url_for
from .views import data_view

# Application Factory 기반의 함수 정의 
# 함수명 : create_app() : 변경 불가
# 반환값 : Flask Server 인스턴스
def create_app() :
    # Flask Server 인스턴스 생성
    app = Flask(__name__)

    # Blueprint 인스턴스 등록 : 블루프린트 = 서브 카테고리의 페이지 라우팅 기능(유사한 페이지를 묶어놓고 라우팅 하는 역할)
    app.register_blueprint(data_view.data_BP)


    with app.test_request_context():
        print(url_for('static', filename='css/style_1.css'))
        print(url_for('static', filename='css/popcorn.png'))

    # Flask Server 인스턴스 반환
    return app 



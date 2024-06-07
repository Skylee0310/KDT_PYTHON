# 모듈 로딩
from flask import Flask,render_template, Blueprint


# 애플리케이션 팩토리 함수
def create_app() :
    myapp = Flask(__name__)

    # bp 등록
    from .views import main_views
    myapp.register_blueprint(blueprint=main_views.bp)

    return myapp



# ## 전역 변수
# myapp = Flask(__name__) # 인스턴스 생성

# ## 사용자 요청 URL 처리 기능 = 라우팅(Routing)
# ## 형식 : @Flask_instance_name.route('url string')

# # 웹 서버의 첫 페이지 : http://127.0.0.1:5000/
# @myapp.route("/") #http://127.0.0.1:5000는 생략.

# def index_page() :
# #    return "<h3><font color='skyblue'>My Web Index Page</font></h3>" # 헤더 안 써도 됨.
#     return render_template('tem.html')
# # 사용자별 페이지 반환
# # 사용자 페이지 URL : http://127.0.0.1:5000/<username>

# @myapp.route("/<name>") # 홑화살표 괄호가 없으면 변하는 값이아닌 username이 된다.
# def username(name) :
#     return f"username : {name}"

# @myapp.route("/<int:number>")
# def show_number(number) :
#     return f"Select Number : {number}"

# @myapp.route("/hello") 
# def hello() :
#     return f"hello"
# @myapp.route('/user_info')
# def user_login2() :
#     return myapp.redirect('/') # 첫페이지로 돌아가기



# ## 실행 제어 --> 조건에 따른 실행 처리
# if __name__ == '__main__' : # 임포트 되는 게 아닐 때
#     # Flask 웹 서버 구동   
#     myapp.run(debug=True) # 서버 구동
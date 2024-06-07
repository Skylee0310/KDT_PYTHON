# 데이터 저장 및 출력 관련 웹 페이지 라이팅.
# url : /input + @
#       /input/save
#       /input/delete # 기능에 따라 쓸 수 있음..
#       /input/update # 기능에 따라 쓸 수 있음..
#-----------------------------------------------------------------------------------------------------------------

from flask import Blueprint, render_template, request

# BP 인스턴스 생성
data_BP = Blueprint('data', __name__, template_folder='templates', url_prefix='/input')

#라우팅 함수들
@data_BP.route('/')
# http://127.0.0.1:5000/input/
def input_data() :
    return render_template(template_name_or_list='input_data.html', 
                           action="/input/save",
                           method="POST")


#GET 방식으로 데이터 저장 처리 함수
# 사용자의 요청 즉, REQUEST 객체에 데이터 저장

@data_BP.route('/save_get')
# http://127.0.0.1:5000/input/save_get
def save_get_data() :
    # 요청 데이터 추출
    req_dict = request.args.to_dict()
    v = req_dict.get('value')
    m = req_dict.get('message')
    #return f"save get data :{{req_dict}}"
    return render_template(template_name_or_list='save_data.html', **req_dict)

#POST 방식으로 데이터 저장 처리 함수
@data_BP.route('/save_get', methods=['GET', 'POST'])
# http://127.0.0.1:5000/input/save_post
def post_data() :
        # 요청 데이터 추출
    # req_dict = request.args.to_dict()/
    method = request.method
    headers = request.headers
    args = request.args.to_dict()
    v = request.form['value']
    m = request.form['message']
    return f"SAVE POST DATA =><br><br> METHOD : {method} <br><br> HEADERS : {headers} <br><br> ARGS :{args} <br>VALUE : {v}<br>MSG : {m}"


#GET 방식으로 데이터 저장 처리 함수
@data_BP.route('/save', methods=['GET', 'POST'])
#http://127.0.0.1:5000/input/save

def save_data() :
    method = request.method
    headers = request.headers
    if (request.method == 'GET') : 
        req_dict = request.args.to_dict()
        return render_template(template_name_or_list='save_data.html', **req_dict)
    
    elif (request.method == 'POST') :
        v = request.form['value']
        m = request.form['message']
        args = request.args.to_dict()
        return f"SAVE POST DATA =><br><br> METHOD : {method} <br><br> HEADERS : {headers} <br><br> ARGS :{args} <br>VALUE : {v}<br>MSG : {m}"
    

#GET, POST 요청 차이점
''' GET, POST 요청 시 url 형태, data {} 담기는 형태의 차이가 있다.

GET 요청 url에섯 key:value 값이 담기는 데 반해, POST 요청 시 /join 등의 url 형태이다.
그리고 GET 요청 시 data: {} 비어있는데 반해, POST 요청 시 data: {key:'value'} 담긴다.
출처: https://jjungslife.tistory.com/57 [Jann's World:티스토리]'''
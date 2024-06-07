# -----------------------------------------------------------------------------
# 역할 : 데이터 저장 및 출력 관련 웹 페이지 라우팅 처리 
# URL : /input
#       /input/save
#       /input/delete
#       /input/update
# -----------------------------------------------------------------------------

# 모듈 로딩 
from flask import Blueprint, render_template

# BP 인스턴스 생성
data_BP = Blueprint('data', 
                    __name__, 
                    template_folder = 'templates', 
                    url_prefix='/input/') 

# 라우팅
@data_BP.route('')
def input_data():
    pass 

# get 방식으로 데이터 저장 처리 함수
@data_BP.route('save_get')
def save_get_data():
    return render_template(input_data.html)

# post 방식으로 데이터 저장 처리 함수
@data_BP.route('save_post')
def save_post_data():
    return 'save get data'
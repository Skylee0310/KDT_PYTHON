from flask import Blueprint, render_template, request
from YouWEB.model import Question

bp = Blueprint('main',
               __name__,
               template_folder='templates',
               url_prefix = '/')


## 라우팅 함수들
@bp.route('/')
def index() : 
    # Question 테이블에 저장된 데이터 읽어서 출력 
    question_list = Question.query.order_by(Question.create_date.desc())

    # return f"<h3> HI HI </h3> {question_list}"
    return render_template('q_list.html', question_list = question_list)

@bp.route('/question/create')
def create_question() :
    return render_template(template_name_or_list='q_create.html', action = '/new_q_list')

@bp.route('/new_q_list', methods=["POST"])
def get_question() :
    title = request.form['title']
    content = request.form['content']
    if request.method == 'POST' :
        return f"title : {title} content : {content}"

# @bp.route('/detail/<int:question_id>/')
# def detail(question_id):
#     question = Question.query.get(question_id)
#     return render_template('question/question_detail.html', question = question)
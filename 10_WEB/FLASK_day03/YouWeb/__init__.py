# 모듈 로딩
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# DB관련 인스턴스 생성
db= SQLAlchemy()
migrate = Migrate()

# Application Factory 함수
def create_app() :

    # flask Server 인스턴스 생성
    app = Flask(__name__)

    # print(f'__name__ : {__name__}')
    # app.config.from_object(config)

    # 설정 내용 로딩
    app.config.from_pyfile('config.py')

    # ORM 즉, DB 초기화
    db.init_app(app)
    migrate.init_app(app=app, db=db)

    # 테이블 클래스
    from . import model

    # 블루프린트
    from .views import main_views
    app.register_blueprint(main_views.bp)
    
    # flask Server 인스턴스 반환
    return app


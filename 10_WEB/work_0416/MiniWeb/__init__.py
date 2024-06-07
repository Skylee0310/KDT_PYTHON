from flask import Flask,render_template, Blueprint


# 애플리케이션 팩토리 함수
def create_app() :
    app = Flask(__name__)
    
    # bp 등록
    from .view import main_views
    app.register_blueprint(blueprint=main_views.bp)

    return app
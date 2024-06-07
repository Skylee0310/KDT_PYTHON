from flask import Flask

def create_app() : #create_app 함수가 app 객체를 생성해 반환.
   
   # Flask Server 인스턴스 생성
    app = Flask(__name__)
    
    from .views import main_views
    app.register_blueprint(main_views.bp)
    
    # Flask Server 인스턴스 반환
    return app
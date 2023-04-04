from flask import Flask

app = Flask(__name__)  #플라스크 객체 생성 / __name__ 현재 실행 중인 모듈 이름을 전달하는 것 

@app.route('/')
def home():
    return "home page app" 
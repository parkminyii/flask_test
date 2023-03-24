'''
    - GET 방식으로 데이터 전송하기
        - 클라이언트 (Json, Xml, Text, Form,(키=값&키=값...), Form_encode, Graphal, Binary)
            - form 전송, 화면 껌벅 => 화면 전환, Form, Form_encode
                <form action=""http://127.0.0.1:5000/link" method="get">
                    <input name="name" value="hello"/> 
                    <input name="age" value="100"/> 
                    <input type="submit" value="전송"/>
                </form>
            - ajax 가능 (jQuery로 표현), 화면은 현재 화면 유지 
                - (Json, Xml, Text, Form,(키=값&키=값...), Form_encode, Graphal, Binary)
                $.post({
                    url:"http://127.0.0.1:5000/link",
                    data:"name=hello&age=100",
                    success:(res)=>{},
                    error:(err)=>{}
                })
        - 서버 
            - get 방식 데이터 추출
            - name = request.form.get('name')
            - age = request.form.get('age')

    - /link쪽으로 요청하는 방식은 다양할 수 있다. 단, 사이트 설계상 1가지로만 정의되어 있다면
      다른 방식의 접근은 모두 비정상적인 접근이다(웹 크롤링, 스크래핑, 해킹 등이 대상)
      이런 접근을 필터링할 것인가? 보안의 기본 사항 
'''
from flask import Flask, render_template, jsonify, request, redirect, url_for
from d4 import select_login # 모듈가져오기 
app = Flask(__name__)

# @app.route() => 기본적으로 GET 방식
# 메소드 추가는 => methods=['POST', ...]
@app.route('/login', methods=['POST', 'GET'])
def login():
    # method별 분기
    if request.method == 'GET':
        return render_template('login.html')
    else: # POST
        # request.form['uid'] # 값이 누락되면 서버 셧다운됨, 사용 금지 
        # 1. 로그인 정보 획득 
        uid = request.form.get('uid')
        upw = request.form.get('upw') # 암호는 차후에 암호화 해야 한다 (관리자도 볼 수 없다. 해싱)
        print( uid, upw )
        # 2. 회원 여부 쿼리
        result = select_login(uid, upw)
        if result: # 3. 회원이면
            # 3-1. 세션 생성, 기타 필요한 조치 수행
            # 3-2. 서비스 메인 화면으로 이동
            pass
        else:      # 4. 회원 아니면
            # 4-1. 적당한 메세지 후, 다시 로그인 유도 
            return render_template('error.html')
            pass
        #return redirect('https://www.naver.com') # 요청을 다른 URL로 포워딩한다 

if __name__ == "__main__":
    app.run(debug=True)
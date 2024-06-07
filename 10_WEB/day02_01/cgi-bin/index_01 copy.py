#모듈 로딩
import cgi

# client 요청 데이터 즉, Grom 데이터 저장 인스턴스 
form = cgi.FieldStorage()

### 데이터 추출
if 'data' in form and 'no' in form:
    result = form.getvalue('data') + ' - ' + form.getvalue('no')
else :
    result="No data"

# Web 브라우저 화면 출력 코드
def print_browser(result=""):
    # HTML 파일 읽기 -> body 문자열
    filename = '../html/test.html'
    with open(file=filename, mode = 'r', encoding='utf-8') as f :

        # HTML Header
        print('content-Type : text/html')
        print() # header와 body 구분 - 없으면 출력 불가능

        print('<form><input type = "text" name = "data" placeholder="data"><br>')
        print('<form><input type = "number" name = "no" placeholder="no"><br>')
        print('<input type = "submit"></form></body></html>')

        # HTML Body
        print(f"Hello CGI ^^ Form : {result}")
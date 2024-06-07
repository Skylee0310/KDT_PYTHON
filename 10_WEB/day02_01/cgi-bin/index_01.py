#모듈 로딩
import cgi, sys, codecs

# 
sys.stdout=codecs.getwriter('utf-8')(sys.stdout.detach())


# Web 브라우저 화면 출력 코드
def print_browser(result=""):
    # HTML 파일 읽기 -> body 문자열
    filename = './html/test.html'
    with open(file=filename, mode = 'r', encoding='utf-8') as f :

        # HTML Header
        print('content-Type : text/html; charset=utf-8')
        print() # header와 body 구분 - 없으면 출력 불가능

        # HTML Body
        print(f.read().format(result))

# 요청 처리 및 브라우징
# client 요청 데이터 즉, Grom 데이터 저장 인스턴스 
form = cgi.FieldStorage()

### 데이터 추출
if 'data' in form:
    result = form.getvalue('data') #form['data']
else :
    result="No data"
    
print_browser(result)
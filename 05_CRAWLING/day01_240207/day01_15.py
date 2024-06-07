from bs4 import BeautifulSoup

tr = '''
<table>
    <tr class = "passed a b c" id = "row1 example"><td>t1</td></tr>
    <tr class = "failed" id = "row2"><td>t2</td></tr>
</table>
'''


# find_all() 함수 : 검색된 모든 태그를 list 형태로 리턴
table = BeautifulSoup(tr, 'html.parser')
for row in table.find_all('tr') :
    print(row.attrs)
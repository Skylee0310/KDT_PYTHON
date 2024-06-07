import cgi, sys, codecs
import pandas as pd

# 
sys.stdout=codecs.getwriter('utf-8')(sys.stdout.detach())

# 웹브라우저 화면 출력 코드
try:
    def print_browser(result="") :
        # HTML 파일 읽기 -> body 문자열
        filename = './html/index.html'
        with open(file=filename, mode="r", encoding="utf-8") as f :

            # HTML Header
            print('content-Type : text/html')
            print() # header와 body 구분 - 없으면 출력 불가능

            # print('<form><input type = "text" name = "data" placeholder="data"><br>')
            # print('<input type = "submit"></form></body></html>')

            # HTML Body
            print('...')
            print(f.read().format(result))
            print('...')

    # 결과 예측에 넣을 텍스트 토큰화 하는 함수
    def tokentext(text, df, vocaDF) : 
        # text :입력할 가사. df : 가사 df / vocaDF : 단어사전df
        from konlpy.tag import Kkma
        kkma = Kkma()
        texttoken = kkma.morphs(text)

        # 어휘사전
        vocab_dict = {word: idx for idx, word in enumerate(vocaDF['0'].to_list())}
        encoded = [vocab_dict[token] for token in texttoken if token in vocab_dict]
        # 인코딩 결과 출력
        print("토큰화된 단어들:", texttoken)
        print("인코딩 결과:", encoded)
        padded_id=[]
        max_length = df.shape[1]

        if len(encoded) < max_length :
            padded_id.append(encoded + [0]*(max_length-len(encoded)))
        else :
            padded_id.append(encoded)
        return padded_id[0]
        
    # 결과 예측 함수
    def predict(model, text):
        import torch
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        with torch.no_grad():
            text = torch.tensor((text), dtype=torch.int64).to(device)
            text = text.unsqueeze(0)
            offsets = torch.tensor([0]).to(device)
            predicted_label = model(text)
            result = predicted_label.argmax(1).item()
            if result == 0: genre='ballad'
            elif result == 1 : genre='dance'
            elif result == 2 : genre='fork'
            elif result == 3 : genre='hiphop'
            elif result == 4 : genre='indi'
            elif result == 5 : genre='R&B'
            elif result == 6 : genre='rock'
            elif result == 7 : genre='trot'
            return genre

    import torch.nn as nn

    class LSTM(nn.Module):
        def __init__(self, vocab_size, input_size, hidden_size, num_layers, dropout, output_size):
            super(LSTM, self).__init__()
            self.embedding = nn.Embedding(vocab_size, input_size)
            self.hidden_size = hidden_size
            self.num_layers = num_layers
            self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, dropout=dropout)
            self.fc = nn.Linear(hidden_size, output_size)
            self.init_weights()
        
        def init_weights(self):
            initrange = 0.5
            self.fc.weight.data.uniform_(-initrange, initrange)
            self.fc.bias.data.zero_()

        def forward(self, text):
            embedded = self.embedding(text)
            out, _ = self.lstm(embedded)
            out = self.fc(out[:, -1, :])
            return out
    #=================================================================================
    #(1) 학습 데이터 읽기
    import os, torch, joblib

    mdl = './model/model.pth'
    #mdl = joblib.load(pklfile)

    #=================================================================================
    #(2) 웹 페이지 <form> -> <input> 리스트 가져오기
    form = cgi.FieldStorage()
    # text = form["text"] # 문제
    # ballad = form.getvalue('ballad')
    # dance = form.getvalue('dance')
    # fork = form.getvalue('fork')
    # hiphop = form.getvalue('hiphop')
    # indi = form.getvalue('indi')
    # rnb = form.getvalue('R&B')
    # rock = form.getvalue('rock')
    # trot = form.getvalue('trot')
    #==================================================================================

    #(3) 판정하기
    import pandas as pd
    #from model import LSTM
    import torch.nn as nn


    text = '아름다운 청춘의 한 장 함께 써내려 가자 너와의 추억들로 가득 채울래 (come on!) 아무 걱정도 하지는 마, 나에게 다 맡겨 봐 지금 이 순간이 다시 넘겨볼 수 있는 한 페이지가 될 수 있게.'
    encoded = '../model/encoded.csv'
    vocab = '../model/vocab.csv'
    df = pd.read_csv('encoded.csv')
    vocab = pd.read_csv('vocab.csv')
    mdl = LSTM()

    if 'text' in form :
        token = tokentext(text, df, vocab)
        genre = predict(mdl, token)
        result = f'이 가사의 장르는 {genre}입니다.'
    else :
        result = '가사의 장르를 알 수 없습니다.'
    #==================================================================================
    print('.')
    print_browser(result=result)
except Exception as e:
    print(e)
    # print('.....')




# python -m http.server 8080 --bind 127.0.0.1 --cgi
'''
1. 주어진 데이터의 공분산을 계산하세요.
2. 주어진 데이터의 상관계수를 계산하세요.
3. 각 특성별로 히스토그램을 그려보세요.
4. 각 품종별로 특성(꽃받침 길이, 꽃받침 너비, 꽃잎 길이, 꽃잎 너비)에 대한 상자 그림을 그려보세요.
5. 각 품종별로 꽃받침 길이와 꽃받침 너비의 관계를 산점도로 나타내고 색상으로 품종을 구분하세요.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = 'iris.csv'
iris_df = pd.read_csv(file)
setosa_df = iris_df.groupby('variety').get_group('Setosa')
versicolor_df = iris_df.groupby('variety').get_group('Versicolor')
virginica_df = iris_df.groupby('variety').get_group('Virginica')

#print(setosa_df)
'''
[데이터 정보] 
sepal.length = 꽃받침 길이
sepal.width = 꽃받침 너비
petal.length = 꽃잎 길이
petal.width = 꽃잎 너비
variety = 품종
'''
def draw_hist(x, title, xlabel, ylabel, a, b) :
    # a = x눈금 범위
    # b = x눈금 step
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    freq, _, _ = ax.hist(x, bins=30)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks(np.linspace(0, a, b))
    plt.show()

def draw_box(x, sub, label, fig1) :
    ax = fig1.add_subplot(sub)
    ax.boxplot(x, labels=[label])

def draw_scatter(subplot, x, y, title, color, xlabel, ylabel, fig) :
    ax = fig.add_subplot(subplot)
    #산점도 그리기
    ax.set_title(title)
    ax.scatter(x, y, c = color)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)


sepal_length = iris_df['sepal.length']
sepal_width = iris_df['sepal.width']
petal_length = iris_df['petal.length']
petal_width = iris_df['petal.width']
print(petal_length)

# 품종별 꽃받침 길이
setosa_sepal_length = setosa_df['sepal.length']
versicolor_sepal_length = versicolor_df['sepal.length']
virginica_sepal_length = virginica_df['sepal.length']

# 품종별 꽃받침 너비
setosa_sepal_width = setosa_df['sepal.width']
versicolor_sepal_width = versicolor_df['sepal.width']
virginica_sepal_width = virginica_df['sepal.width']

# 품종별 꽃잎 길이
setosa_petal_length = setosa_df['petal.length']
versicolor_petal_length = versicolor_df['petal.length']
virginica_petal_length = virginica_df['petal.length']

# 품종별 꽃잎 너비
setosa_petal_width = setosa_df['petal.width']
versicolor_petal_width = versicolor_df['petal.width']
virginica_petal_width = virginica_df['petal.width']



#꽃받침 길이 - 꽃받침 너비 공분산
cov_sepal = np.cov(sepal_length, sepal_width)
print('꽃받침 길이 - 너비 공분산 : ', cov_sepal[0,1])

#꽃잎 길이 - 꽃잎 너비 공분산
cov_petal = np.cov(petal_length, petal_width)
print('꽃잎 길이 - 너비 공분산 : ', cov_petal[0,1])
print('')

# 꽃받침 길이 - 너비 상관계수
corr_sepal = (cov_sepal[0,1])/(np.std(sepal_length)*np.std(sepal_width))
corr_sepal = round(corr_sepal, 3)
print('꽃받침 길이-너비 상관계수 :', corr_sepal)

# 꽃잎 길이 - 너비 상관계수
corr_petal = (cov_petal[0,1])/(np.std(petal_length)*np.std(petal_width))
corr_petal = round(corr_petal, 3)
print('꽃잎 길이-너비 상관계수 :',corr_petal)
print()

# 꽃받침 길이 도수분포표 그래프 출력
draw_hist(sepal_length, 'sepal length', 'length of sepal', 'number of iris', max(sepal_length), 12)

# 꽃받침 너비 도수분포표 그래프 출력
draw_hist(sepal_width, 'sepal width', 'width of sepal', 'number of iris', max(sepal_width), 12)

# 꽃잎 길이 도수분포표 그래프 출력.
# freq_class_petal_length = [i*0.5 for i in range(0, 14)]
draw_hist(petal_length, 'petal length', 'length of petal', 'number of iris', max(petal_length), 12)

# 꽃잎 너비 도수분포표 그래프 출력
draw_hist(petal_width, '[petal width]', 'width of petal', 'number of iris', max(petal_width), 12)


# # 꽃받침 길이 상자그림
fig1 = plt.figure(figsize=(9,6))
draw_box(setosa_sepal_length, 131, 'setosa_sepal_length', fig1)
draw_box(versicolor_sepal_length, 132, 'versicolor_sepal_length', fig1)
draw_box(virginica_sepal_length, 133, 'virginica_sepal_length', fig1)
plt.show()

# # 꽃받침 너비 상자그림
fig2 = plt.figure(figsize=(9,6))
draw_box(setosa_sepal_width, 131, 'setosa_sepal_width', fig2)
draw_box(versicolor_sepal_width, 132, 'versicolor_sepal_width', fig2)
draw_box(virginica_sepal_width, 133, 'virginica_sepal_width', fig2)
plt.show()

# 꽃잎 길이 상자그림
fig3 = plt.figure(figsize=(9,6))
draw_box(setosa_petal_length, 131, 'sentosa_petal_length', fig3)
draw_box(versicolor_petal_length, 132, 'versicolor_petal_length', fig3)
draw_box(virginica_petal_length, 133, 'virginica_petal_length', fig3)
plt.show()

# 꽃잎 너비 상자그림
fig4 = plt.figure(figsize=(9,6))
draw_box(setosa_petal_width, 131, 'sentosa_petal_width', fig4)
draw_box(versicolor_petal_width, 132, 'versicolor_petal_width', fig4)
draw_box(virginica_petal_width, 133, 'virginica_petal_width', fig4)
plt.show()

fig = plt.figure(figsize=(60, 10))

draw_scatter(131, setosa_sepal_length, setosa_sepal_width, 'setosa', 'tomato', 'sepal_length', 'sepal_width', fig)
draw_scatter(132, virginica_sepal_length, virginica_sepal_width, 'virginica', 'black', 'virginica_length', 'virginica_width', fig)
draw_scatter(133, versicolor_sepal_length, versicolor_sepal_width, 'versicolor', 'royalblue', 'versicolor_length', 'versicolor_width', fig)
plt.show()
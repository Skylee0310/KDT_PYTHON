'''
문제 1 :
1-1) 데이터셋을 불러오고, 데이터프레임으로 변환한 후 첫 5개 행을 출력하시오.
1-2) 데이터프레임의 기본 정보를 확인하고 각 열의 데이터 타입을 제시하시오
1-3) 붓꽃의 품종에 대한 클래스 분포를 확인하고 각 클래스별 데이터의 개수를 제시하시오.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

iris_df = pd.read_csv('iris.csv')

print('문제 1.')
print('[iris_df 첫 5개 행 출력]', '\n', iris_df.head(5))
print()
'''
[데이터 정보] 
sepal.length = 꽃받침 길이
sepal.width = 꽃받침 너비
petal.length = 꽃잎 길이
petal.width = 꽃잎 너비
variety = 품종
'''
print('[iris_df 기본 정보 확인]')
iris_df.info()
print('')

setosa_df = iris_df.groupby('variety').get_group('Setosa')
versicolor_df = iris_df.groupby('variety').get_group('Versicolor')
virginica_df = iris_df.groupby('variety').get_group('Virginica')

print('[iris_df의 품종 클래스 분포, 각 클래스별 데이터 개수 제시]')
print('붓꽃의 품종에 대한 클래스 분포 :?')
print('1) setosa 개수 : ', setosa_df.shape[0])
print('2) versicolor 개수 : ', versicolor_df.shape[0])
print('3) virginica 개수 : ', virginica_df.shape[0])
print('='*80)
print()

'''
문제 2 :
2-1) 붓꽃 데이터셋에서 각 특성 간의 산점도(scatter plot)를 그리되, 각 클래스 별로 다른 색상을 사용하여 시각화하시오.
2-2) 꽃받침의 길이(Sepal Length)와 꽃받침의 너비(Sepal Width)의 관계를 시각화하고, 각 클래스별로 구분하여 출력하시오.
'''

print('문제 2.')
print('1) 산점도 그리기')
print('2) 꽃반침의 길이와 너비의 관계를 시각화. 클래스별로 구분하여 출력.')
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

def draw_scatter(x, y, color, label) :
    plt.scatter(x, y, c = color, label = label)
    plt.xlabel('length')
    plt.ylabel('width')

def draw_hitmap(subplot, title, x, y, xlabel, ylabel, fig) :
    ax = fig.add_subplot(subplot)
    ax.set_title(title, fontsize=20)
    c = ax.hist2d(x, y)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks(c[1])
    ax.set_yticks(c[2])
    fig.colorbar(c[3], ax=ax)

plt.figure(figsize=(10,10))
plt.title('[Iris scatter]', fontsize=20)
draw_scatter(setosa_sepal_length, setosa_sepal_width, 'purple', 'setosa sepal')
draw_scatter(versicolor_sepal_length,versicolor_sepal_width, 'yellow', 'versicolor sepal')
draw_scatter(virginica_sepal_length,virginica_sepal_width, 'royalblue', 'virginica sepal')
draw_scatter(setosa_petal_length, setosa_petal_width, '#BE93DD', 'setosa petal')
draw_scatter(versicolor_petal_length, versicolor_petal_width, '#9CDD93', 'versicolor petal')
draw_scatter(virginica_petal_length, virginica_petal_width, '#8ACBF7', 'virginica petal')
plt.legend()
plt.show()

fig = plt.figure(figsize=(90,30))
draw_hitmap(131, 'setosa', setosa_sepal_length, setosa_sepal_width, 'setosa_sepal_length', 'setosa_sepal_width', fig)
draw_hitmap(132, 'versicolor', versicolor_sepal_length, versicolor_sepal_width, 'versicolor_sepal_length', 'versicolor_sepal_width', fig)
draw_hitmap(133, 'virginica', virginica_sepal_length, virginica_sepal_width, 'virginica_sepal_length', 'virginica_sepal_width', fig)
plt.show()

'''
문제 3 :
3-1) 꽃잎의 길이(Petal Length)를 연속확률변수로 가정할 때, 이 확률변수의 평균과 분산을 계산하시오.
=> mean(), std()

3-2) 꽃잎의 너비(Petal Width)를 연속확률변수로 가정할 때, 이 확률변수의 확률밀도함수(probability density function, PDF)를 계산하고 그래프로 시각화하시오.
    (1) 취할 수 있는 값의 구간에 대해 하한과 상한을 x_range로 정의한다.
    (2) x_range를 정의역으로 하는 밀도함수 구현.
        def f(x) :
            if x_range[0] <= x <= x_range[1] :
                return 2*x
            else :
                return 0
    (3) 확률 분포 리스트 구현
        X = [x_range, f]
        
    (4) 평균
        def E(X, g=lambda x:x):
            x_range, f =X
            def integrand(x) :
                return g(x) * f(x)
            return intefrate.quad(integrand, -np.inf, np.inf)[0]
    (5) 분산
        def V(X, g=lambda x : x) :
            x_range, f = X
            mean = E(X, g)
            def integrand(x) :
                return (g(x) - mean) ** 2 * f(x)
            return integrate.quad(integrand, -np.inf, np.inf)[0]

3-3) 꽃잎의 길이(Petal Length)가 4cm 이상 5cm 미만일 확률을 계산하시오.
=> 

'''

from scipy import integrate

print('문제 3.')
petal_length = iris_df['petal.length']
petal_width = iris_df['petal.width']
print('확률변수의 평균 : ', round(petal_length.mean(), 3))
print('확률변수의 분산 : ', round(petal_length.var(), 3))

print('2) 꽃잎의 너비(Petal Width)를 연속확률변수로 가정할 때, '
      '이 확률변수의 확률밀도함수(probability density function, PDF)를 계산하고 그래프로 시각화하시오.')
def f(x) :
    if x_range[0] <= x <= x_range[1] :
        return 2*x
    else :
        return 0

max_value = max(petal_width)
min_value = min(petal_width)

x_range = np.array(petal_length)
X = [x_range, f]

xs = np.linspace(max_value, min_value, 100)

fig = plt.figure(figsize =(10,6))
ax = fig.add_subplot(111)
ax.plot(xs, [f(x) for x in xs], label = 'f(x)', color = 'green')
ax.hlines(0, -0.2, 1.2, alpha = 0.3)
ax.vlines(0, -0.2, 2.2, alpha=0.3)
ax.vlines(xs.max(), 0, 2.2, linestyles=':', color = 'pink')

xs = np.linspace(min_value, max_value, 100)

ax.fill_between(xs, [f(x) for x in xs], label ='prob')
ax.set_xticks(np.arange(-0.2, 1.3, 0.1))
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.2, 2.1)
ax.legend()
plt.show()


#<시행착오>
#def f(x):
    # if x_range[0] <= x <= x_range[1]:
    #     return 2 * x
    # else:
    #     return 0

#def E(X, g=lambda x:x):
    # x_range, f =X
    # def integrand(x) :
    #     return g(x) * f(x)
    # return integrate.quad(integrand, -np.inf, np.inf)[0]


# def V(X, g=lambda x: x):
#     x_range, f = X
#     mean = E(X, g)
#
#     def integrand(x):
#         return (g(x) - mean) ** 2 * f(x)
#
#     return integrate.quad(integrand, -np.inf, np.inf)[0]

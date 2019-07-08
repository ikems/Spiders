import matplotlib.pyplot as plt
import numpy
import pandas as pd
import pylab as pl  #用于修改x轴坐标

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

columns = ['index', 'name', 'score', 'director', 'year', 'area', 'styles', 'actors']
df = pd.read_csv('movie_top_250.csv', encoding='utf-8', header=None, names=columns, index_col='index')

# print(df)
colors1 = '#6D6D6D'


def analysis(content, angle, number):
    node_list = []
    #将数据切割并以列表的形式存储到node_list中
    for i in content.str.replace(' ', ',').str.split(','):
        node_list.extend(i)
    #去重
    node_set = set(node_list)
    #对node_list中的数据进行分别计数并存储到列表中
    node_num = {}
    for i in node_set:
        node_num[i] = node_list.count(i)

    #进行排序
    node_num = sorted(node_num.items(), key=lambda node_list: node_list[1], reverse=True)
    #取列表前10
    node_num = dict(node_num[0:number])
    #设置横坐标列表
    x_star = list(node_num.keys())
    #设置纵坐标列表
    y_star = list(node_num.values())
    #采用长条形的图来表示
    plt.bar(range(number), y_star, tick_label=x_star)
    #设置坐标角度和方向，以防坐标文字过长堆积在一起
    pl.xticks(rotation=angle)

    # 为每个条形图添加数值标签
    for x, y in enumerate(list(y_star)):
        # print(x, y)
        plt.text(x, y + 0.5, '%s' % round(y, 1), ha='center', color=colors1)


analysis(df.director, 270, 10)
plt.title('榜单最佳导演', color=colors1)
plt.xlabel('导演名字')
plt.ylabel('指导的电影数量')
plt.tight_layout()
plt.savefig('榜单最佳导演')
plt.show()


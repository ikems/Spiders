import matplotlib.pyplot as plt
import numpy
import pandas as pd
import pylab as pl  #用于修改x轴坐标


plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

#修改绘图风格，
plt.style.use('ggplot')

#设置所生成的图片大小
fig = plt.figure(figsize=(8,5))

#设置图标title、text标注的颜色
colors1 = '#6D6D6D'

#表头
columns = ['index', 'name', 'score', 'director', 'year', 'area', 'styles', 'actors']

#打开表格， index_col='index'表示将文件的索引设置为index
df = pd.read_csv('movie_top_250.csv', encoding='utf-8', header=None, names=columns, index_col='index')

def top_score_20():
    #按得分降序排列
    df_score = df.sort_values('score', ascending= False)

    name1 = df_score.name[:20]  #x轴坐标
    score1 = df_score.score[:20] #y轴坐标

    plt.bar(range(20), score1, tick_label = name1) #绘制条形图，用range（）能保持x轴正确顺序
    plt.ylim((9,9.8)) #设置纵坐标轴范围
    plt.title('豆瓣电影榜单top20', color=colors1)#标题
    plt.xlabel('电影名称')  #x轴标题
    plt.ylabel('评分')  #y轴标题

    #为每个条形图添加数值标签
    for x,y in enumerate(list(score1)):
        plt.text(x, y+0.01, '%s' %round(y,1), ha='center', color=colors1)

    plt.xticks(rotation=270) #x轴名称太长发生重叠，旋转为纵向显示
    plt.tight_layout()  #自动控制空白边缘，以全部显示x轴名称
    plt.savefig('电影评分前20榜单')
    plt.show()


def analysis2():
    area_list = []
    area_total = df.area

    sdd = df.area.str.replace(' ', ',').str.split(',')
    print(area_total)
    for i in sdd:
        area_list.extend(i)
    area_set = set(area_list)
    # print(len(sdd_set))
    area_num = {}
    for i in area_set:
        area_num[i] = area_list.count(i)

    area_num = sorted(area_num.items(), key=lambda area_list: area_list[1], reverse=True)
    area_num = dict(area_num[0:10])

    x_star = list(area_num.keys())
    y_star = list(area_num.values())

    plt.bar(range(10), y_star, tick_label=x_star)
    # pl.xticks(rotation=270)
    for x, y in enumerate(list(y_star)):
        # print(x, y)
        plt.text(x, y + 0.5, '%s' % round(y, 1), ha='center', color=colors1)

    plt.title('国家/地区电影作品数量排名', color=colors1)
    plt.xlabel('国家/地区')
    plt.ylabel('数量')
    # plt.tight_layout()
    plt.savefig('国家地区电影作品数量排名')
    plt.show()


# analysis2()


def analysis3():
    style_list = []

    for i in df.styles.str.replace(' ', ',').str.split(','):
        style_list.extend(i)

    style_set = set(style_list)
    # print(style_set)

    style_num = {}
    for i in style_set:
        style_num[i] = style_list.count(i)

    style_num = sorted(style_num.items(), key=lambda style_list: style_list[1], reverse=True)
    style_num = dict(style_num[0:10])

    x_styles = list(style_num.keys())
    y_styles = list(style_num.values())

    plt.bar(range(10), y_styles, tick_label=x_styles)
    # pl.xticks(rotation=270)
    for x, y in enumerate(list(y_styles)):
        # print(x, y)
        plt.text(x, y + 0.5, '%s' % round(y, 1), ha='center', color=colors1)

    plt.title('榜单电影类型统计', color=colors1)
    plt.xlabel('电影类型')
    plt.ylabel('数量')
    plt.tight_layout()
    plt.savefig('榜单电影类型统计')
    plt.show()



# analysis3()

def analysis4():
    actor_list = []
    for i in df.actors.str.split(','):
        if isinstance(i, list):
        # print(type(i))
            actor_list.extend(i[0:3])
        else:
            pass
    actor_set = set(actor_list)
    # print(style_set)

    actor_num = {}
    for i in actor_set:
        actor_num[i] = actor_list.count(i)

    actor_num = sorted(actor_num.items(), key=lambda actor_list: actor_list[1], reverse=True)
    actor_num = dict(actor_num[0:20])

    x_actors = list(actor_num.keys())
    y_actors = list(actor_num.values())

    plt.bar(range(20), y_actors, tick_label=x_actors)
    pl.xticks(rotation=270)
    for x, y in enumerate(list(y_actors)):
        # print(x, y)
        plt.text(x, y + 0.5, '%s' % round(y, 1), ha='center', color=colors1)

    plt.title('榜单最佳演员', color=colors1)
    plt.xlabel('演员名字')
    plt.ylabel('参演电影数量')
    plt.tight_layout()
    plt.savefig('榜单最佳演员')
    plt.show()
    print(actor_list)

# analysis4()


def analysis5():
    a = df.index
    b = []
    for i in a:
        b.append(i)
    print(b)

    c = df.score
    d = []
    for i in c:
        d.append(i)
    print(d)
    plt.gca().invert_yaxis()  # 反转y轴
    # plt.style.use('ggplot')
    plt.scatter(d, b)
    plt.xlabel('score')
    plt.ylabel('index')
    plt.title('排名与得分')
    plt.savefig('得分与排名的关系')
    plt.show()


analysis5()

def analysis6():
    a = df.index
    b = []
    for i in a:
        b.append(i)
    print(b)

    c = df.score
    d = []
    for i in c:
        d.append(i)
    print(d)
    plt.gca().invert_yaxis()  # 反转y轴
    plt.xlabel('score')
    plt.ylabel('index')
    plt.title('排名与得分')
    plt.savefig('得分与排名的关系')
    plt.show()


analysis5()

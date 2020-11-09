# -*- coding: utf-8 -*-
#导入所需要的包
import pymysql
import networkx as nx
import matplotlib.pyplot as plt

def getData(sql):
    # 打开数据库连接
    # 打开数据库连接
    db = pymysql.connect("localhost","root","root","data-set" )
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句，频接sql语句，由参数提供
    #sql = "SELECT * FROM mix6 WHERE Weight >1"
    print(sql)
    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 获取所有记录列表
       results = cursor.fetchall()
    except:
       print("Error: unable to fecth data")
    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()
    return results

def drawPicture(elem_dic):
    # -*- coding: utf-8 -*-
    import pandas as pd
    import numpy as np
    import codecs
    import networkx as nx
    import matplotlib.pyplot as plt

    import matplotlib
    #设定字体以及颜色
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['font.family'] = 'sans-serif'

    colors = ["red", "green", "blue", "yellow"]
    #创建无向图
    G = nx.Graph()
    #添加节点，这边添加节点的时候也需要注意一下
    G.add_weighted_edges_from(elem_dic)
    # nx.draw(G,with_labels=True,pos=nx.random_layout(G),font_size=12,node_size=2000,node_color=colors) #alpha=0.3
    # pos=nx.spring_layout(G,iterations=50)
    pos = nx.random_layout(G)
    # nx.draw_networkx_nodes(G, pos, node_shape='o', node_color=colors, alpha=0.3)
    nx.draw(G, pos, with_labels=False)

    # plt.savefig('./1.png') #存储生成的图片
    plt.show()
    #计算节点的中心性
    betweenness = nx.betweenness_centrality(G, normalized=False)
    print(sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[0:10])

    # triangles = nx.triangles(G)
    # sorted(triangles.items(), key=lambda x: x[1], reverse=True)[0:10]
    #print("节点的度中心性:",nx.degree_centrality(G))  # 计算节点的度中心性
    #print("节点的接近中心性:",nx.closeness_centrality(G))  # 计算节点的接近中心性
    #print("节点的介数中心性:",nx.betweenness_centrality(G))  # 计算节点的介数中心性
    #print("边的介数中心性",nx.edge_betweenness_centrality(G))  # 计算边的介数中心性
    #print("节点的特征向量中心性",nx.eigenvector_centrality(G))  # 计算节点的特征向量中心性
    #print("节点的流介数中心性:",nx.current_flow_betweenness_centrality(G))  # 计算节点的流介数中心性
    #print("边的流介数中心性:",nx.edge_current_flow_betweenness_centrality(G))  # 计算边的流介数中心性


if __name__=="__main__":
    #我是利用的Gephi来生成的共现频次，然后直接导入了数据库。格式如下
    '''
    Scource(头)  Target(尾)  weight(频次)
    A   B   2
    C   D   4
    '''
    '''
    邻接矩阵和共现矩阵的算法网上也有，不过我这边没用到这个算法。
    不过应该也可以自己写，应该也不难的
    '''
    elem_list=getData("SELECT Source,Target,Weight FROM mix6 WHERE Weight >=1")
    '''
    因为从数据库查询出来的数据，fetchall的结果是这样的((A,B,2),(C,D,4),(E,F,3))
    刚好和其中一种传入节点参数的格式差不多，[(A,B,2),(C,D,4),(E,F,3)]，我就直接把元组转换为列表，当作参数传进去了
    '''
    # print(list(elem_list))
    #网络分析
    drawPicture(list(elem_list))



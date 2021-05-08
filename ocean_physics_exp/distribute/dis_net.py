# coding:utf-8
import matplotlib.pyplot as plt
import numpy
import json
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

if __name__ == "__main__":

    fig, ax1 = plt.subplots(1, 1, figsize=(6, 3), frameon=True)

    plt.grid(True, linestyle='--', alpha=0.5)
    ax1.set_xlabel("接入无人平台节点数(单位：个)")
    ax1.set_ylabel("平均每秒仿真接收网络消息数(单位：条)", color='tab:red')
    ax1.set_xlim((0, 55))
    ax1.set_ylim((0, 1000))
    ax1.tick_params(axis='y', labelcolor='tab:red')
    ax2 = ax1.twinx()
    ax2.set_ylabel("平均一个仿真周期运行时间(单位：秒)", color='tab:blue')
    ax2.set_ylim((0, 0.005))
    ax2.tick_params(axis='y', labelcolor='tab:blue')

    updateTime = []
    msgNum = []
    index = []
    for file_index in range(1, 10+1):
        with open("./dis_data_{}.json".format(file_index * 5), 'r') as f:
            jsonData = json.load(f)
            index.append(file_index*5)
            updateTime.append(jsonData["updateTime"])
            msgNum.append(jsonData["msgNum"])

    ax1.plot(index, msgNum, linewidth=1, marker='.', color='tab:red')
    ax2.plot(index, updateTime, linewidth=1, marker='.', color='tab:blue')
    fig.tight_layout()
    plt.savefig("./dis_net.png", dpi=300)
    plt.clf()
    # plt.show()
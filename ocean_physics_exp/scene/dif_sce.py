# coding:utf-8
import matplotlib.pyplot as plt
import numpy
import json
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        if height > 0:
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


if __name__ == "__main__":
    f = open("./scene.json", 'r')
    jsonData = json.load(f)
    blueZ = jsonData["blueZ"]
    redZ = jsonData["redZ"]

    # blueZ = {1.1, 2.5, 1.6, 2.9}
    # redZ = {1.6, 0.7, 1.9, 2.2}


    x = numpy.arange(len(blueZ))
    width = 0.4

    fig, ax = plt.subplots(1, 1, figsize=(9, 3), frameon=True)

    # plt.xlim((0, 5))
    plt.ylim((0, 5))
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlabel("实验场景", size=12)
    plt.ylabel("平均每场训练战损(单位：艘)", size=12)

    # plt.plot(numpy.arange(0, 50), netMsg, label="仿真接收网络通信消息数", linewidth=1, color='blue', alpha=0.5)
    # plt.plot(numpy.arange(0, 50), agentMsg, label="仿真内agent交互消息数", linewidth=1, color='red', alpha=0.5)

    rect1 = plt.bar(x-width/2, blueZ, width, label="蓝方战损数", tick_label=['                场景一', '                场景二','                场景三','                场景四'])
    rect2 = plt.bar(x+width/2, redZ, width, label="红方战损数")
    autolabel(rect1)
    autolabel(rect2)

    fig.tight_layout()
    plt.legend()
    plt.savefig("./dif_scene.png", dpi=300)
    plt.clf()
    # plt.show()
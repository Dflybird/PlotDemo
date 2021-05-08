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
    f = open("./dis_msg_data_2.json", 'r')
    jsonData = json.load(f)
    agentMsg = jsonData["agentMsg"]
    netMsg = jsonData["netMsg"]

    agentMsg = agentMsg[-140:-90]
    netMsg = netMsg[-140:-90]

    x = numpy.arange(len(agentMsg))
    width = 0.4

    fig, ax = plt.subplots(1, 1, figsize=(9, 3), frameon=True)

    plt.xlim((0, 50))
    plt.ylim((-5, 20))
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlabel("仿真周期(单位：cycle)", size=12)
    plt.ylabel("消息数量", size=12)

    plt.plot(numpy.arange(0, 50), netMsg, label="仿真接收网络通信消息数", linewidth=1, color='blue', alpha=0.5)
    plt.plot(numpy.arange(0, 50), agentMsg, label="仿真内agent交互消息数", linewidth=1, color='red', alpha=0.5)

    # rect1 = ax.bar(x-width/2, netMsg, width, label="仿真接收网络通信消息数")
    # rect2 = ax.bar(x+width/2, agentMsg, width, label="仿真内agent交互消息数")
    # autolabel(rect1)
    # autolabel(rect2)

    fig.tight_layout()
    plt.legend()
    # plt.savefig("./dis_msg_bar.png", dpi=300)
    # plt.clf()
    plt.show()
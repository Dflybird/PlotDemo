# coding:utf-8
import matplotlib.pyplot as plt
import numpy
import json
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

if __name__ == "__main__":

    plt.subplots(1, 1, figsize=(8, 4), frameon=True)
    plt.xlim((0, 30))
    plt.ylim((-3, 3))
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlabel("时刻（单位：秒）", size=12)
    plt.ylabel("无人船在世界坐标系中的垂直坐标", size=12)
    labels = ["无作用力影响", "受重力和静水浮力影响", "受重力和海浪浮力影响"]
    for file_index in range(0, 3):
        with open("./usv_buoy_data_{}.json".format(file_index), 'r') as f:
            jsonData = json.load(f)
            buoyData = jsonData["buoyData"]
            plt.plot(numpy.arange(0, len(buoyData) / 50, 0.02), buoyData, label=labels[file_index], linewidth=2)

    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig("./usv_buoy.png", dpi=300)
    plt.clf()
    # plt.show()
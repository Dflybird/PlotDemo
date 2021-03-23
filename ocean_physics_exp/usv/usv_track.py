# coding:utf-8
import matplotlib.pyplot as plt
import numpy
import json
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

if __name__ == "__main__":

    plt.subplots(1, 1, figsize=(16, 8), frameon=True)
    plt.xlim((0, 50))
    plt.ylim((-5, 10))
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlabel("无人船运动距离（单位：米）", size=16)
    plt.ylabel("无人船偏离规划航迹距离（单位：米）", size=16)
    labels = ["无作用力影响", "受横向风和静水浮力影响", "受横向风和海浪浮力影响"]
    for file_index in range(0, 3):
        with open("./usv_track_data_{}.json".format(file_index), 'r') as f:
            jsonData = json.load(f)
            buoyData = jsonData["buoyData"]
            plt.plot(numpy.arange(0, len(buoyData)*10, 10), numpy.abs(buoyData), label=labels[file_index], linewidth=2)

    plt.legend(loc="lower right")
    plt.savefig("./usv_track.png", dpi=300)
    plt.clf()
    # plt.show()
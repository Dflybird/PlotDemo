# coding:utf-8
import matplotlib.pyplot as plt
import numpy
import json
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

if __name__ == "__main__":

    plt.subplots(1, 1, figsize=(8, 4), frameon=True)
    plt.xlim((0, 14))
    plt.ylim((0, 0.8))
    plt.grid(True, linestyle='--', alpha=0.5)
    # plt.xlabel("Lutra Airboat和仿真的无人船速度对比，推进力为3.13N", size=12)
    plt.xlabel("时间 （单位：秒）", size=12)
    plt.ylabel("速度（单位：米/秒）", size=12)
    labels = ["仿真无人船", "真实舰艇"]
    f = open("./lutra_airboat_data.json")
    # f = open("./lutra_prop_data.json")
    jsonData = json.load(f)
    realData = jsonData["speedData"]
    f = open("./sim_speed_data.json")
    jsonData = json.load(f)
    simData = jsonData["speed"]
    plt.plot(numpy.arange(0, len(realData) / 5, 0.2), realData, label="真实舰艇", linewidth=0, marker='s')
    plt.plot(numpy.arange(0, len(simData) / 10, 0.1), simData, label="仿真无人船", linewidth=0, marker='.')

    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig("./speed_lutra_airboat.png", dpi=300)
    # plt.show()
    plt.clf()

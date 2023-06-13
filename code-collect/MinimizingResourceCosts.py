# -*- coding : utf-8 -*-
# Time       : 2023/4/25 11:04
# Auth       : Yangyang Zhang(张洋洋)
# File       : MinimizingResourceCosts.py
# Explain    : 最小化资源成本

"""
公司创新实验室正在研究如何最小化资源成本，最大化资源利用率，请你设计算法帮他们解决一个任务混部问题：
1. 有 taskNum 项任务，每个任务有开始时间（startTime），结束时间（endTime），并行度（parallelism）三个属性。
2. 并行度是指这个任务运行时占用的服务器数量，一个服务器在每个时刻可以被任意任务使用但最多被一个任务占用 ，任务运行完会立即释放（结束时刻不占用）。
3. 给定一批任务，让这批任务由同一批服务器承载运行，请你计算完成这批任务最少需要多少服务器，从而最大化控制资源成本。

解答：贪心算法
1. 按照任务的开始时间将任务排序；
2. 遍历每一个任务，尝试将其分配到当前可用的服务器上；
3. 如果当前没有可用的服务器，就新增一个服务器，并将该任务分配给新服务器；
4. 如果当前有多个可用的服务器，则选择其中结束时间最早的服务器，并将该任务分配给该服务器；
5. 更新服务器的结束时间，并标记该服务器上当前任务的并行度；
6. 对于结束时间早于当前任务开始时间的服务器，将其释放，从而确保服务器的使用率最高。
"""


def min_servers(tasks):
    # 将任务按照开始时间排序
    tasks = sorted(tasks, key=lambda t: t['startTime'])
    servers = []
    for task in tasks:
        # 查找所有可用的服务器，选择结束时间最早的服务器
        available_servers = [s for s in servers if s['endTime'] <= task['startTime']]
        if available_servers:
            server = min(available_servers, key=lambda s: s['endTime'])
            server['endTime'] = task['endTime']
            server['parallelism'] += task['parallelism']
        else:
            # 新增一个服务器
            server = {'endTime': task['endTime'], 'parallelism': task['parallelism']}
            servers.append(server)
    return len(servers)

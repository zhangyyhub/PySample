# -*- coding : utf-8 -*-
# Time       : 2023/4/17 17:44
# Auth       : Yangyang Zhang(张洋洋)
# File       : LoadBalancer.py
# Explain    : 模拟实现加权轮询的负载均衡调度策略

class LoadBalancer:
    def __init__(self, servers:list):
        self.servers = servers             # 后端服务器列表
        self.weights = [1] * len(servers)  # 后端服务器权重列表，初始权重为1
        self.total_weight = len(servers)   # 总权重，初始值为服务器数量

    def get_next_server(self):
        """
        选择后端服务器，更新服务器权重
        """
        max_weight = max(self.weights)                          # 获取最大权重
        chosen_server = None
        for i in range(len(self.servers)):
            if self.weights[i] == max_weight:
                chosen_server = self.servers[i]                 # 选择权重最大的服务器
                self.weights[i] -= self.total_weight            # 权重减去总权重
                break

        self.total_weight -= 1                                  # 总权重减1
        self.weights = [weight + 1 for weight in self.weights]  # 更新所有服务器的权重，增加1
        print("self.weights:", self.weights)
        print("self.total_weight:", self.total_weight)

        return chosen_server

    def simulate_request(self):
        """
        选择一个后端服务器处理请求，并输出选择的服务器名称
        """
        chosen_server = self.get_next_server()
        print("Request handled by server:", chosen_server)


# 后端服务器列表
servers = ['Server1', 'Server2', 'Server3']
# 创建负载均衡器
load_balancer = LoadBalancer(servers)

# 模拟十次请求量
for i in range(10):
    load_balancer.simulate_request()

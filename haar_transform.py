import numpy as np
from collections import deque

class HaarTransform:
    def transnform(self, data):
        # data = np.array(data)
        avg = np.mean(data)
        print('average:', avg)
        eigenvector = self.find_eigenvector_bfs(data)
        print('eigenvector:', eigenvector)
        return avg, eigenvector

    def inverse_transform(self, avg, eigenvector, length):
        data = []
        for i in range(length):
            index = i + length

            data.append(avg)
            while(index > 1):
                g = (-1) ** ((index % 2) + 2)
                index = int(index / 2)
                data[i] += g * eigenvector[index-1]
        return data

    def find_eigenvector_bfs(self, data):
        eigenvector = []
        queue = deque([data])
        while queue:
            node = queue.popleft()
            if len(node) == 1:
                continue

            left_node, right_node = self.split_data(node)
            eigenvector.append(self.calculate_root_eigenvector(left_node, right_node))
            queue.append(left_node)
            queue.append(right_node)
        return eigenvector

    def split_data(self, data):
        middle_index = int(len(data) / 2)
        left_data = data[:middle_index]
        right_data = data[middle_index:]
        return left_data, right_data

    def calculate_root_eigenvector(self, left_data, right_data):
        ml = np.mean(left_data)
        mr = np.mean(right_data)
        return (ml-mr)/2

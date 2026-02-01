from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        queue = deque([root])
        level_num = 0
        max_sum = float('-inf')
        answer = 0

        while queue:
            level_num += 1
            level_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                answer = level_num

        return answer

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
		#use mapping to save operations
        move = {'0': ('1','9'),
                '1': ('0','2'),
                '2': ('1','3'),
                '3': ('2','4'),
                '4': ('3','5'),
                '5': ('4','6'),
                '6': ('5','7'),
                '7': ('6','8'),
                '8': ('7','9'),
                '9': ('8','0')}
        deadends = set(deadends)
        start = '0000'
        if start == target:
            return 0
        if start in deadends:
            return -1
        queue = deque([start,])
        step = 0
        while queue:
            step += 1
            size = len(queue)
            for _ in range(size):
                previous = queue.popleft()
                for i, num in enumerate(previous):
                    for nextNum in move[num]:
                        candidate = previous[:i] + nextNum + previous[(i+1):]
                        if candidate == target:
                            return step
                        elif candidate not in deadends:
                            deadends.add(candidate)
                            queue.append(candidate)
        return -1
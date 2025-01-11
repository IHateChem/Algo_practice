class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        answers = []
        times = sorted(zip(growTime, plantTime), reverse = True)
        t = 0
        for g, p in times:
            t += p
            answers.append(t+g)
        return max(answers)

        
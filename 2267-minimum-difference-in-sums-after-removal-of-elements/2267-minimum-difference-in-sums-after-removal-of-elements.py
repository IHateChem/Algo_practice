import heapq
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        # 초기 힙 설정
        left_heap = [-x for x in nums[:n]]  # 최대 힙
        heapq.heapify(left_heap)
        left_sum = -sum(left_heap)

        right_heap = nums[-n:]  # 최소 힙
        heapq.heapify(right_heap)
        right_sum = sum(right_heap)

        # 왼쪽 구역 탐색
        left_sums = [left_sum]
        for i in range(n, 2 * n):
            # 최대 힙에서 최댓값 확인 후 비교
            if -left_heap[0] > nums[i]:
                left_sum += nums[i] + heapq.heappop(left_heap)
                heapq.heappush(left_heap, -nums[i])
            left_sums.append(left_sum)

        # 우측 구역 탐색
        right_sums = [right_sum]
        for i in range(2 * n - 1, n - 1, -1):
            # 최소 힙에서 최솟값 확인 후 비교
            if right_heap[0] < nums[i]:
                right_sum += nums[i] - heapq.heappop(right_heap)
                heapq.heappush(right_heap, nums[i])
            right_sums.append(right_sum)

        right_sums.reverse()  # 순서를 맞추기 위해 뒤집기

        # 답 반환: left_sums와 right_sums의 차의 최솟값
        min_diff = float('inf')
        for left, right in zip(left_sums, right_sums):
            min_diff = min(min_diff, left - right)

        return min_diff
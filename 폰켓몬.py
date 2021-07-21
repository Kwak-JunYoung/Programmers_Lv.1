def solution(nums):
    return min(len(nums) // 2, len(set(nums)))
# len(nums) // 2 는 최대로 뽑을 수 있는 포켓몬의 수를 뜻합니다.
# len(set(nums))는 중복 제거된 포켓몬의 갯수를 의미합니다. 현재 챙길 수 있는 포켓몬의 종류수를 의미하기도 합니다.
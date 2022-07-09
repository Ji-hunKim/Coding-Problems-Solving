class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tmp = 1
        check = 0
        arr = []
        for n in nums:
            if n == 0:
                check += 1
                continue
            else:
                tmp *= n
        if check >= 2:
            for _ in range(len(nums)):
                arr.append(0)
        elif check == 1:
            for n in nums:
                if n == 0:
                    arr.append(tmp)
                else:
                    arr.append(0)
        else:
            for n in nums:
                arr.append(tmp // n)
        return arr
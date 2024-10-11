class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = deque([])
        product = 1
        for i in nums:
            product *= i
            pre.append(product)

        product = 1
        for i in reversed(nums):
            product *= i
            post.appendleft(product)

        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(post[i + 1])
            elif i == len(nums) - 1:
                result.append(pre[i - 1])
            else:
                result.append(pre[i - 1] * post[i + 1])  

        return result


        
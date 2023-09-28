# 3. Create a class to find three elements that sum to zero from a set of n real numbers
# Input array: [-25,-10,-7,-3,2,4,8,10]
# Expected output: [[-10,2,8],[-7,-3,10]]

class ThreeSumFinder:
    def find_three_sum(self, nums):
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result



nums = [-25, -10, -7, -3, 2, 4, 8, 10]
sum_finder = ThreeSumFinder()
result = sum_finder.find_three_sum(nums)



print("Three elements that sum to zero:")
print(result)

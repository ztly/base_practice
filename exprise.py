class Solution:
    def twoSum(self, nums, target):
        for numi in range(0, len(nums)):
            arrs = nums[numi+1:]
            for arri in range(0, len(arrs)):
                sum = nums[numi] + arrs[arri]
                if sum == target:
                    return [numi,numi+arri+1]

    def twoSum2(self, nums, target):
        for index1 in range(0, len(nums)):
            nums2 = nums[index1+1:]
            for index2 in range(len(nums2)):
                num1 = nums[index1]
                num2 = nums2[index2]
                sum = num1+num2
                if sum == target:
                    return [index1, index2+index1+1]

if __name__ == "__main__":               
    solution = Solution()
    sum = solution.twoSum2([2, 7, 11, 15],26)
    print(sum)
#! /usr/bin/env python
###
### given a array s of n integers, find three integers in s such that the sum is closest to the target
###

class Solution:
	def execute(self,arrList,target):
		intLen=len(arrList)
		if intLen<=3:
			return 0
		smallSum=arrList[0]+arrList[1]+arrList[2]
		arrList.sort()		
		for i in range(0,intLen):
			j=i+1
			k=intLen-1
			while j<k:
				threeSum=arrList[i]+arrList[j]+arrList[k]
				if threeSum == target:
					return threeSum
				elif threeSum > target:
					k-=1
				else:
					j+=1
				if abs(threeSum-target) < abs(smallSum-target):
					smallSum=threeSum
		return smallSum



obj=Solution()
arrList=[1,2,3,5,7,-1,-4,22,-2,232,24,90,-10,180,-15]
target=188
rs=obj.execute(arrList,target)
print rs

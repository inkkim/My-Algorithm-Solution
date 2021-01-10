# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def merge_sort(elements):
	if len(elements) <= 1:
		return elements
	
	half = len(elements) // 2
	left = merge_sort(elements[:half])
	right = merge_sort(elements[half:])
	return merge(left, right)


def merge(left, right):
	ans = []
	while len(left) > 0 or len(right) > 0:
		if len(left) > 0 and len(right) > 0:
			if left[0] <= right[0]:
				ans.append(left[0])
				left = left[1:]
			else:
				ans.append(right[0])
				right = right[1:]
		elif len(left) > 0:
			ans.append(left[0])
			left = left[1:]
		elif len(right) > 0:
			ans.append(right[0])
			right = right[1:]
	return ans

n = int(input())
elements = input().split()
merge_sort(elements)
def two_sum(nums,target):
	index_list= range(len(nums))
	for idx in index_list:
		first_num = nums[idx]
		for idx_j in index_list:
			if idx_j == idx:
				continue
			second_num = nums[idx_j]
			num_sum = first_num + second_num
			if target == num_sum:
				return [idx, idx_j]


print (two_sum([2,5,7,8,9],11))
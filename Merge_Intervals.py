def merge_intervals(intervals):
	if len(intervals) == 1:
		return intervals
	if not len(intervals):
		return []

	intervals = sorted(intervals, key= lambda x: (x[0], x[1]))
	#print(intervals)
	outputs = []
	curr_start = intervals[0][0]
	curr_end = intervals[0][1]
	for new_start, new_end in intervals:
		if new_start <= curr_end:
			curr_end = max(curr_end, new_end)
		else:
			outputs.append([curr_start, new_end])
			curr_start,curr_end = new_start, new_end
	outputs.append([curr_start, curr_end])
	return outputs






print(merge_intervals([[1,3],[2,6],[4,8]]))
print(merge_intervals([[1,4],[4,5]]))
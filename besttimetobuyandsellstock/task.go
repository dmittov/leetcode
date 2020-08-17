package besttimetobuyandsellstock

func min(lhs int, rhs int) int {
	if lhs < rhs {
		return lhs
	}
	return rhs
}

func maxIntSlice(slice []int) int {
	maxVal := slice[0]
	for _, val := range slice {
		if val > maxVal {
			maxVal = val
		}
	}
	return maxVal
}

func maxProfit(prices []int) int {
	if len(prices) < 1 {
		return 0
	}
	var values = make([]int, len(prices))
	for currentMin, currentValue, idx := prices[0], 0, 1; idx < len(prices); idx++ {
		currentMin = min(prices[idx], currentMin)
		currentValue = prices[idx] - currentMin
		values[idx] = currentValue
	}
	return maxIntSlice(values)
}

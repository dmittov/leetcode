package besttimetobuyandsellstock2

func maxProfit(prices []int) int {
	profit := 0
	lastIdx := len(prices) - 1
	var stepProfit int
	for prevIdx := 0; prevIdx < lastIdx; prevIdx++ {
		stepProfit = prices[prevIdx+1] - prices[prevIdx]
		if stepProfit > 0 {
			profit += stepProfit
		}
	}
	return profit
}

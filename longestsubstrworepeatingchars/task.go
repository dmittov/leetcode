package longestsubstrworepeatingchars

func lengthOfLongestSubstring(s string) int {
	charLatestPosition := make(map[int32]int)
	longest := 0
	runes := []rune(s)
	for startPos, endPos := 0, 0; endPos < len(runes); endPos++ {
		symbol := runes[endPos]
		latestOccurence, exists := charLatestPosition[symbol]
		if exists {
			if latestOccurence >= startPos {
				startPos = latestOccurence + 1
			}
		}
		if current := endPos - startPos + 1; current > longest {
			longest = current
		}
		charLatestPosition[symbol] = endPos
	}
	return longest
}

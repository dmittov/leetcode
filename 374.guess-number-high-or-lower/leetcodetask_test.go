package leetcodetask

import (
	"testing"
)

type testCase struct {
	num, max int
}

func TestGuesser(t *testing.T) {
	for _, input := range []testCase{
		{num: 6, max: 10},
		{num: 6, max: 6},
		{num: 0, max: 10},
	} {
		var guess = func(num int) int {
			if num == input.num {
				return 0
			} else if input.num < num {
				return -1
			}
			return 1
		}
		if result := guessNumber(input.max, guess); result != input.num {
			t.Errorf("Wrong guess: %d / max: %d, right number was: %d", result, input.max, input.num)
		}
	}
}

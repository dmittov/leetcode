package leetcodetask

/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * func guess(num int) int;
 */

func getGuessNumber(lowerBound int, upperBound int) int {
	return (lowerBound + upperBound) / 2
}

func guessNumber(n int, guess func(num int) int) int {
	lowerBound := 0
	upperBound := n
	var guessResult int
	guessNumber := getGuessNumber(lowerBound, upperBound)
	for guessResult = guess(guessNumber); guessResult != 0; guessResult = guess(guessNumber) {
		if guessResult < 0 {
			upperBound = guessNumber
		} else {
			if upperBound-lowerBound > 1 {
				lowerBound = guessNumber
			} else {
				lowerBound = guessNumber + 1
			}
		}
		guessNumber = getGuessNumber(lowerBound, upperBound)
	}
	return guessNumber
}

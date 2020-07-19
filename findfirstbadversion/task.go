package findfirstbadversion

/**
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */

func findFirstBadVersion(lo int, hi int, isBadVersion func(version int) bool) int {
	var median int
	for hi-lo > 1 {
		median = (lo + hi) / 2
		if isBadVersion(median) {
			hi = median
		} else {
			lo = median
		}
	}
	if isBadVersion(lo) {
		return lo
	}
	return hi
}

func firstBadVersion(n int, isBadVersion func(version int) bool) int {
	return findFirstBadVersion(1, n+1, isBadVersion)
}

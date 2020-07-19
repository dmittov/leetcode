package findfirstbadversion

import (
	"testing"
)

type testCase struct {
	badVersion, maxVersion int
}

func TestFirstBadVersion(t *testing.T) {
	// versioning start with 1
	for _, input := range []testCase{
		{badVersion: 13, maxVersion: 20},
		{badVersion: 1, maxVersion: 1},
		{badVersion: 1, maxVersion: 10},
		{badVersion: 10, maxVersion: 10},
	} {
		var isBadVersion = func(version int) bool {
			if version >= input.badVersion {
				return true
			}
			return false
		}
		if result := firstBadVersion(input.maxVersion, isBadVersion); result != input.badVersion {
			t.Errorf("Wrong result: %d / bad version: %d, max version was: %d", result, input.badVersion, input.maxVersion)
		}
	}
}

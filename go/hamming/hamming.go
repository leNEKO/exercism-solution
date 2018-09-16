package hamming

import (
	"errors"
)

// Distance calculate hamming diff
func Distance(a, b string) (int, error) {
	if len(a) != len(b) {
		return -1, errors.New("length error")
	}

	distance := 0
	for i := range a {
		if a[i] != b[i] {
			distance++
		}
	}

	return distance, nil
}

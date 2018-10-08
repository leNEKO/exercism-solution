package isogram

import (
	u "unicode"
)

// IsIsogram - return true if input is an isogram
func IsIsogram(word string) bool {
	var counter []rune

	for _, r := range word {
		lower := u.ToLower(r)
		if RuneInSlice(lower, counter) {
			return false
		}
		if u.IsLetter(r) {
			counter = append(counter, lower)
		}
	}

	return true
}

// RuneInSlice - check if rune is already present in a runes slice
func RuneInSlice(query rune, slice []rune) bool {
	for _, r := range slice {
		if query == r {
			return true
		}
	}

	return false
}

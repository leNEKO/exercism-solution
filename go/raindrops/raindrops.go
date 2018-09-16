package raindrops

import "strconv"

// Convert an integer to raindrops string
func Convert(i int) string {
	r := ""
	if i%3 == 0 {
		r += "Pling"
	}
	if i%5 == 0 {
		r += "Plang"
	}
	if i%7 == 0 {
		r += "Plong"
	}
	if r == "" {
		r = strconv.Itoa(i)
	}
	return r
}

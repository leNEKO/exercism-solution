// Package twofer is a solution to the exercism's two fer exercise
package twofer

// ShareWith return string:  One for 'input', one for me
func ShareWith(input string) string {
	if len(input) == 0 {
		input = "you"
	}

	return "One for " + input + ", one for me."
}

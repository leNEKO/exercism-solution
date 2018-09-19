package scrabble

import "strings"

// ScoreGroup : char -> score
var ScoreGroup = map[string]int{
	"aeioulnrst": 1,
	"dg":         2,
	"bcmp":       3,
	"fhvwy":      4,
	"k":          5,
	"jx":         8,
	"qz":         10,
}

// Score : calculate scrabble score from word
func Score(word string) int {
	m := ScoreMap(ScoreGroup)
	score := 0
	for _, r := range strings.ToLower(word) {
		score += m[r]
	}
	return score
}

// ScoreMap : convert string -> int map to rune -> int map
func ScoreMap(m map[string]int) map[rune]int {
	var r = map[rune]int{}
	for group, v := range m {
		for _, c := range group {
			r[c] = v
		}
	}
	return r
}

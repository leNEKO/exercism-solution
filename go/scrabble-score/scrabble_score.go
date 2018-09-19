package scrabble

import (
	s "strings"
	u "unicode"
)

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
var runeScore = ScoreMap(ScoreGroup)

// Score - calculate scrabble score from word
var Score = ScoreSwitch

// ScoreSwitch (with hardcoded switchs instead of a map)
func ScoreSwitch(word string) int {
	score := 0
	for _, r := range word {

		switch u.ToLower(r) {
		case 'a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't':
			score += 1
		case 'd', 'g':
			score += 2
		case 'b', 'c', 'm', 'p':
			score += 3
		case 'f', 'h', 'v', 'w', 'y':
			score += 4
		case 'k':
			score += 5
		case 'j', 'x':
			score += 8
		case 'q', 'z':
			score += 10
		}
	}
	return score
}

// ScoreLowerByRune (convert to lower rune by rune)
func ScoreLowerByRune(word string) int {
	score := 0
	for _, r := range word {
		score += runeScore[u.ToLower(r)]
	}
	return score
}

// ScoreLowerByword (convert to lower whole string)
func ScoreLowerByword(word string) int {
	score := 0
	for _, r := range s.ToLower(word) {
		score += runeScore[r]
	}
	return score
}

// ScoreMap - convert string -> int map to rune -> int map
func ScoreMap(m map[string]int) map[rune]int {
	var r = map[rune]int{}
	for group, v := range m {
		for _, c := range group {
			r[c] = v
		}
	}
	return r
}

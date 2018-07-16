var reverseString = function(str) {
    return str
        .split("")
        .reverse()
        .join("");
};

module.exports = reverseString;

if (require.main === module) {
    console.log(
        reverseString(reverseString("a̐éö̲\r\néléphant, p🏳️‍🌈, hêtre, Aïe 🌷"))
    );
}

class Pangram {
    constructor(str) {
        this.str = str
    }

    isPangram() {
        var str = this.str;
        if (str == '' || str == undefined) {
            return false;
        }
        var bingo = {};
        for (var c of "abcdefghijklmnopqrstuvwxz".split("")) {
            bingo[c] = 1;
        }

        for (var c of str.toLowerCase()) {
            if (bingo[c] !== undefined) {
                delete bingo[c];
            }
        }
        return (Object.keys(bingo).length === 0);

    }
}

module.exports = Pangram
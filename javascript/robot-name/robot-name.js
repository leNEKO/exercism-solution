//  Fisher–Yates shuffle
function shuffle(a) {
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
    return a;
}

// configuration
const padAlpha = 2;
const padDigit = 3;

const asciis = {
    keys: "0123456789abcdefghijklmnop",
    vals: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
};

const digits = {
    keys: "0123456789",
    vals: "0123456789"
};

// generate all possible ids
var ids = [];
for (
    let i = 0;
    i < digits.keys.length ** padAlpha * digits.keys.length ** padDigit;
    i++
) {
    ids.push(i);
}
// then shuffle
var shuffledIds = shuffle(ids);

// python like divmod
function divmod(num, div) {
    return { quotient: Math.floor(num / div), remainder: num % div };
}

// convert decimal to int with custom base and symbols
function decToWhatever(dec, pad, dict) {
    let conv = "";
    for (c of parseInt(dec, 10).toString(dict.keys.length)) {
        conv += dict.vals[dict.keys.indexOf(c)];
    }
    return conv.padStart(pad, dict.vals[0]);
}

// convert decimal to custom format AADDD
function numToName(num) {
    let parts = divmod(num, 10 ** padDigit);
    let alphaPart = decToWhatever(parts.quotient, padAlpha, asciis);
    let digitPart = decToWhatever(parts.remainder, padDigit, digits);
    return alphaPart + digitPart;
}

class Robot {
    constructor() {
        this.setName();
    }

    setName() {
        // pick next avalaible id
        this.name = numToName(shuffledIds.pop());
    }

    getName() {
        return this.name;
    }

    reset() {
        this.setName();
    }
}

module.exports = Robot;

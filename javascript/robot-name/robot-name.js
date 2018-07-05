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

const max = asciis.keys.length ** padAlpha * digits.keys.length ** padDigit;

// generate all possible ids
var ids = [];
for (let i = 0; i < max; i++) {
    ids.push(i);
}
// then shuffle
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
var shuffledIds = shuffle(ids);

// python like divmod
function divmod(num, div) {
    return { quotient: Math.floor(num / div), remainder: num % div };
}

// convert decimal to int with custom base and symbols
function decToWhatever(dec, pad, lut) {
    let conv = "";
    for (c of parseInt(dec, 10).toString(lut.keys.length)) {
        conv += lut.vals[lut.keys.indexOf(c)];
    }
    return conv.padStart(pad, lut.vals[0]);
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
        let next = shuffledIds.pop();
        if (next === undefined) {
            throw new Error(
                "Le trop de robots est l'ennemi du mieux de robots"
            );
        }
        this.name = numToName(next);
    }

    getName() {
        return this.name;
    }

    reset() {
        this.setName();
    }
}

module.exports = Robot;

if (require.main === module) {
    const max = 26 ** 2 * 10 ** 3;
    let usedNames = [];
    for (let i = 0; i < max; i++) {
        var newRobot = new Robot();
        usedNames[newRobot.name] = true;
    }
}

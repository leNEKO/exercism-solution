// usuable modulo
function mod(n, m) {
    return ((n % m) + m) % m;
}

const alpha = "abcdefghijklmnopqrstuvwxyz".split("");
var by_keys = {};
for (k in alpha) {
    by_keys[alpha[k]] = k;
}


class Cipher {
    constructor(key) {

        if (key == undefined) {
            key = this.randomKey()
        } else if (key == '') {
            throw Error("Bad key");
        } else {
            for (k of key) {
                if (by_keys[k] == undefined) {
                    throw Error("Bad key");
                }
            }
        }
        this.key = key
    }

    randomKey(length = 128) {
        var key = "";
        while (key.length < length) {
            key += alpha[Math.floor(Math.random() * alpha.length)];
        }
        return key;
    }

    codec(str, dir = 1) {
        var encoded = "";
        var i;
        for (i = 0; i < str.length; i++) {
            var c = str[i]; // str char
            var k = this.key[i % this.key.length]; // key char
            var pos = parseInt(by_keys[c]);
            var offset = parseInt(by_keys[k]);
            var npos = mod(pos + offset * dir, alpha.length);
            var nc = alpha[npos];
            encoded += nc;
        }
        return encoded;
    }

    encode(str) {
        return this.codec(str, 1);
    }

    decode(str) {
        return this.codec(str, -1);
    }
}


module.exports = Cipher
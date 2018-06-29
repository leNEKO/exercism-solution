const ascii = "abcdefghijklmnopqrstuvwxyz";

class RotationalCipher {
    rotate(text, key) {
        let rotated = "";
        for (const c of text) {
            const clow = c.toLowerCase();
            const k = ascii.indexOf(clow); // index of current char
            let nc = ""; // rotated char
            if (k >= 0) {
                // if [a-z]
                const rk = (k + key) % ascii.length; // rotated index
                nc = ascii[rk];
                // keep the case
                if (clow.toUpperCase() === c) {
                    nc = nc.toUpperCase();
                }
            } else {
                // other symbols
                nc = c;
            }
            rotated += nc;
        }
        return rotated;
    }
}

module.exports = RotationalCipher;

if (require.main === module) {
    console.log(new RotationalCipher().rotate("ABCabc", 1));
}

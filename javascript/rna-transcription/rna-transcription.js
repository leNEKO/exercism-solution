class DnaTranscriber {
    constructor() { }

    toRna(str) {
        var map = {
            "G": "C",
            "C": "G",
            "T": "A",
            "A": "U",
        };

        var trs = "";
        for (var c of str.split("")) {
            if (c in map) {
                trs += map[c];
            } else {
                throw Error("Invalid input");
            }
        }
        return trs;
    }
}

module.exports.default = DnaTranscriber;
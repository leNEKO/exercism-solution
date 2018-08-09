class Queens {
    constructor(pos = { white: [0, 3], black: [7, 3] }) {
        this._white = pos.white;
        this._black = pos.black;
        if (pos.white[0] === pos.black[0] && pos.white[1] === pos.black[1]) {
            console.log("Queens cannot share the same space");
            //throw Error("Queens cannot share the same space");
        }
    }

    toString() {
        let board = [];
        const white = this._white;
        const black = this._black;

        for (const x in [...Array(8)]) {
            let line = [];
            for (const y in [...Array(8)]) {
                let char = "_";
                if (this._white[0] == x && this._white[1] == y) {
                    char = "W";
                }
                if (this._black[0] == x && this._black[1] == y) {
                    char = "B";
                }
                line.push(char);
            }
            board.push(line.join(" ") + "\n");
        }
        return board.join("");
    }

    canAttack() {
        // shortcuts
        const bx = this._black[0];
        const by = this._black[1];
        const wx = this._white[0];
        const wy = this._white[1];

        // horizontal attack
        if (bx === wx || by === wy) {
            return true;
        }
        // diagonnal attack
        const dx = Math.abs(bx - wx);
        const dy = Math.abs(by - wy);

        if (dx === dy) {
            return true;
        }

        return false;
    }
}

module.exports = Queens;

if (require.main === module) {
    pos = { white: [2, 4], black: [2, 7] };
    q = new Queens(pos);
    console.log(q.toString());
}

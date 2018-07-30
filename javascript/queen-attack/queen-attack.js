class Queens {
    constructor(pos = { white: [0, 3], black: [7, 3] }) {
        this.white = pos.white
        this.black = pos.black
        if (pos.white[0] === pos.black[0] && pos.white[1] === pos.black[1]) {
            console.log("Queens cannot share the same space")
            // throw Error("Queens cannot share the same space")
        }
    }
    toString() {
        let board = []
        const white = this.white
        const black = this.black

        for (const x in [...Array(8)]) {
            let line = []
            for (const y in [...Array(8)]) {
                if this.
            }
            board.push(line)
        }
    }
}

// class Queen {
//     constructor(x, y) {
//         this.coord = [x, y]
//     }

//     canAttack(another) {
//         x, y = this.coord
//         ax, ay = another.coord
//     }
// }

module.exports = Queens

if (require.main === module) {
    q = new Queens({ white: [0, 3], black: [0, 3] })
    q.toString()
}
class Triangle {
    constructor(size) {
        this.rows = [[1]]; // init the triangle top
        for (let y = 1; y < size; y++) {
            this.lastRow = []; // a new row
            for (let x = 0; x <= y; x++) {
                const up = this.rows[y - 1]; // previous row
                const left = up[x - 1] || 0;
                const right = up[x] || 0;
                this.lastRow.push(left + right);
            }
            this.rows.push(this.lastRow);
        }
    }
}

module.exports = Triangle;

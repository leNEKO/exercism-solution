class Matrix {
    constructor(str) {
        this.rows = [];
        this.columns = [];

        // fill the rows array
        for (var row_str of str.split("\n")) {
            var row = row_str.split(" ").map(function(t) {
                return parseInt(t);
            });
            this.rows.push(row);
        }

        // fill the columns array
        for (var y in this.rows) {
            for (var x in this.rows[y]) {
                // create empty colum array if undefined
                if (this.columns[x] == undefined) {
                    this.columns[x] = [];
                }
                // x, y <- y, x
                this.columns[x][y] = this.rows[y][x];
            }
        }
    }
}

module.exports = Matrix;

if (require.main === module) {
    new Matrix("0 1 2\n3 4 5");
}

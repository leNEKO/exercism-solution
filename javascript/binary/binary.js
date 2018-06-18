class Binary {
  constructor(str) {
    this.str = str;
  }
  // better :)
  toDecimal(mode = 2) {
    var pos = this.str.split("").reverse();
    var total = 0;
    for (var pow in pos) {
      var val = pos[pow];
      total += val * mode ** pow;
    }
    return this.str.match(/[^0-1]/) ? 0 : total;
  }
}

module.exports = Binary;

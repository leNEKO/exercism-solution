class Gigasecond {
  constructor(date) {
    this.giga = new Date(date.getTime() + 1e12); // getting rid of UTC daylight saving confusion
  }

  date() {
    return this.giga;
  }
}

module.exports = Gigasecond;

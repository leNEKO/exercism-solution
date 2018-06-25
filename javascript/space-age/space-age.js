const earth_year = 31557600;
const ratios = {
    Earth: 1,
    Mercury: 0.2408467,
    Venus: 0.61519726,
    Mars: 1.8808158,
    Jupiter: 11.862615,
    Saturn: 29.447498,
    Uranus: 84.016846,
    Neptune: 164.79132
};

class SpaceAge {
    constructor(seconds) {
        this.seconds = seconds;
        for (var k in ratios) {
            let ratio = ratios[k];
            let years = seconds / (earth_year * ratio);
            // cool, i can now get rid of this new Function("…") hackish trick
            this["on" + k] = function() {
                return parseFloat(years.toFixed(2));
            };
        }
    }
}

module.exports = SpaceAge;

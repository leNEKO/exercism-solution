"use strict";
exports.__esModule = true;
exports.decodedResistorValue = void 0;
var COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
];
function decodedResistorValue(_a) {
    var colorA = _a[0], colorB = _a[1], colorC = _a[2];
    var value = (parseInt("".concat(COLORS.indexOf(colorA)).concat(COLORS.indexOf(colorB)), 10)
        * (Math.pow(10, COLORS.indexOf(colorC))));
    var suffix;
    if (value > 1000) {
        value *= .001;
        suffix = 'kiloohms';
    }
    else {
        suffix = 'ohms';
    }
    return "".concat(value, " ").concat(suffix);
}
exports.decodedResistorValue = decodedResistorValue;

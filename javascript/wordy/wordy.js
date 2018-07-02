var ArgumentError = function() {};

var operatorMap = {
    plus: function(a, b) {
        return Number(a) + Number(b);
    },
    minus: function(a, b) {
        return a - b;
    },
    multiplied: function(a, b) {
        return a * b;
    },
    divided: function(a, b) {
        return a / b;
    }
};
var isValidOperator = function(operator) {
    return Object.keys(operatorMap).indexOf(operator) > -1;
};

var WordProblem = function(question) {
    var operators = [];
    var operands = [];
    var words = question
        .replace("What is ", "")
        .replace(/by/g, "")
        .replace("?", "")
        .match(/\S+/g);
    words.forEach(function(word, index) {
        index % 2 === 0 ? operands.push(word) : operators.push(word);
    });

    var answer = function() {
        if (!operators.every(isValidOperator)) {
            throw new ArgumentError();
        }
        return operators.reduce(function(total, operator) {
            total = operatorMap[operator](operands.shift(), operands.shift());
            operands.unshift(total);
            return total;
        }, 0);
    };

    return { answer };
};

module.exports = {
    ArgumentError: ArgumentError,
    WordProblem: WordProblem
};

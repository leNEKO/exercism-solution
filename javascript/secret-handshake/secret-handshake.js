// configuration as an object for easy reading
const actions = {
    0b10000: "REVERSE",
    0b01000: "jump",
    0b00100: "close your eyes",
    0b00010: "double blink",
    0b00001: "wink",
};

class SecretHandshake {
    constructor(num) {
        // must be a valid number
        if (typeof (num) !== "number") {
            throw new Error("Handshake must be a number");
        }

        // init values
        this.list = [];
        let reverse = false;

        // as object are unordered, we need to convert it as an array
        var orderedActions = [];
        for (let val in actions) {
            orderedActions.unshift({ "id": parseInt(val), "val": actions[val] });
        }

        // then go trough the actions
        for (let action of orderedActions) {
            while ((num - action.id) >= 0) {
                if (action.val === "REVERSE") {
                    reverse = !reverse;
                } else {
                    this.list[reverse ? "push" : "unshift"](action.val);
                }
                num -= action.id
            }
        }
    }

    commands() {
        return this.list;
    }
}

module.exports = SecretHandshake;

if (require.main === module) {
    console.log(new SecretHandshake(19))
}
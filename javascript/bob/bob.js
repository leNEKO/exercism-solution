class Bob {
    constructor() {
        this.brain = {
            0b100: "Sure.",
            0b010: "Whoa, chill out!",
            0b110: "Calm down, I know what I'm doing!",
            0b111: "Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn",
            0b001: "Fine. Be that way!",
            0b000: "Whatever.",
        };
    }

    hey(message) {
        var message = message.trim();
        var state = 0b000;

        // anything
        if (!message) {
            state += 0b001;
        } else {

            // is question
            if (message.slice(-1) === "?") {
                state += 0b100;
            }

            // is yelling
            var letters = message.replace(/[^a-z]/gi, '');
            if (letters && (letters.toUpperCase() === letters)) {
                state += 0b010;
            }
        }

        return this.brain[state];

    }

}

module.exports = Bob
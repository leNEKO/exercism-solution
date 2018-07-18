class List {
    constructor() {
        this.values = [];
    }

    append(data) {}
}

module.exports = List;

if (require.main === module) {
    l = new List();
    console.log(l);
    l.append(new List());
    console.log(l);
}

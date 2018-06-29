class School {
    constructor(name) {
        this.name = name;
        this.db = {};
    }

    roster() {
        return this.db;
    }

    grade(n) {
        return this.db[n] || [];
    }

    add(student, n) {
        if (this.db[n] === undefined) {
            this.db[n] = [];
        }
        this.db[n].push(student);
        this.db[n].sort();
    }
}

module.exports = School;

if (require.main === module) {
    let s = new School("Leader of the New School");
    s.add("Busta Rhymes", 1);
    s.add("Charlie Brown", 1);
    s.add("Dinco D", 1);
    s.add("Cut Monitor Milo", 1);
    console.log(s);
}

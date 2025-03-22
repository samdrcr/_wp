export class Animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        return `I am ${this.name}`;
    }
}
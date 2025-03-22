export class Vector {
    constructor(components) {
        this.components = components;
    }
    add(other) {
        return new Vector(this.components.map((val, i) => val + other.components[i]));
    }
    sub(other) {
        return new Vector(this.components.map((val, i) => val - other.components[i]));
    }
    dot(other) {
        return this.components.reduce((sum, val, i) => sum + val * other.components[i], 0);
    }
}
let a = new Vector([1, 2, 3]);
let b = new Vector([4, 5, 6]);
console.log(a.add(b).sub(b).dot(b));
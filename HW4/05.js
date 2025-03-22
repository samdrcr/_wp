import { Animal } from "./Animal.js";
export class Dog extends Animal {
    speak() {
        return `Woof! I am ${this.name}`;
    }
}
const dog = new Dog("Buddy");
console.log(dog.speak());
function Challenge(age, first, color) {
    this.firstName = first;
    this.age = age;
    this.eyeColor = color;
}
const Person = new Challenge(34, "Matt", "brown");

console.log(Person);
"""
class Dog {
  constructor(name) {
    this._name = name;
    this._behavior = 0;
  }

  get name() {
    return this._name;
  }
  get behavior() {
    return this._behavior;
  }   

  incrementBehavior() {
    this._behavior ++;
  }
}
"""

class Dog: 
    def __init__(self, name):
        self._name = name
        self._behavior = 0

    @property
    def name(self):
        return self._name

    @property
    def behavior(self):
        return self._behavior
    
    def increment_behavior(self):
        self._behavior += 1

"""
const halley = new Dog('Halley');
console.log(halley.name); // Print name value to console
console.log(halley.behavior); // Print behavior value to console
halley.incrementBehavior(); // Add one to behavior
console.log(halley.name); //Print name value to console
console.log(halley.behavior); // Print behavior value to console
"""

halley = Dog("Halley")
print(halley.name)
print(halley.behavior)
halley.increment_behavior()             
print(halley.name)
print(halley.behavior)
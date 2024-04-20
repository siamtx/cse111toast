const button = document.querySelector("button");

/*button.addEventListener("click", updateName);

/*function updateName() {
/*  const name = prompt("Enter a new name");
/*  button.textContent = `Player 1: ${name}`;
/*} */

const person = {
    name: {
        first:"Bob",
        last: "Smith",
    },
    age: 32,
    bio: function() {
      console.log(`${this.name.first} ${this.name.last} is ${this.age} years old.`);
    },
    introduceSelf: function() {
      console.log(`Hi! I'm ${this.name.first}.`);
    },
  };

  const myDataName = "height";
  const myDataValue = "1.75m";
  person[myDataName] = myDataValue;


  function Person(name) {
    this.name = name;
    this.introduceSelf = function () {
      console.log(`Hi! I'm ${this.name}.`);
    };
  }
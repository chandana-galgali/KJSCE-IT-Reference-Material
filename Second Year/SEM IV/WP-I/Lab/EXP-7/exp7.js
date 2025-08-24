// Activity 1: Convert JSON objects into a string using JSON.stringify()
const person = {
    name: "Chandana Galgali",
    age: 19,
    city: "Mumbai"
};

const personJSON = JSON.stringify(person);
console.log("JSON String:", personJSON);

// Activity 2: Replace any data in JSON object. There's no JSON.replace(), so we modify the object itself
let personParsed = JSON.parse(personJSON);
personParsed.age = 22;
personParsed.city = "New Jersey";

// Then convert it back to a JSON string
const modifiedPersonJSON = JSON.stringify(personParsed);
console.log("Modified JSON String:", modifiedPersonJSON);

// Activity 3: Convert valid JSON string into JSON using JSON.parse()
const finalPersonObject = JSON.parse(modifiedPersonJSON);
console.log("Final Person Object:", finalPersonObject);
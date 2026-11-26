// version: 1.0

values = ["love", "happiness", "security", "kindness", "justice"]
esteem = ["enough", "worthy", "special", "rich", "beautiful"]
optimism = ["faith", "resilience", "forgivingness", "positivity", "acceptance"]

strOne = "Today I shall value ";
strTwo = "I am ";
strThree = "I practice "

randomInt = (max) => {
    return Math.floor(Math.random() * max);
}

message = () => {
    sentOne = strThree + optimism[randomInt(optimism.length)] + ".";
    sentTwo = " " + strOne + values[randomInt(values.length)] + ".";
    sentThree = " " + strTwo + esteem[randomInt(esteem.length)] + "!";
    return sentOne + sentTwo + sentThree;
}

console.log(message())
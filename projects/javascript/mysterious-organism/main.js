// Returns a random DNA base
const returnRandBase = () => {
  const dnaBases = ['A', 'T', 'C', 'G'];
  return dnaBases[Math.floor(Math.random() * 4)];
};

//console.log(returnRandBase());

// Returns a random single stand of DNA containing 15 bases
const mockUpStrand = () => {
  const newStrand = [];
  for (let i = 0; i < 15; i++) {
    newStrand.push(returnRandBase());
  }
  return newStrand;
};

//console.log(mockUpStrand())

const pAequorFactory = (num, dna) => {
  return {
    specimenNum: num,
    dna: dna,
    mutate() {
      const randIndex = Math.floor(Math.random() * this.dna.length);
      console.log(randIndex)
      let newBase = returnRandBase();
      console.log("new base", newBase)
      while (newBase === this.dna[randIndex]) {
        newBase = returnRandBase();
        console.log(newBase)
      }
      this.dna[randIndex] = newBase;
      return this.dna;
    },
    compareDNA(otherOrg) {
      let common = 0;
      for (let i = 0; i < this.dna.length; i++) {
        if (this.dna[i] === otherOrg.dna[i]) {
          common++;
        }
      }
      const percent = Math.round((common / this.dna.length * 100) * 100) / 100;
      console.log(`specimen #${this.specimenNum} and specimen #${otherOrg.specimenNum} have ${percent}% DNA in common.`);
    },
    willLikelySurvive() {
      const cAndGBases = this.dna.filter(base => base === 'C' || base === 'G');
      return (cAndGBases.length / this.dna.length) >= 0.6;
    }
  };
};

const originalDna = mockUpStrand();
const specimen = pAequorFactory(1, [...originalDna]);
console.log('Original DNA:', specimen.dna.join(''));
specimen.mutate();
console.log('Mutated DNA: ', specimen.dna.join(''));

const specimen2 = pAequorFactory(2, mockUpStrand());
specimen.compareDNA(specimen2);

console.log('Specimen 1 will survive:', specimen.willLikelySurvive());
console.log('Specimen 2 will survive:', specimen2.willLikelySurvive());

survingSpecimen = [];
let specimenNum = 3;

while (survingSpecimen.length < 30) {
  const newSpecimen = pAequorFactory(specimenNum, mockUpStrand());
  if (newSpecimen.willLikelySurvive()) {
    survingSpecimen.push(newSpecimen);
  }
  specimenNum++;
}
console.log(`Created ${survingSpecimen.length} surviving specimens!`);


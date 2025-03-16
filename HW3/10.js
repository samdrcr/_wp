let studentScores = { Alice: 85, Bob: 92, Charlie: 78 };
for (let student in studentScores) {
    console.log(`${student} 的分數是 ${studentScores[student]}`);
}
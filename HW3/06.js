function computeFactorial(num) {
    if (num <= 1) return 1;
    return num * computeFactorial(num - 1);
}
console.log(computeFactorial(5));
function solution(a, b) {    
    let plusOne = parseInt(a.toString() + b.toString());
    
    let threeMultiply = 2 * a * b;
    
    if (plusOne >= threeMultiply) {
        return plusOne;
    }
    else {
        return threeMultiply;
    }
}
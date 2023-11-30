function solution(string) {
    let answer = '';
    // loop through string
    for(let i = 0; i < string.length; i++){
      // initialize variable to current iteration
      const currentIteration = string[i];
      // conditional if the current iteration is uppercase
      if(currentIteration === currentIteration.toUpperCase()) {
        // add a empty space concatenated with the current iteration
        answer += ' ' + currentIteration;
      } else {
        // else just return the current iteration
        answer += currentIteration;
      }}
    return answer
  }
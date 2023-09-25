let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

const test = Number(input[0])
let n = 0
let arr = []
for(let i=1;i<=test;i++) {
  n = Number(input[i])
  arr = []
  for(let k=1; k<=n; k++) arr.push(k)
  dfs([], 0)
  console.log()
}

function dfs(result, depth) {
  if(depth == n-1) {
    let str = ''
    for(let i=0; i< n-1; i++) str+= arr[i] + result[i]
    str+= arr[n-1] + ''
    current = eval(str.split(' ').join(''))
    if(current == 0) console.log(str)
    return
  }

  for(let x of [' ', '+', '-']) {
    result.push(x)
    dfs(result, depth + 1)
    result.pop()
  }
}
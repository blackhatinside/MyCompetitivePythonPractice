// https://www.codechef.com/problems/TALLER
let fs = require("fs");
let data = fs.readFileSync(0, "utf-8");
let idx = 0;
data = data.split("\n");
function input() {
  return data[idx++];
}

let tcs = parseInt(input());
for (let tc = 0; tc < tcs; tc++) {
    let xy = input().split(" ");
    console.log((xy[0] > xy[1] ? "A" : "B"));
}

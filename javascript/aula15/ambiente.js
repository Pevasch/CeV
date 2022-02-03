let num = [5,8,2,9,3]
num.push(6)
num[6] = 1

console.log(`Nosso vetor é o ${num}`)
console.log(`O vetor tem ${num.length} posições`)

let inopos = num.indexOf(6)
console.log(`O valor 6 está na posição ${inopos}`)

console.log(`O vetor na ordem é assim: ${num.sort()}`)

/*
for (let pos = 0; pos < num.length; pos++) {
    console.log(num[pos])
}
*/

let pos = num.indexOf(6)
console.log(`O valor 6 agora está na posição ${pos}`)

for (let pos in num) {
    console.log(num[pos])
}

function pira(height) {
    // let height = prompt("높이를 입력하세요");
let r = "";
    for (let i = 1; i <= height; i++) {
        for(let z = 1; z <= height-i; z++){
            r += " ";
        }
        for (let j = 1; j <= i*2-1; j++) {
            r += "*";
        }
        for(let q = 1; q <= height-i; q++){
            r += " ";
        }
        r += "\n";
    }
    console.log(r);
}
pira(7);

function c(callback){
    for(let i = 0; i < 10; i++){
        callback();
    }
}

let callback = () =>{
    console.log("Hello!")
};

// c(callback);

c(() => {
    console.log("hello")
});
let times;
function displayHello(){
    times = setInterval(() => {
        console.log("Hello!");
    }, 3000);
}

displayHello();

let num = [1, 2, 3, 4, 5];
num.unshift(1);
// console.log(num);

let nam = {'a': 10, 'b' : 20, 'c' : 30};
for(key in nam){
    console.log(key);
}
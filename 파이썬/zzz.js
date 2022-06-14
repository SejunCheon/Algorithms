let user = [1, 2, 3, 4, 5, 6, 7, 8];

let userList = [
  { name: "mike", age: 30 },
  { name: "kay", age: 19 },
  { name: "brory", age: 22 },
];

let userName = ["mike", "kay", "brory"];

let arr = [27, 8, 5, 13];

arr.sort((a, b) => {
  return a - b;
});

let result = userList.reduce((acc, cur) => {
  if (cur.age > 19) {
    acc.push(cur.name);
  }
  return acc;
}, []);

let [user1, user2, user3] = userName;

function showName(...num) {
  let result = num.reduce((n, cur) => n + cur);
  // console.log(result);
}

function User(name, age, ...skils) {
  this.name = name;
  this.age = age;
  this.skils = skils;
}

const sana = new User("사나", 26, "코딩", "일본어", "한국어");
const 카카로트 = new User("손오공", 999, "초사이언", "에네르기파");

let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];
let arrResult = [...arr2, ...arr1];

function makeCounter() {
  let num = 0;

  return function () {
    return num++;
  };
}

let counter = makeCounter();
console.log(counter());
console.log(counter());

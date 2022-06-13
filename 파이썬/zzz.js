let user = [1, 2, 3, 4, 5, 6, 7, 8];

let userList = [
  { name: "mike", age: 30 },
  { name: "kay", age: 19 },
  { name: "brory", age: 22 },
];

let result = userList.map((user, index) =>
  Object.assign({}, user, { id: index + 1, isAdult: user.age > 19 })
);

let arr = ["브로리,카카로드,배지터"];

let result2 = arr.split(",");

console.log(result2);

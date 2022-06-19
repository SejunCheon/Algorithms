a = [1, 1, 2, 2, 7, 8, 8];
b = [0, 1, 3, 1, 0];
c = [1, 1, 5];

function findUniqueNumber(arr) {
  let i = 0;
  a = arr.sort();
  console.log("자르기 전 배열 : " + a);
  let result = [];
  while (i < a.length) {
    if (a[0] !== a[1]) {
      result = a.shift(a[i]);
      console.log("혼자인 숫자 : " + result);
      break;
    }
    a.splice(0, 2);
    result = a;
    console.log("자른 후 배열 : " + result);
    i++;
  }
  console.log("혼자있는 숫자 : " + result);
}

findUniqueNumber(a);

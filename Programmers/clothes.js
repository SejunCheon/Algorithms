function solution(n, lost, reserve){
    var answer = 0;
    let arr = [];

    for(let i = 1; i <= n; i++){
        arr.push(1); // 체육복을 1추가한다
        if(reserve.includes(i)){ // 체육복을 2개 가지고 온 학생이라면
            arr[i-1]++; // 1개 추가한다. 학생번호와 index는 다르다.
        }else if(lost.includes(i)){
            arr[i-1]--; // 1개를 뺀다.
        }
    }
    for(let i = 0; i < n; i++){
        if(!arr[i]){ // 0은 falsy 한 값이기 때문에 !를 붙여주면 truthy한 값이 된다. (arr[i] === 0) 과 같다.
            if(arr[i-1]===2){ // 앞에 있는 학생이 체육복을 2개 가지고 있다면
                arr[i]++; // 내꺼 하나 플러스
                arr[i-1]--; // 뒤에 있는 학생 하나 마이너스
            }else if(arr[i+1]===2){
                arr[i]++; // 내꺼 하나 플러스
                arr[i+1]--; // 뒤에 있는 학생 하나 마이너스
            }
        }
    }
    for(let i = 0; i < n; i++){
        if(arr[i] >= 1){
            answer++;
        }
    }
    // console.log(arr);
    console.log(answer);
}
let lost = [2,4];
let reserve = [1,3,5];

let reserve2 = [3];

let lost2 = [3];
let reserve3 = [1];
solution(3, lost2, reserve3);
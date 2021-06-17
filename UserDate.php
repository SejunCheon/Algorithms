<?php
    // require_once : 포함할 파일이 없으면 다음 코드로 넘어가지 않는다
    require_once('conn.php'); 
    require_once('res.php');
    
    // json 디코드 순수데이터를 전달받음
    $req = json_decode(file_get_contents("php://input"));


    // 날짜와 학번을 입력하면 해당되는 DB데이터출력
    function DateUser($arg){

    $dbConect = dbCone();  // DB연결이 가능하도록 짜여진 코드를 불러온 것
    
    $sql = "SELECT * FROM attendance_status WHERE date = '$arg->date' && m_id = $arg->m_id";

        // $result = $dbConect->query($sql); # sql문 실행
        
        if($result = $dbConect->query($sql)){
            
            return $result->fetch_row(); // 해당되는 DB데이터가 배열로 차례차례 출력
        }
            $dbConect->close();
            return null; // 잘못된 값일시 null 출력
    }
        

    $resData = DateUser($req);  
   
    $res = new Res(($resData != null ? true : false), $resData);  // 연결이 성공하면 값과 성공문구 출력    

    // # json 엔코드를 했을 때 한글만 깨지는현상이 발생해 쓴코드 
    echo json_encode($resData, JSON_UNESCAPED_UNICODE); 
    // echo json_encode($res);
?>
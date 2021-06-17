<?php
    // 시간 헤더 설정하기
    date_default_timezone_set('Asia/Seoul');

    // require_once : 포함할 파일이 없으면 다음 코드로 넘어가지 않는다
    require_once('conn.php');
    require_once('res.php');

    // json 디코드 순수데이터를 전달받음
    $req = json_decode(file_get_contents('php://input'));

    // 오후6시이후 출석을 안한 인원에 대한 자동으로 결석처리
    function UserAbsentStatus($arg){
    
    $dbConn = dbCone();

    $dateTarget = date("Y-m-d",strtotime("-4 months")); // 현재 날짜에서 4개월을 뺀 날짜
    $dateNow = date("Y-m-d", strtotime('-1 days')); // 현재 날짜 - 1일

    // 현재 날짜에서 4개월은 뺀 날로부터 현재 날짜 -1일 에대한 데이터중 가장최근 날짜 조회
    $sql = "SELECT date FROM attendance_status where m_id = $arg->m_id  && $dateTarget < date <= $dateNow && status = '출석' order by date DESC";

        if($result = $dbConn->query($sql)){

            $dataResult = $result->fetch_assoc();
            
            // $dateResult값을 넣으면 빈값이 나오기때문에 문자열 로변환
            $newDate = implode('', $dataResult); // Select문 문자열로 변환
            $newDate2 = date("Y-m-d", strtotime($newDate)); // 문자열 데이트로 변환
            $newDate3 = date("Y-m-d", strtotime($newDate2."+1day")); // 데이트에 +1일 더해서 변환

            // Select한 날짜부터 현재-1일 까지 반복을 통하여 결석값을 넣어준다
            for($i = $newDate3; $i < $dateNow; $i++){
                // 출석현황 데이터에 날짜 + 결석 + 학번을 추가해준다
                $sql2 = "INSERT INTO attendance_status (date, status, m_id) values ('$i', '결석', '$arg->m_id')";

                $result2 = $dbConn->query($sql2);
            }
            // $dbConect->close();
            return null;
        }
    }

    $resdata= UserAbsentStatus($req);

    // 연결이 성공하면 값과 성공문구 출력    
    $res = new Res(($resdata != null ? true : false), $resdata);

    //  json 엔코드를 했을 때 한글만 깨지는현상이 발생해 쓴코드 
    echo json_encode($resdata, JSON_UNESCAPED_UNICODE);
?>
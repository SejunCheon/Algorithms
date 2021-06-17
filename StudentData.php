<?php
require_once('conn.php');
require_once('res.php');

$req = json_decode(file_get_contents("php://input"));

function StudentData($arg){

    $dbConect = deCone();

    $sql = "SELECT * FROM attendance_status WHERE m_id = $arg->m_id";

    if($result = $dbConect->query($sql)){
        return $result->fetch_assoc();
    }

    // $dbConect->close();
    // return null;
    return null;
}

$resData = Student_Data($req);

$res = new Res(($resData != null ? true : false), $resData);

echo json_encode($resData, JSON_UNESCAPED_UNICODE);
?>
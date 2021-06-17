<?php
require_once('conn.php');
require_once('res.php');

$req = json_decode(file_get_contents("php://input"));

function Student_Data($arg){
    $dbConect = deCone();

    $sql = "SELECT * FROM attendance_status WHERE date = '$arg->date'";

    if($result = $dbConect->query($sql)){
        return $result->fetch_all();
    }

    // $dbConect->close();
    // return null;
}

$resData = Student_Data($req);

$res = new Res(($resData != null ? true : false), $resData);

echo json_encode($resData, JSON_UNESCAPED_UNICODE);
?>
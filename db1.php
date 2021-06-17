<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    $servername = "localhost";
    $dbname = "testDB";
    $user = "SejunCheon";
    $password = "72339900";

    try{
        $conn = new PDO('mysql:host=$servername;dbname=$dbname',$user,$password);
        $conn = setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $sql = "CRATE DATABASE Hotel";
        $conn->exec($sql);
        echo "데이터베이스 생성 성공!";
    }catch(PDOException $ex){
        echo "데이터베이스 생성 실패!:".$ex->getMessage()."<br>";
    } 
    $conn = null;
    ?>
</body>
</html>
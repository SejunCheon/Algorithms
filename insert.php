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
        $conn = mysqli_connect("localhost", "root", "72339900","opentutorials");
        $sql = "
        INSERT INTO topic (
            title,
            description, 
            created
        ) VALUE(
            'MySQL',
            'MySQL is ..',
            NOW()
     )";
    $result = mysqli_query($conn, $sql);
    if($result === false){
        echo mysqli_error($conn);
    }

    ?>
</body>
</html>
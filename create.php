<?php
$conn = mysqli_connect(
    't',
    '',
    '',
    '');

$sql = "SELECT * FROM topic";
$result = mysqli_query($conn, $sql);
$list = '';
while($row = mysqli_fetch_array($result)){
    $list = $list."<li><a 
    href=\"index.php?id={$row['id']}\">{$row['title']}</a></li>";    
}

$article = array(
    'title'=>'Welcome',
    'description'=>'Hello, Web'
    );
if(isset($_GET['id'])){
$filtered_id = mysqli_real_escape_string($conn, $_GET['id']);
$sql = "SELECT * FROM topic where id={$_GET['id']}";  
$result = mysqli_query($conn, $sql);
$row = mysqli_fetch_array($result);
$article['title'] = $row['title'];
$article['description'] = $row['description'];
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>create.php</title>
</head>
<body>
    <h1>WEB</h1>
    <ol>
        <?=$list?>
    </ol>
    <a href="create.php">create</a>
    <form action="process_create.php" method="POST">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea name="description" placeholder="description"></textarea></p>
        <p><input type="submit"></p>
    </form>
</body>
</html>

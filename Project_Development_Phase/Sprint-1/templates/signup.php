<?php

header('Location:Login.html');
$host = "localhost";
$dbusername = "root";
$dbpassword = "";
$dbname = "web";

$conn = new mysqli ($host, $dbusername, $dbpassword, $dbname);
if (!$conn){
    die("connection failed:" . mysqli_connect_error());
}
if (isset($_POST['register'])){
    
    $name = $_POST['name'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $sql_query = "INSERT INTO signup (name, email, password)values('$name', '$email', '$password')";
    if (mysqli_query($conn, $sql_query)){
        echo "Registered successfully";
    }
    else{
        echo "error:" . $sql . "" . mysqli_error($conn);

    }
    mysqli_close($conn);
}
?>
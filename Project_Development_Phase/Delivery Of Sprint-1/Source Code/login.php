<?php
    
    
    $conn = new mysqli("localhost", "root", "", "web");
    
    if ($conn->connect_error){
        die("failed to connect:".$conn->connect_error);

    }
    if (isset($_POST['Login'])){

        $email = $_POST['email'];
        $password = $_POST['password'];
        $stmt = $conn->prepare("SELECT * FROM signup where email = ?");
        $stmt->bind_param("s", $email);
        $stmt->execute();
        $stmt_result = $stmt->get_result();
        if($stmt_result->num_rows > 0){
            $data = $stmt_result->fetch_assoc();
            if ($data['password'] === $password){
                echo "login successfully";
                header('Location:disease.html');
            }
            else{
                echo "invalid password";
            }
        }
        else{
                echo "invalid email or password";
            }
            mysqli_close($conn);
          
        
    }
?>
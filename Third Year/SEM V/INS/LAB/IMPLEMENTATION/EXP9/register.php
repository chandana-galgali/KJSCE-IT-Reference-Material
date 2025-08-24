<?php

$conn = new mysqli('localhost', 'root', '', 'Register_Page');
if ($conn->connect_error){
    die('Connection Failed: '. $conn->connect_error);
}

function encrypt_shift_cipher($password, $key){
    $encrypted_password = "";
    for ($i = 0; $i < strlen($password); $i++){
        if (ctype_upper($password[$i]))
            $base = 'A';
        else
            $base = 'a';
        $encrypted_password .= chr(((ord($password[$i]) - ord($base) + $key) % 26) + ord($base));
    }
    return $encrypted_password;
}

$username = $_POST['username'];
$password = $_POST['password'];
$key = (int) $_POST['key'];

$encrypted_password = encrypt_shift_cipher($password, $key);

$stmt = $conn->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
$stmt->bind_param("ss", $username, $encrypted_password);

if ($stmt->execute()) {
    echo "Registration successful!";
} else {
    echo "Error: " . $stmt->error;
}

$stmt->close();
$conn->close();
?>

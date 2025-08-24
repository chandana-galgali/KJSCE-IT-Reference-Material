<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Perfume Store - Session Handling</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #E0F7FA;
            margin: 0;
            padding: 20px;
        }
        .container {
            width: 50%;
            margin: auto;
            background: #F3E5F5;
            padding: 30px;
            box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
            border-radius: 15px;
        }
        .header {
            text-align: center;
            padding: 15px;
            background: #B3E5FC;
            color: #37474F;
            border-radius: 10px;
            font-size: 24px;
            font-weight: bold;
            letter-spacing: 2px;
        }
        .message {
            text-align: center;
            margin: 25px 0;
            font-size: 20px;
            color: #5C6BC0;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="header">
        <h1>Welcome to Perfume Paradise</h1>
    </div>

    <?php
    session_start();

    // Set a session variable for favorite perfume
    if(!isset($_SESSION["fav_perfume"])) {
        $_SESSION["fav_perfume"] = "Aqua Di Gio"; // default favorite perfume
        echo "<div class='message'>Welcome! We have set your favorite perfume to " . $_SESSION["fav_perfume"] . ".</div>";
    } else {
        echo "<div class='message'>Welcome back! Your favorite perfume is " . $_SESSION["fav_perfume"] . ".</div>";
    }
    ?>

</div>
</body>
</html>
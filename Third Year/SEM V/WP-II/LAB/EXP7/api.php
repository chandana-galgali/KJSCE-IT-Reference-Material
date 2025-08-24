<?php
header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

$server = "localhost";
$username = "root";
$password = "";
$dbname = "perfumes_db";

// Connect to the database
$conn = new mysqli($server, $username, $password, $dbname);
if ($conn->connect_error) {
    die(json_encode(["error" => "Connection failed: " . $conn->connect_error]));
}

// Helper function to get JSON input data
function getInput() {
    return json_decode(file_get_contents("php://input"), true);
}

$method = $_SERVER['REQUEST_METHOD'];
$path = explode('/', trim($_SERVER['PATH_INFO'], '/'));

// READ: Retrieve all perfumes or a specific perfume by ID
if ($method == 'GET' && $path[0] == 'perfumes') {
    $id = isset($path[1]) ? intval($path[1]) : 0;
    $sql = $id ? "SELECT * FROM perfumes WHERE id = $id" : "SELECT * FROM perfumes";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        $perfumes = [];
        while($row = $result->fetch_assoc()) {
            $perfumes[] = $row;
        }
        echo json_encode($perfumes);
    } else {
        echo json_encode(["message" => "No perfumes found"]);
    }

// CREATE: Add a new perfume
} elseif ($method == 'POST' && $path[0] == 'perfumes') {
    $data = getInput();
    $name = $data['name'];
    $brand = $data['brand'];
    $price = $data['price'];
    $description = $data['description'];

    $sql = "INSERT INTO perfumes (name, brand, price, description) VALUES ('$name', '$brand', '$price', '$description')";
    if ($conn->query($sql) === TRUE) {
        echo json_encode(["message" => "Perfume added successfully"]);
    } else {
        echo json_encode(["error" => "Error: " . $conn->error]);
    }

// UPDATE: Update an existing perfume by ID
} elseif ($method == 'PUT' && $path[0] == 'perfumes' && isset($path[1])) {
    $data = getInput();
    $id = intval($path[1]);
    $name = $data['name'];
    $brand = $data['brand'];
    $price = $data['price'];
    $description = $data['description'];

    $sql = "UPDATE perfumes SET name='$name', brand='$brand', price='$price', description='$description' WHERE id=$id";
    if ($conn->query($sql) === TRUE) {
        echo json_encode(["message" => "Perfume updated successfully"]);
    } else {
        echo json_encode(["error" => "Error: " . $conn->error]);
    }

// DELETE: Delete a perfume by ID
} elseif ($method == 'DELETE' && $path[0] == 'perfumes' && isset($path[1])) {
    $id = intval($path[1]);
    $sql = "DELETE FROM perfumes WHERE id=$id";
    if ($conn->query($sql) === TRUE) {
        echo json_encode(["message" => "Perfume deleted successfully"]);
    } else {
        echo json_encode(["error" => "Error: " . $conn->error]);
    }

// Invalid request
} else {
    echo json_encode(["error" => "Invalid request"]);
}

$conn->close();
?>
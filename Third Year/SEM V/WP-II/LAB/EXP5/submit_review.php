<?php
// Database configuration
$host = 'localhost';
$dbname = 'perfume_store';
$user = 'root';
$pass = '';

try {
    // Connect to the database
    $dbh = new PDO("mysql:host=$host;dbname=$dbname", $user, $pass);
    $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Insert form data into the 'reviews' table
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $perfume_name = $_POST['perfume_name'];
        $reviewer_name = $_POST['reviewer_name'];
        $rating = $_POST['rating'];
        $review_text = $_POST['review_text'];

        $sql = "INSERT INTO reviews (perfume_name, reviewer_name, rating, review_text) 
                VALUES (:perfume_name, :reviewer_name, :rating, :review_text)";
                
        $stmt = $dbh->prepare($sql);
        $stmt->bindParam(':perfume_name', $perfume_name);
        $stmt->bindParam(':reviewer_name', $reviewer_name);
        $stmt->bindParam(':rating', $rating);
        $stmt->bindParam(':review_text', $review_text);
        $stmt->execute();

        echo "<p style='color:green; text-align:center;'>Thank you for your review!</p>";
    }
} catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
}
?>
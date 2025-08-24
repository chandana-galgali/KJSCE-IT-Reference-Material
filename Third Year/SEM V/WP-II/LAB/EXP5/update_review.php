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

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        // Get form data
        $id = $_POST['id'];
        $rating = $_POST['rating'];
        $review_text = $_POST['review_text'];

        // Update the review in the database
        $sql = "UPDATE reviews SET rating = :rating, review_text = :review_text WHERE id = :id";
        $stmt = $dbh->prepare($sql);
        $stmt->bindParam(':id', $id, PDO::PARAM_INT);
        $stmt->bindParam(':rating', $rating, PDO::PARAM_INT);
        $stmt->bindParam(':review_text', $review_text, PDO::PARAM_STR);

        if ($stmt->execute()) {
            echo "<p style='color:green;'>Review updated successfully!</p>";
        } else {
            echo "<p style='color:red;'>Failed to update the review. Please check the ID and try again.</p>";
        }
    }
} catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
}
?>

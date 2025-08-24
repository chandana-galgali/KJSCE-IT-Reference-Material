<link rel="stylesheet" href="styless.css">
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

    // Retrieve all reviews
    $sql = "SELECT * FROM reviews";
    $stmt = $dbh->query($sql);
    $reviews = $stmt->fetchAll(PDO::FETCH_ASSOC);

    echo "<div class='reviews-container'>";
    echo "<h2>Perfume Reviews</h2>";
    foreach ($reviews as $review) {
        echo "<div class='review'>";
        echo "<strong>Perfume:</strong> " . htmlspecialchars($review['perfume_name']) . "<br>";
        echo "<strong>Reviewer:</strong> " . htmlspecialchars($review['reviewer_name']) . "<br>";
        echo "<strong>Rating:</strong> " . htmlspecialchars($review['rating']) . "/5<br>";
        echo "<strong>Review:</strong> " . htmlspecialchars($review['review_text']) . "<br>";
        echo "<small><em>Posted on: " . $review['created_at'] . "</em></small>";
        echo "</div>";
    }
    echo "</div>";

} catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
}
?>
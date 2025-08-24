<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Update Review</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="update-container">
        <h2>Update Review</h2>
        <form action="update_review.php" method="POST">
            <label for="id">Review ID:</label>
            <input type="number" id="id" name="id" required><br><br>

            <label for="rating">New Rating (1 to 5):</label>
            <input type="number" id="rating" name="rating" min="1" max="5" required><br><br>

            <label for="review_text">New Review Text:</label>
            <textarea id="review_text" name="review_text" required></textarea><br><br>

            <input type="submit" value="Update Review">
        </form>
    </div>
</body>
</html>
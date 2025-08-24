<?php
// Set the target URL for the book website
$targetUrl = "http://books.toscrape.com/";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $targetUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Execute cURL to fetch HTML content
$htmlContent = curl_exec($ch);
if(curl_errno($ch)) {
    echo 'cURL error: ' . curl_error($ch);
    curl_close($ch);
    exit;
}
curl_close($ch);

// Load HTML content into DOMDocument
$dom = new DOMDocument();
libxml_use_internal_errors(true); // Suppress warnings for invalid HTML
$dom->loadHTML($htmlContent);
libxml_clear_errors();

// Use XPath to locate book information
$xpath = new DOMXPath($dom);
$books = $xpath->query("//article[@class='product_pod']");

// Open a CSV file to save the scraped data
$file = fopen("books_data.csv", "w");
fputcsv($file, ['Title', 'Price', 'Availability']); // Header row

// Iterate through each book container and extract details
foreach ($books as $book) {
    // Extract book title
    $titleNode = $xpath->query(".//h3/a", $book)->item(0);
    $title = $titleNode ? $titleNode->getAttribute("title") : "N/A";

    // Extract book price
    $priceNode = $xpath->query(".//p[@class='price_color']", $book)->item(0);
    $price = $priceNode ? $priceNode->textContent : "N/A";

    // Extract availability status
    $availabilityNode = $xpath->query(".//p[contains(@class, 'instock')]", $book)->item(0);
    $availability = $availabilityNode ? trim($availabilityNode->textContent) : "N/A";

    // Write data to CSV file
    fputcsv($file, [$title, $price, $availability]);
}

// Close the CSV file
fclose($file);

echo "Data scraping completed. Check 'books_data.csv' for results.";
?>

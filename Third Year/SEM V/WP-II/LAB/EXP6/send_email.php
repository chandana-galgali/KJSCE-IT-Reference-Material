<?php
require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/SMTP.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

$mail = new PHPMailer(true);

try {
    // Server settings
    $mail->SMTPDebug = 2;
    $mail->isSMTP();
    $mail->Host       = 'smtp.gmail.com';
    $mail->SMTPAuth   = true;
    $mail->Username   = 'chandana.g@somaiya.edu';  // Your email
    $mail->Password   = 'yrmugjiyzylovvsf';         // Your email password
    $mail->SMTPSecure = 'tls';
    $mail->Port       = 587;

    // Recipients
    $mail->setFrom('chandana.g@somaiya.edu', 'Perfume Paradise');  
    $mail->addAddress('prachi.gandhi@somaiya.edu', 'Prachi Gandhi');
    $mail->addAddress('mahek.jt@somaiya.edu', 'Mahek Thakkar'); 
    $mail->addCC('samrudhi.b@somaiya.edu'); 
    $mail->addCC('t.mangaonkar@somaiya.edu');
    $mail->addBCC('anand.pt@somaiya.edu');

    // Email Content
    $mail->isHTML(true);
    $mail->Subject = 'Exclusive Offer Just for You at Perfume Paradise!';
    
    // HTML Body with a perfume promotional theme
    $mail->Body = '
        <html>
    <body style="font-family: Arial, sans-serif; background-color: #ffffff; color: #333333; margin: 0; padding: 20px;">
        <div style="max-width: 600px; margin: auto; background-color: #0b1d3b; padding: 20px; border: 1px solid #b39555; border-radius: 8px;">
            <h2 style="color: #b39555; text-align: center; border-bottom: 2px solid #b39555; padding-bottom: 10px;">
                Welcome to <span style="color: #ffffff;">Perfume Paradise</span>, <br>Your Fragrance Destination!
            </h2>
            <p style="font-size: 1.1em; color: #ffffff;">Dear <strong>Customer</strong>,</p>
            <p style="font-size: 1em; color: #ffffff;">
                We are thrilled to have you as part of the Perfume Paradise family! To show our appreciation, we are offering an
                exclusive <strong style="color: #b39555;">15% discount</strong> on your next purchase. Indulge in the luxury of our latest arrivals
                and signature scents.
            </p>
            <h3 style="color: #0b1d3b; text-align: center; margin-top: 20px; padding: 10px; background-color: #b39555; border-radius: 8px;">
                Exclusive Offer Code: <span style="color: #0b1d3b;">CHANDANA20</span>
            </h3>
            <p style="font-size: 1em; color: #ffffff; text-align: center;">
                Use this code at checkout to redeem your discount. Dont wait too long - this offer is valid only for the next 7 days!
            </p>
            <hr style="border: none; border-top: 2px solid #b39555; margin: 20px 0;">
            <h3 style="color: #b39555;">Our Recommendations for You:</h3>
            <ul style="color: #ffffff; font-size: 1em; line-height: 1.5em;">
                <li><strong style="color: #b39555;">Midnight Blossom</strong> - A delicate blend of floral and woody notes, perfect for evening wear.</li>
                <li><strong style="color: #b39555;">Summer Breeze</strong> - Fresh and vibrant, capturing the essence of a sunny day by the beach.</li>
                <li><strong style="color: #b39555;">Vanilla Dreams</strong> - A warm, comforting scent with hints of vanilla and sandalwood.</li>
            </ul>
            <p style="font-size: 1em; color: #ffffff;">
                Visit our website to explore more <a href="https://keva.co.in/" style="color: #b39555; text-decoration: none;">here</a>.
            </p>
            <hr style="border: none; border-top: 2px solid #b39555; margin: 20px 0;">
            <p style="color: #ffffff;">Thank you for choosing Perfume Paradise. We look forward to bringing you more enchanting scents!</p>
            <p style="color: #ffffff;">
                Sincerely,<br><span style="font-weight: bold; color: #b39555;">Perfume Paradise Team</span>
            </p>
        </div>
    </body>
</html>
    ';
    
    // Plain text alternative body
    $mail->AltBody = 'Thank you for being a valued customer at Perfume Paradise! Enjoy 15% off your next purchase with the code CHANDANA20. Visit us at https://keva.co.in/ to explore our exclusive fragrances.';

    // Send the email
    $mail->send();
    echo 'Promotional email has been sent successfully';
} catch (Exception $e) {
    echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
}
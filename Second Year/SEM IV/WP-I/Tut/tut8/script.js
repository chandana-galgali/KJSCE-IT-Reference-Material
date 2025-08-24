const now = new Date();
document.getElementById('dateDisplay').innerHTML = `${now.toDateString()}. Discover today's trending perfumes!`;
let perfumes = ['Rose & Oud', 'Jasmine Twilight', 'Citrus Breeze', 'Amber Elegance', 'Vanilla Dreams'];
let perfumesListHTML = '<ul>';
perfumes.forEach(perfume => {
    perfumesListHTML += `<li>${perfume}</li>`;
});
perfumesListHTML += '</ul>';
document.getElementById('arrayDisplay').innerHTML = `Our Featured Selections: ${perfumesListHTML}`;
function revealOffer() {
    document.getElementById('specialOffer').innerHTML = "Today's Special Offer!";
    document.getElementById('description').innerHTML = "Enjoy a 20% discount on all first-time purchases. Discover your signature scent with Scent Haven.";
    document.getElementById('description').style.color = "#007BFF"; 
    document.getElementById('description').style.fontWeight = "bold";
}
let slideIndex = 1;
    showSlides(slideIndex);
    function plusSlides(n) {
        showSlides(slideIndex += n);
    }
    function showSlides(n) {
        let i;
        let slides = document.getElementsByClassName("mySlides");
        if (n > slides.length) {slideIndex = 1}    
        if (n < 1) {slideIndex = slides.length}
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";  
        }
        slides[slideIndex-1].style.display = "block";  
    }
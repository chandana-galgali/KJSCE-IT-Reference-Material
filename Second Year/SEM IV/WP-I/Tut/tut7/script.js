// JS FILE

document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();
   
    var name = document.getElementById('name').value;
    var rollNumber = document.getElementById('rollNumber').value;
    var email = document.getElementById('email').value;
    var telephone = document.getElementById('telephone').value;
    var address = document.getElementById('address').value;
    var gender = document.getElementById('gender').value;
    var dob = document.getElementById('dob').value;
    var course = document.getElementById('course').value;

    if (name === "") {
        alert('Please enter your name.');
        return;
    }
   
    if (!isNaN(name)) {
        alert('Name must be a string of alphabets only.');
        return;
    }

    if (name.length > 50) {
        alert('Name must not exceed 50 characters.');
        return;
    }

    if (rollNumber === "") {
        alert('Please enter your roll number.');
        return;
    }
   
    if (isNaN(rollNumber)) {
        alert('Roll number must be a number.');
        return;
    }

    if (!(/^\d{11}$/.test(rollNumber))) {
        alert('Roll number must contain only 11 digits.');
        return;
    }
   
    if (email === "") {
        alert('Please enter your Email ID.');
        return;
    }
   
    if (!email.match(/\S+@\S+\.\S+/)) {
        alert('Email ID must be in the correct format.');
        return;
    }

    if (email.length > 100) {
        alert('Email ID must not exceed 100 characters.');
        return;
    }

    if (telephone === "") {
        alert('Please enter your telephone number.');
        return;
    }

    if (isNaN(telephone)) {
        alert('Telephone number must only contain digits.');
        return;
    }
   
    if (!(/^\d{10}$/.test(telephone))) {
        alert('Telephone number must be a 10 digit number.');
        return;
    }

    if (address.trim() === "") {
        alert('Please enter your address.');
        return;
    }

    if (address.length > 200) {
        alert('Address must not exceed 200 characters.');
        return;
    }

    var pinCodeRegex = /\b\d{6}\b/;
    if (!pinCodeRegex.test(address)) {
        alert('Address must end with a 6-digit PIN code.');
        return;
    }
   
    if (gender === "") {
        alert('Please select your gender.');
        return;
    }

    if (!["male", "female", "other"].includes(gender)) {
        alert('Please select a valid gender option.');
        return;
    }

    if (document.getElementById('gender').selectedIndex === 0) {
        alert('Please select your gender from the dropdown.');
        return;
    }

    if (dob === "") {
        alert('Please select your date of birth.');
        return;
    }

    var currentDate = new Date();
    var selectedDate = new Date(dob);
    var minDate = new Date();
    minDate.setFullYear(currentDate.getFullYear() - 18);

    if (selectedDate >= minDate) {
        alert('You must be at least 18 years old to register.');
        return;
    }

    if (selectedDate > currentDate) {
        alert('Date of Birth cannot be in the future.');
        return;
    }

    if (course === "") {
        alert('Please select your course.');
        return;
    }

    if (document.getElementById('course').selectedIndex === 0) {
        alert('Please select your course from the dropdown.');
        return;
    }

    var validCourses = ["Computer Science", "Information Technology", "Electronics and Computer Science", "Electronics and Telecommunications", "Mechanical"];


    if (!validCourses.includes(course)) {
        alert('Please select a valid course.');
        return;
    }
   
    alert('Form submitted successfully!');

    var summaryHtml = `
        <div class="container submission-summary">
            <h1>Here's what we received:</h1>
            <ul>
                <li><strong>Name:</strong> ${name}</li>
                <li><strong>Roll Number:</strong> ${rollNumber}</li>
                <li><strong>Email ID:</strong> ${email}</li>
                <li><strong>Telephone Number:</strong> ${telephone}</li>
                <li><strong>Address:</strong> ${address}</li>
                <li><strong>Gender:</strong> ${gender}</li>
                <li><strong>Date of Birth:</strong> ${dob}</li>
                <li><strong>Course:</strong> ${course}</li>
            </ul>
        </div>`;

    // Set the body's innerHTML to the summaryHtml
    document.body.innerHTML = summaryHtml;
});
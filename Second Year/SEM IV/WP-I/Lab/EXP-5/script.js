// JS FILE
document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
    
    var name = document.getElementById('name').value;
    var rollNumber = document.getElementById('rollNumber').value;
    var email = document.getElementById('email').value;
    var telephone = document.getElementById('telephone').value;
    
    if (!isNaN(name)) {
        alert('Name must be a string of alphabets only.');
        return;
    }
    
    if (isNaN(rollNumber)) {
        alert('Roll number must be a number.');
        return;
    }
    
    if (email.indexOf('@') < 0 || email.indexOf('.') < 0) {
        alert('Email ID must contain an "@" and "."');
        return;
    }
    
    if (!(/^\d{10}$/.test(telephone))) {
        alert('Telephone number must be a 10 digit number.');
        return;
    }
    
    alert('Form submitted successfully!');
});

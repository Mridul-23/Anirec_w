document.addEventListener('DOMContentLoaded', function() {
    // Set placeholder for password1
    var password1Field = document.getElementById('id_password1');
    if (password1Field) {
        password1Field.setAttribute('placeholder', 'Password');
    }

    // Set placeholder for password2
    var password2Field = document.getElementById('id_password2');
    if (password2Field) {
        password2Field.setAttribute('placeholder', 'Confirm Password');
    }
});


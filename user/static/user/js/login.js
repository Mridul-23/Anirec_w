document.querySelector('.toggle-password').addEventListener('click', function (e) {
    const passwordField = document.querySelector('#id_password');
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        e.target.textContent = 'Hide';
    } else {
        passwordField.type = 'password';
        e.target.textContent = 'Show';
    }
});

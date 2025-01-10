function createAutocomplete(selector) {
    new Autocomplete(selector, {
        search: (input) => {
            const url = `/anirec/search/?name=${input}`;
            return new Promise((resolve) => {
                fetch(url)
                    .then((response) => response.json())
                    .then((data) => {
                        resolve(data.data);
                    });
            });
        },
    });
}

createAutocomplete("#autocomplete1");
createAutocomplete("#autocomplete2");
createAutocomplete("#autocomplete3");

// Form submission handler
document.getElementById("shows-form").addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = {
        show1: formData.get("show1"),
        show2: formData.get("show2"),
        show3: formData.get("show3"),
        show1_rating: formData.get("show1_rating"),
        show2_rating: formData.get("show2_rating"),
        show3_rating: formData.get("show3_rating")
    };

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch('/anirec/recommendations/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
        if (result.status === 'success') {
            window.location.href = '/anirec/recommendations/';
        } else {
            console.error('MError:', result.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

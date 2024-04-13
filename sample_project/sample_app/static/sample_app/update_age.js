function fetchUpdatedAge() {
    fetch('http://127.0.0.1:8000/sample_app/api/get-updated-age/')
        .then(response => response.json())
        .then(data => {
            // Update the UI to display the updated age
            document.getElementById('updated-age').innerText = 'Updated Age: ' + data.updated_age;
        })
        .catch(error => console.error('Error:', error));
}

// Call fetchUpdatedAge every minute
setInterval(fetchUpdatedAge, 60000); /
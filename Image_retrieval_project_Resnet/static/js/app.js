// app.js

// Array to store the history of searches
let searchHistory = [];

// Function to handle adding new history item
function addToHistory(queryImage) {
    // Add the new query image to the history array
    searchHistory.push(queryImage);
    
    // Call the function to update the display
    displayHistory();
}

// Function to display the search history in the UI
function displayHistory() {
    // Get the history list element
    const historyList = document.getElementById('historyList');
    
    // Clear out the previous history items
    historyList.innerHTML = '';
    
    // Loop through the searchHistory array and display each item
    searchHistory.forEach((item, index) => {
        const li = document.createElement('li');
        li.textContent = `Search ${index + 1}: ${item}`;
        historyList.appendChild(li);
    });
}

// Simulated image search process
function retrieveSimilarImages() {
    const queryImage = document.getElementById('imageUpload').value;
    
    if (queryImage) {
        // Simulate image retrieval (you can replace this with your actual image retrieval logic)
        document.getElementById('similarImages').innerHTML = '<img src="path-to-similar-image.jpg" alt="Similar Image">';
        
        // Add the query image to the search history
        addToHistory(queryImage);
    }
}

// Add event listener to the retrieve button
document.getElementById('retrieveButton').addEventListener('click', retrieveSimilarImages);

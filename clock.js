// Function to update the clock
function updateClock() {
    const now = new Date();
    
    // Format time as HH:MM:SS
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    
    const timeString = `${hours}:${minutes}:${seconds}`;
    
    // Update the clock element
    document.getElementById('clock').textContent = timeString;
    
    // Format date
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    const dateString = now.toLocaleDateString('en-US', options);
    
    // Update the date element
    document.getElementById('date').textContent = dateString;
}

// Update the clock immediately when page loads
updateClock();

// Update the clock every second
setInterval(updateClock, 1000);

// Optional: Add functionality to toggle between 12-hour and 24-hour formats
let is24HourFormat = true;

document.addEventListener('keydown', function(event) {
    // Press 't' to toggle time format
    if (event.key === 't' || event.key === 'T') {
        is24HourFormat = !is24HourFormat;
        updateClock(); // Update immediately to reflect the change
    }
});

// Function to format time based on selected format (would be used if we implement toggle)
function formatTime(date, is24Hour) {
    let hours = date.getHours();
    const minutes = String(date.getMinutes()).padStart(2, '0');
    const seconds = String(date.getSeconds()).padStart(2, '0');
    
    if (!is24Hour) {
        const ampm = hours >= 12 ? 'PM' : 'AM';
        hours = hours % 12;
        hours = hours ? hours : 12; // the hour '0' should be '12'
        return `${hours}:${minutes}:${seconds} ${ampm}`;
    } else {
        return `${String(hours).padStart(2, '0')}:${minutes}:${seconds}`;
    }
}
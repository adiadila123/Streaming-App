 // dark-mode-toggle.js
const darkModeToggle = document.getElementById('darkModeToggle');
    const modeLabel = document.getElementById('modeLabel');
    const bodyElement = document.body;

    const updateModeLabel = () => {
        modeLabel.textContent = darkModeToggle.checked ? 'Light Mode':'Dark Mode' ;
    };

    darkModeToggle.addEventListener('change', function() {
        bodyElement.classList.toggle('dark-mode', this.checked);
        updateModeLabel();

        // Save the user's preference in localStorage
        localStorage.setItem('darkMode', this.checked ? 'enabled' : 'disabled');
    });

    // Check the saved preference and set the initial mode
    if (localStorage.getItem('darkMode') === 'enabled') {
        bodyElement.classList.add('dark-mode');
        darkModeToggle.checked = true;
    }
    updateModeLabel();  // Update label on initial load

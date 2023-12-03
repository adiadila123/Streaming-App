document.addEventListener('DOMContentLoaded', function () {
    var trailerModal = document.getElementById('thrillerModal');

    trailerModal.addEventListener('hide.bs.modal', function () {
        // Find the iframe inside the modal
        var iframe = this.querySelector('iframe');
        if (iframe) {
            // Reset the src attribute to stop the video
            var iframeSrc = iframe.src;
            iframe.src = '';
            iframe.src = iframeSrc;  // Optionally reset the src to its original value if needed later
        }
    });
});


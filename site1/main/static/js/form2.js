    document.addEventListener('DOMContentLoaded', function() {
      var form = document.getElementById('contact-form');
      if (form) {
        var messages = document.querySelector('.messages-container');
        if (messages) {
          form.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
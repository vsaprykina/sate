document.addEventListener('DOMContentLoaded', function() {
  var serviceInfos = document.querySelectorAll('.service-info p:not(:last-child)');

  serviceInfos.forEach(function(info) {
    info.addEventListener('click', function() {
      this.style.display = 'block';
    });
  });
});
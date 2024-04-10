
    document.addEventListener('DOMContentLoaded', function() {
        var reasonDivs = document.querySelectorAll('.reason');
        reasonDivs.forEach(function(div, index) {
            setTimeout(function() {
                div.classList.add('visible');
            }, index * 300);
        });
    });

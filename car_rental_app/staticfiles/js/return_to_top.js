window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("return-to-top").style.display = "block";
    } else {
        document.getElementById("return-to-top").style.display = "none";
    }
}

function topFunction() {
    // Scroll to the top of the page with smooth animation
    scrollToTop(1000); // Adjust the duration as needed (in milliseconds)
}

function scrollToTop(duration) {
    const startingY = window.pageYOffset;
    const startTime = performance.now();

    function scrollStep(time) {
        let elapsed = time - startTime;
        let progress = Math.min(elapsed / duration, 1);
        window.scrollTo(0, startingY * (1 - easeInOutCubic(progress)));

        if (elapsed < duration) {
            requestAnimationFrame(scrollStep);
        }
    }

    function easeInOutCubic(t) {
        return t < 0.5 ? 4 * t * t * t : (t - 1) * (2 * t - 2) * (2 * t - 2) + 1;
    }

    requestAnimationFrame(scrollStep);
}


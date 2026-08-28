document.addEventListener('DOMContentLoaded', function () {
    const body = document.body;
    if (body && body.classList.contains('interactive-bg')) {
        body.addEventListener('mousemove', function (event) {
            const x = (event.clientX / window.innerWidth) * 100;
            const y = (event.clientY / window.innerHeight) * 100;
            body.style.background = `radial-gradient(circle at ${x}% ${y}%, rgba(255,255,255,0.15), rgba(0,0,0,0.08) 30%, transparent 60%), linear-gradient(-45deg, #1e3c72, #2a5298, #6dd5ed, #2193b0)`;
            body.style.backgroundSize = 'cover';
        });
    }
});

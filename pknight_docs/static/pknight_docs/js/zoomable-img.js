const zoomableImages = document.querySelectorAll('.zoomable-image');
zoomableImages.forEach((image) => {
    image.addEventListener('click', () => {
        const fullscreenImage = document.createElement('img');
        fullscreenImage.src = image.src;
        fullscreenImage.alt = image.alt;
        fullscreenImage.classList.add('fixed', 'top-0', 'left-0', 'w-full', 'h-full', 'z-50', 'object-contain', 'cursor-zoom-out');
        document.body.appendChild(fullscreenImage);
        document.body.classList.add('overflow-hidden');
        fullscreenImage.addEventListener('click', () => {
            fullscreenImage.remove();
            document.body.classList.remove('overflow-hidden');
        });
    });
});

const zoomableImages = document.querySelectorAll('.zoomable-image');
zoomableImages.forEach((image) => {
    image.addEventListener('click', () => {
        const fullscreenImage = document.createElement('img');
        fullscreenImage.src = image.src;
        fullscreenImage.alt = image.alt;
        // 添加类，object-contain 保持图片比例，cursor-zoom-out 鼠标移入时显示放大图标，backdrop-blur-lg 背景模糊
        fullscreenImage.classList.add('fixed', 'top-0', 'left-0', 'w-full', 'h-full', 'z-50', 'object-contain', 'cursor-zoom-out', 'backdrop-blur-lg');
        document.body.appendChild(fullscreenImage);
        document.body.classList.add('overflow-hidden');
        fullscreenImage.addEventListener('click', () => {
            fullscreenImage.remove();
            document.body.classList.remove('overflow-hidden');
        });
    });
});

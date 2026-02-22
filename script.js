document.addEventListener('DOMContentLoaded', () => {
    const profileImg = document.getElementById('profileImg');
    const imagePlaceholder = document.querySelector('.image-placeholder');
    const profileImageContainer = document.querySelector('.profile-image');
    const toggleBtn = document.getElementById('togglePhotoBtn');

    let photoHidden = false;

    if (profileImg) {
        profileImg.addEventListener('error', () => {
            profileImg.style.display = 'none';
            if (imagePlaceholder) {
                imagePlaceholder.style.display = 'flex';
            }
        });

        profileImg.addEventListener('load', () => {
            profileImg.style.display = 'block';
            if (imagePlaceholder) {
                imagePlaceholder.style.display = 'none';
            }
        });
    }

    if (toggleBtn && profileImageContainer) {
        toggleBtn.addEventListener('click', () => {
            photoHidden = !photoHidden;
            profileImageContainer.style.display = photoHidden ? 'none' : 'block';
            toggleBtn.textContent = photoHidden ? '🖼️ Show Photo' : '🖼️ Hide Photo';
        });
    }
});

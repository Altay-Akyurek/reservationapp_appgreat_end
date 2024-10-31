document.addEventListener('DOMContentLoaded', function () {
    const menuItems = document.querySelectorAll('.tm-list a');
    const menuToggle = document.getElementById('menu-toggle');
    const menu = document.querySelector('.menu');

    // Menü öğeleri hover efekti
    menuItems.forEach(item => {
        item.addEventListener('mouseover', function () {
            this.classList.add('hovered');
        });
        
        item.addEventListener('mouseout', function () {
            this.classList.remove('hovered');
        });

        item.addEventListener('click', function() {
            // Menü öğesine tıklanınca küçük bir animasyon
            this.style.transform = 'scale(1.2)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 300);
        });
    });

    // Menü toggle animasyonu
    menuToggle.addEventListener('change', function () {
        if (this.checked) {
            menu.style.transform = 'translateX(0)';
            menu.style.opacity = '1';
        } else {
            menu.style.transform = 'translateX(100%)';
            menu.style.opacity = '0';
        }
    });

    // Sayfa kaydırıldığında menü stilini değiştirme
    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            document.querySelector('.tm-header').classList.add('scrolled');
        } else {
            document.querySelector('.tm-header').classList.remove('scrolled');
        }
    });
});

function scrollToSection(sectionId) {
        const section = document.getElementById(sectionId);
        if (section) {
            window.scrollTo({
                top: section.offsetTop,
                behavior: 'smooth'
            });
        }
    }

    document.querySelector('.navbar ul:nth-child(2)').addEventListener('click', function() {
        scrollToSection('services');
    });

    document.querySelector('.navbar ul:nth-child(4)').addEventListener('click', function() {
        scrollToSection('contact');
    });

    document.querySelector('.second_info ul:nth-child(2)').addEventListener('click', function() {
        scrollToSection('contact');
    });

    document.querySelector('.second_info ul:nth-child(3)').addEventListener('click', function() {
        scrollToSection('services');
    });

    document.querySelector('.second_info ul:nth-child(4)').addEventListener('click', function() {
        scrollToSection('home');
    });

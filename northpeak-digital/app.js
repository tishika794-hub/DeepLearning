document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialize Lucide Icons
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    // 2. Scroll Header State
    const header = document.getElementById('header');
    const checkScroll = () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    };
    window.addEventListener('scroll', checkScroll);
    checkScroll(); // Run once in case user loads page scrolled down

    // 3. Mobile Navigation Menu Toggle
    const menuToggle = document.getElementById('menu-toggle');
    const mobileDrawer = document.getElementById('mobile-drawer');
    const mobileLinks = document.querySelectorAll('.mobile-link');

    const toggleMenu = () => {
        menuToggle.classList.toggle('active');
        mobileDrawer.classList.toggle('open');
        document.body.classList.toggle('no-scroll');
    };

    menuToggle.addEventListener('click', toggleMenu);

    mobileLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (mobileDrawer.classList.contains('open')) {
                toggleMenu();
            }
        });
    });

    // 4. Mouse Move Glow Effect for Service Cards
    const serviceCards = document.querySelectorAll('.service-card');
    serviceCards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            card.style.setProperty('--x', `${x}px`);
            card.style.setProperty('--y', `${y}px`);
        });
    });

    // 5. Reveal Animations & Statistics Counter Observer
    const revealItems = document.querySelectorAll('.reveal-item');
    const statNumbers = document.querySelectorAll('.stat-number');

    // Count Up Animation function
    const countUp = (element) => {
        const target = parseFloat(element.getAttribute('data-target'));
        const prefix = element.getAttribute('data-prefix') || '';
        const suffix = element.getAttribute('data-suffix') || '';
        const decimals = parseInt(element.getAttribute('data-decimals') || '0', 10);
        
        let start = 0;
        const duration = 2000; // ms
        let startTimestamp = null;
        
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            const currentVal = progress * (target - start) + start;
            
            element.innerHTML = prefix + currentVal.toFixed(decimals) + suffix;
            
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    };

    // Observer options
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const sectionObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Reveal regular elements
                if (entry.target.classList.contains('reveal-item')) {
                    entry.target.classList.add('revealed');
                    observer.unobserve(entry.target);
                }
                
                // Trigger stats countup
                if (entry.target.classList.contains('stats-grid')) {
                    statNumbers.forEach(num => countUp(num));
                    observer.unobserve(entry.target);
                }
            }
        });
    }, observerOptions);

    // Watch items
    revealItems.forEach(item => sectionObserver.observe(item));
    const statsGrid = document.querySelector('.stats-grid');
    if (statsGrid) {
        sectionObserver.observe(statsGrid);
    }

    // 6. Pricing monthly/yearly switcher
    const billingToggle = document.getElementById('billing-toggle');
    const billingMonthly = document.getElementById('billing-monthly');
    const billingYearly = document.getElementById('billing-yearly');
    const priceElements = document.querySelectorAll('.pricing-card .price');

    const updatePricing = (isYearly) => {
        priceElements.forEach(priceEl => {
            // Get figures
            const monthlyVal = priceEl.getAttribute('data-monthly');
            const yearlyVal = priceEl.getAttribute('data-yearly');
            
            // Fade out, update, fade in
            priceEl.style.opacity = '0';
            priceEl.style.transform = 'translateY(-10px)';
            
            setTimeout(() => {
                priceEl.textContent = isYearly ? yearlyVal : monthlyVal;
                priceEl.style.opacity = '1';
                priceEl.style.transform = 'translateY(0)';
            }, 200);
        });

        if (isYearly) {
            billingToggle.classList.add('active');
            billingYearly.classList.add('active');
            billingMonthly.classList.remove('active');
        } else {
            billingToggle.classList.remove('active');
            billingYearly.classList.remove('active');
            billingMonthly.classList.add('active');
        }
    };

    billingToggle.addEventListener('click', () => {
        const isYearly = !billingToggle.classList.contains('active');
        updatePricing(isYearly);
    });

    billingMonthly.addEventListener('click', () => updatePricing(false));
    billingYearly.addEventListener('click', () => updatePricing(true));

    // 7. Contact Form Custom Client-Side Validation
    const form = document.getElementById('contact-form');
    const inputs = form.querySelectorAll('input, select, textarea');
    const toastContainer = document.getElementById('toast-container');
    const toastCard = document.getElementById('success-toast');
    const toastClose = document.getElementById('toast-close');
    const submitBtn = document.getElementById('submit-btn');

    // Email Regex
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    // Validate a single field
    const validateField = (field) => {
        const group = field.closest('.form-group');
        let isValid = true;

        if (field.hasAttribute('required') && !field.value.trim()) {
            isValid = false;
        } else if (field.type === 'email' && field.value.trim() && !emailRegex.test(field.value.trim())) {
            isValid = false;
        } else if (field.minLength > 0 && field.value.trim().length < field.minLength) {
            isValid = false;
        }

        if (isValid) {
            group.classList.remove('invalid');
            group.classList.add('valid');
        } else {
            group.classList.remove('valid');
            group.classList.add('invalid');
        }

        return isValid;
    };

    // Setup input listeners for real-time validation feedback
    inputs.forEach(input => {
        input.addEventListener('blur', () => validateField(input));
        input.addEventListener('input', () => {
            if (input.closest('.form-group').classList.contains('invalid')) {
                validateField(input); // Clear errors dynamically once corrected
            }
        });
        
        // Select fields validation on change
        if (input.tagName === 'SELECT') {
            input.addEventListener('change', () => validateField(input));
        }
    });

    // Handle Form Submit
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        let isFormValid = true;
        inputs.forEach(input => {
            const isInputValid = validateField(input);
            if (!isInputValid) {
                isFormValid = false;
            }
        });

        if (isFormValid) {
            // Save original button content
            const originalBtnContent = submitBtn.innerHTML;
            
            // Show loading state
            submitBtn.disabled = true;
            submitBtn.style.cursor = 'not-allowed';
            submitBtn.innerHTML = `
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="spinner-animate" style="margin-right:8px; animation: spin 0.8s linear infinite;"><path d="M21 12a9 9 0 1 1-6.219-8.56"/></svg>
                <span>Sending Request...</span>
            `;

            // Mock submission delay
            setTimeout(() => {
                // Show Success Toast
                toastCard.classList.add('show');
                
                // Clear validation classes and resets
                inputs.forEach(input => {
                    const group = input.closest('.form-group');
                    group.classList.remove('valid');
                    group.classList.remove('invalid');
                });
                form.reset();

                // Restore Button State
                submitBtn.disabled = false;
                submitBtn.style.cursor = 'pointer';
                submitBtn.innerHTML = originalBtnContent;

                // Auto hide toast after 5s
                setTimeout(() => {
                    toastCard.classList.remove('show');
                }, 5000);

            }, 1200);
        }
    });

    // Close Toast
    toastClose.addEventListener('click', () => {
        toastCard.classList.remove('show');
    });
});

// Spin Animation helper style injected dynamically if needed
const style = document.createElement('style');
style.innerHTML = `
@keyframes spin {
    to { transform: rotate(360deg); }
}
body.no-scroll {
    overflow: hidden;
}
`;
document.head.appendChild(style);

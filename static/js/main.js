/**
 * Main JavaScript functionality for Moroccan Accounting Information Website
 */

document.addEventListener('DOMContentLoaded', function() {
  // Initialize Bootstrap tooltips
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });
  
  // Initialize Bootstrap popovers
  const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
  popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl);
  });

  // Theme toggle functionality
  setupThemeToggle();
  
  // Add fade-in animation to elements with the fade-in class
  animateFadeIn();
  
  // Add smooth scrolling to all links
  addSmoothScrolling();
  
  // Add active class to current nav item
  setActiveNavItem();
});

/**
 * Setup theme toggle functionality
 */
function setupThemeToggle() {
  const themeToggle = document.getElementById('theme-toggle');
  const htmlElement = document.documentElement;
  
  if (themeToggle) {
    // Check for saved theme preference or use preference from OS
    const savedTheme = localStorage.getItem('theme');
    const prefersDarkTheme = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    // Set initial theme
    if (savedTheme) {
      htmlElement.setAttribute('data-bs-theme', savedTheme);
      updateThemeIcon(savedTheme);
    } else if (prefersDarkTheme) {
      htmlElement.setAttribute('data-bs-theme', 'dark');
      updateThemeIcon('dark');
    } else {
      htmlElement.setAttribute('data-bs-theme', 'light');
      updateThemeIcon('light');
    }
    
    // Toggle theme on click
    themeToggle.addEventListener('click', function() {
      const currentTheme = htmlElement.getAttribute('data-bs-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      
      htmlElement.setAttribute('data-bs-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      
      updateThemeIcon(newTheme);
    });
  }
}

/**
 * Update theme icon based on current theme
 * @param {string} theme - The current theme ('dark' or 'light')
 */
function updateThemeIcon(theme) {
  const themeIcon = document.getElementById('theme-icon');
  
  if (themeIcon) {
    if (theme === 'dark') {
      themeIcon.classList.remove('bi-sun-fill');
      themeIcon.classList.add('bi-moon-fill');
    } else {
      themeIcon.classList.remove('bi-moon-fill');
      themeIcon.classList.add('bi-sun-fill');
    }
  }
}

/**
 * Animate elements with fade-in class
 */
function animateFadeIn() {
  const fadeElements = document.querySelectorAll('.fade-in');
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1
  });
  
  fadeElements.forEach(element => {
    observer.observe(element);
  });
}

/**
 * Add smooth scrolling to all links
 */
function addSmoothScrolling() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        targetElement.scrollIntoView({
          behavior: 'smooth'
        });
      }
    });
  });
}

/**
 * Set active class on current nav item
 */
function setActiveNavItem() {
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || 
        (currentPath === '/' && href === '/') || 
        (href !== '/' && currentPath.startsWith(href))) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
}

/**
 * Toggle visibility of content
 * @param {string} elementId - The ID of the element to toggle
 */
function toggleContent(elementId) {
  const element = document.getElementById(elementId);
  if (element) {
    if (element.style.display === 'none' || element.style.display === '') {
      element.style.display = 'block';
    } else {
      element.style.display = 'none';
    }
  }
}

/**
 * Create a notification
 * @param {string} message - The message to display
 * @param {string} type - The type of notification (success, danger, warning, info)
 */
function showNotification(message, type = 'info') {
  const notificationContainer = document.getElementById('notification-container');
  
  if (!notificationContainer) {
    // Create container if it doesn't exist
    const container = document.createElement('div');
    container.id = 'notification-container';
    container.style.position = 'fixed';
    container.style.top = '20px';
    container.style.right = '20px';
    container.style.zIndex = '1050';
    document.body.appendChild(container);
  }
  
  // Create notification element
  const notification = document.createElement('div');
  notification.className = `toast align-items-center text-white bg-${type} border-0`;
  notification.role = 'alert';
  notification.setAttribute('aria-live', 'assertive');
  notification.setAttribute('aria-atomic', 'true');
  
  notification.innerHTML = `
    <div class="d-flex">
      <div class="toast-body">
        ${message}
      </div>
      <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
    </div>
  `;
  
  document.getElementById('notification-container').appendChild(notification);
  
  // Initialize and show toast
  const toast = new bootstrap.Toast(notification, {
    autohide: true,
    delay: 5000
  });
  toast.show();
  
  // Remove from DOM after hiding
  notification.addEventListener('hidden.bs.toast', function() {
    notification.remove();
  });
}

/**
 * JavaScript functions for the Chart of Accounts page
 */

document.addEventListener('DOMContentLoaded', function() {
  // Initialize collapsible account classes
  initAccountClassCollapse();
  
  // Initialize search functionality
  initAccountSearch();
  
  // Initialize copy code functionality
  initCopyAccountCode();
});

/**
 * Initialize collapsible behavior for account classes
 */
function initAccountClassCollapse() {
  // Get all account class headers
  const classHeaders = document.querySelectorAll('.account-class-header');
  
  classHeaders.forEach(header => {
    // Add click event to the header element
    header.addEventListener('click', function(e) {
      // Prevent default action if clicked on button
      if (e.target.tagName === 'BUTTON' || e.target.tagName === 'I') {
        e.preventDefault();
      }
      
      // Find the content container that follows this header
      const content = this.nextElementSibling;
      
      // Toggle the visibility
      if (content.style.maxHeight) {
        content.style.maxHeight = null;
        // Change the icon
        this.querySelector('.toggle-icon').classList.remove('bi-chevron-up');
        this.querySelector('.toggle-icon').classList.add('bi-chevron-down');
      } else {
        content.style.maxHeight = content.scrollHeight + "px";
        // Change the icon
        this.querySelector('.toggle-icon').classList.remove('bi-chevron-down');
        this.querySelector('.toggle-icon').classList.add('bi-chevron-up');
      }
    });
    
    // Also add click event to the button itself
    const button = header.querySelector('button');
    if (button) {
      button.addEventListener('click', function(e) {
        // Prevent propagation to avoid double triggering
        e.stopPropagation();
        
        // Trigger click on parent header
        header.click();
      });
    }
  });
  
  // Open the first class by default
  if (classHeaders.length > 0) {
    classHeaders[0].click();
  }
}

/**
 * Initialize search functionality for accounts
 */
function initAccountSearch() {
  const searchInput = document.getElementById('account-search');
  
  if (searchInput) {
    searchInput.addEventListener('input', function() {
      const searchTerm = this.value.toLowerCase();
      
      // Get all account items
      const accountItems = document.querySelectorAll('.account-item, .sub-account');
      const accountClasses = document.querySelectorAll('.account-class');
      
      // Hide/show account items based on search term
      accountItems.forEach(item => {
        const text = item.textContent.toLowerCase();
        const isVisible = text.includes(searchTerm);
        
        item.style.display = isVisible ? '' : 'none';
      });
      
      // Show account classes that have visible items
      accountClasses.forEach(accountClass => {
        const visibleItems = accountClass.querySelectorAll('.account-item:not([style*="display: none"]), .sub-account:not([style*="display: none"])');
        accountClass.style.display = visibleItems.length > 0 ? '' : 'none';
        
        // If there are visible items, make sure the content is expanded
        if (visibleItems.length > 0) {
          const content = accountClass.querySelector('.account-class-content');
          const header = accountClass.querySelector('.account-class-header');
          
          if (content && !content.style.maxHeight && searchTerm) {
            content.style.maxHeight = content.scrollHeight + "px";
            if (header.querySelector('.toggle-icon')) {
              header.querySelector('.toggle-icon').classList.remove('bi-chevron-down');
              header.querySelector('.toggle-icon').classList.add('bi-chevron-up');
            }
          }
        }
      });
      
      // Show a message if no results found
      const noResultsMessage = document.getElementById('no-results-message');
      if (noResultsMessage) {
        const hasVisibleItems = document.querySelectorAll('.account-item:not([style*="display: none"]), .sub-account:not([style*="display: none"])').length > 0;
        noResultsMessage.style.display = hasVisibleItems ? 'none' : 'block';
      }
    });
  }
}

/**
 * Initialize copy account code functionality
 */
function initCopyAccountCode() {
  const copyButtons = document.querySelectorAll('.copy-code-btn');
  
  copyButtons.forEach(button => {
    button.addEventListener('click', function() {
      // Get the account code to copy
      const code = this.getAttribute('data-code');
      
      // Copy to clipboard
      navigator.clipboard.writeText(code).then(() => {
        // Show success state
        this.innerHTML = '<i class="bi bi-check"></i>';
        this.classList.remove('btn-outline-secondary');
        this.classList.add('btn-success');
        
        // Reset after 2 seconds
        setTimeout(() => {
          this.innerHTML = '<i class="bi bi-clipboard"></i>';
          this.classList.remove('btn-success');
          this.classList.add('btn-outline-secondary');
        }, 2000);
      }).catch(err => {
        console.error('Could not copy text: ', err);
        
        // Show error state
        this.innerHTML = '<i class="bi bi-exclamation-triangle"></i>';
        this.classList.remove('btn-outline-secondary');
        this.classList.add('btn-danger');
        
        // Reset after 2 seconds
        setTimeout(() => {
          this.innerHTML = '<i class="bi bi-clipboard"></i>';
          this.classList.remove('btn-danger');
          this.classList.add('btn-outline-secondary');
        }, 2000);
      });
    });
  });
}

/**
 * Filter accounts by class
 * @param {string} classNumber - The class number to filter by
 */
function filterAccountsByClass(classNumber) {
  // Get all account classes
  const accountClasses = document.querySelectorAll('.account-class');
  
  if (classNumber === 'all') {
    // Show all classes
    accountClasses.forEach(accountClass => {
      accountClass.style.display = '';
    });
  } else {
    // Hide all classes
    accountClasses.forEach(accountClass => {
      const classId = accountClass.id;
      accountClass.style.display = classId === `class-${classNumber}` ? '' : 'none';
    });
  }
}

/**
 * Show account details in a modal
 * @param {string} accountCode - The account code
 * @param {string} accountName - The account name
 * @param {string} accountDescription - The account description
 */
function showAccountDetails(accountCode, accountName, accountDescription) {
  // Get modal elements
  const accountDetailModal = new bootstrap.Modal(document.getElementById('accountDetailModal'));
  const modalTitle = document.getElementById('accountDetailModalTitle');
  const modalCode = document.getElementById('accountDetailCode');
  const modalDescription = document.getElementById('accountDetailDescription');
  
  // Set modal content
  if (modalTitle && modalCode && modalDescription) {
    modalTitle.textContent = accountName;
    modalCode.textContent = accountCode;
    modalDescription.textContent = accountDescription;
    
    // Show the modal
    accountDetailModal.show();
  }
}

/**
 * JavaScript functions for the Chart of Accounts page
 */

document.addEventListener('DOMContentLoaded', function() {
    initAccountClassCollapse();
    initAccountSearch();
    initCopyAccountCode();
});

function initAccountClassCollapse() {
    const classHeaders = document.querySelectorAll('.account-class-header');

    classHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const content = this.nextElementSibling;
            const icon = this.querySelector('.toggle-icon');

            if (content.style.maxHeight && content.style.maxHeight !== '0px') {
                content.style.maxHeight = '0px';
                icon.classList.remove('bi-chevron-up');
                icon.classList.add('bi-chevron-down');
            } else {
                content.style.maxHeight = content.scrollHeight + 'px';
                icon.classList.remove('bi-chevron-down');
                icon.classList.add('bi-chevron-up');
            }
        });
    });

    // Open first class by default
    if (classHeaders.length > 0) {
        classHeaders[0].click();
    }
}

function initAccountSearch() {
    const searchInput = document.getElementById('account-search');
    if (!searchInput) return;

    searchInput.addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase();
        const accountItems = document.querySelectorAll('.account-item, .sub-account');
        const accountClasses = document.querySelectorAll('.account-class');
        let hasResults = false;

        accountItems.forEach(item => {
            const text = item.textContent.toLowerCase();
            const isVisible = text.includes(searchTerm);
            item.style.display = isVisible ? '' : 'none';
            if (isVisible) hasResults = true;
        });

        accountClasses.forEach(accountClass => {
            const hasVisibleItems = Array.from(accountClass.querySelectorAll('.account-item, .sub-account'))
                .some(item => item.style.display !== 'none');
            accountClass.style.display = hasVisibleItems ? '' : 'none';

            if (hasVisibleItems && searchTerm) {
                const content = accountClass.querySelector('.account-class-content');
                const header = accountClass.querySelector('.account-class-header');
                if (content && header) {
                    content.style.maxHeight = content.scrollHeight + 'px';
                    const icon = header.querySelector('.toggle-icon');
                    if (icon) {
                        icon.classList.remove('bi-chevron-down');
                        icon.classList.add('bi-chevron-up');
                    }
                }
            }
        });

        const noResultsMessage = document.getElementById('no-results-message');
        if (noResultsMessage) {
            noResultsMessage.style.display = hasResults ? 'none' : 'block';
        }
    });
}

function initCopyAccountCode() {
    const copyButtons = document.querySelectorAll('.copy-code-btn');

    copyButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.stopPropagation();
            const code = this.getAttribute('data-code');

            navigator.clipboard.writeText(code).then(() => {
                this.innerHTML = '<i class="bi bi-check"></i>';
                this.classList.remove('btn-outline-secondary');
                this.classList.add('btn-success');

                setTimeout(() => {
                    this.innerHTML = '<i class="bi bi-clipboard"></i>';
                    this.classList.remove('btn-success');
                    this.classList.add('btn-outline-secondary');
                }, 2000);
            }).catch(err => {
                console.error('Could not copy text: ', err);
                this.innerHTML = '<i class="bi bi-exclamation-triangle"></i>';
                this.classList.remove('btn-outline-secondary');
                this.classList.add('btn-danger');

                setTimeout(() => {
                    this.innerHTML = '<i class="bi bi-clipboard"></i>';
                    this.classList.remove('btn-danger');
                    this.classList.add('btn-outline-secondary');
                }, 2000);
            });
        });
    });
}

function filterAccountsByClass(classNumber) {
    const accountClasses = document.querySelectorAll('.account-class');

    accountClasses.forEach(accountClass => {
        accountClass.style.display = classNumber === 'all' || accountClass.id === `class-${classNumber}` ? '' : 'none';
    });
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
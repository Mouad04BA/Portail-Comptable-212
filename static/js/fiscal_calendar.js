/**
 * JavaScript functions for the Fiscal Deadlines calendar
 */

document.addEventListener('DOMContentLoaded', function() {
  // Initialize filter buttons
  initDeadlineFilters();
  
  // Initialize calendar visualization
  initCalendarVisualization();
  
  // Initialize deadline countdown display
  initDeadlineCountdown();
});

/**
 * Initialize filter buttons for different tax types
 */
function initDeadlineFilters() {
  const filterButtons = document.querySelectorAll('.deadline-filter');
  
  filterButtons.forEach(button => {
    button.addEventListener('click', function() {
      // Remove active class from all buttons
      filterButtons.forEach(btn => btn.classList.remove('active'));
      
      // Add active class to clicked button
      this.classList.add('active');
      
      // Get filter value
      const filterValue = this.getAttribute('data-filter');
      
      // Filter deadlines
      filterDeadlines(filterValue);
    });
  });
}

/**
 * Filter deadlines by tax type
 * @param {string} filterValue - The tax type to filter by ('is', 'ir', 'tva', 'all')
 */
function filterDeadlines(filterValue) {
  const deadlineItems = document.querySelectorAll('.deadline-item');
  
  deadlineItems.forEach(item => {
    if (filterValue === 'all') {
      item.style.display = '';
      // Animate item back in
      item.classList.add('fade-in');
      setTimeout(() => {
        item.classList.remove('fade-in');
      }, 500);
    } else {
      const taxType = item.getAttribute('data-tax-type').toLowerCase();
      
      if (taxType === filterValue.toLowerCase()) {
        item.style.display = '';
        // Animate item back in
        item.classList.add('fade-in');
        setTimeout(() => {
          item.classList.remove('fade-in');
        }, 500);
      } else {
        item.style.display = 'none';
      }
    }
  });
  
  // Show a message if no deadlines match the filter
  const noDeadlinesMessage = document.getElementById('no-deadlines-message');
  if (noDeadlinesMessage) {
    const visibleDeadlines = document.querySelectorAll('.deadline-item:not([style*="display: none"])').length;
    noDeadlinesMessage.style.display = visibleDeadlines === 0 ? 'block' : 'none';
  }
}

/**
 * Initialize calendar visualization
 */
function initCalendarVisualization() {
  // Get the current date
  const currentDate = new Date();
  const currentYear = currentDate.getFullYear();
  const currentMonth = currentDate.getMonth();
  
  // Initialize calendar if the element exists
  const calendarContainer = document.getElementById('calendar-visualization');
  if (!calendarContainer) return;
  
  // Get all deadlines with proper dates
  const deadlines = [];
  document.querySelectorAll('.deadline-item[data-due-date]').forEach(item => {
    const dateStr = item.getAttribute('data-due-date');
    if (dateStr && dateStr.match(/^\d{4}-\d{2}-\d{2}$/)) {
      const date = new Date(dateStr);
      const taxType = item.getAttribute('data-tax-type');
      const title = item.querySelector('.deadline-title').textContent;
      
      deadlines.push({
        date: date,
        taxType: taxType,
        title: title
      });
    }
  });
  
  // Create year calendar grid
  createYearCalendar(calendarContainer, currentYear, deadlines);
}

/**
 * Create a visual calendar for the year
 * @param {HTMLElement} container - The container to render the calendar in
 * @param {number} year - The year to display
 * @param {Array} deadlines - Array of deadline objects
 */
function createYearCalendar(container, year, deadlines) {
  // Clear container
  container.innerHTML = '';
  
  // Month names
  const monthNames = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
  ];
  
  // Create calendar header
  const header = document.createElement('div');
  header.className = 'calendar-header d-flex justify-content-between align-items-center mb-4';
  header.innerHTML = `
    <h3 class="calendar-year mb-0">${year}</h3>
    <div class="calendar-controls">
      <button class="btn btn-sm btn-outline-secondary calendar-prev-year">
        <i class="bi bi-chevron-left"></i> Previous Year
      </button>
      <button class="btn btn-sm btn-primary calendar-current-year mx-2">
        Current Year
      </button>
      <button class="btn btn-sm btn-outline-secondary calendar-next-year">
        Next Year <i class="bi bi-chevron-right"></i>
      </button>
    </div>
  `;
  container.appendChild(header);
  
  // Add event listeners for year navigation
  header.querySelector('.calendar-prev-year').addEventListener('click', () => {
    createYearCalendar(container, year - 1, deadlines);
  });
  
  header.querySelector('.calendar-current-year').addEventListener('click', () => {
    createYearCalendar(container, new Date().getFullYear(), deadlines);
  });
  
  header.querySelector('.calendar-next-year').addEventListener('click', () => {
    createYearCalendar(container, year + 1, deadlines);
  });
  
  // Create calendar grid
  const calendarGrid = document.createElement('div');
  calendarGrid.className = 'row calendar-grid';
  
  // Add months to grid
  for (let i = 0; i < 12; i++) {
    const monthCard = document.createElement('div');
    monthCard.className = 'col-md-4 col-lg-3 mb-4';
    
    // Create month card
    const firstDay = new Date(year, i, 1);
    const lastDay = new Date(year, i + 1, 0);
    const daysInMonth = lastDay.getDate();
    
    // Filter deadlines for this month
    const monthDeadlines = deadlines.filter(deadline => {
      return deadline.date.getFullYear() === year && deadline.date.getMonth() === i;
    });
    
    // Determine if this month has deadlines
    const hasDeadlines = monthDeadlines.length > 0;
    
    // Create month HTML
    let monthHTML = `
      <div class="card h-100 ${hasDeadlines ? 'border-warning' : ''}">
        <div class="card-header ${hasDeadlines ? 'bg-warning text-dark' : ''} d-flex justify-content-between align-items-center">
          <strong>${monthNames[i]}</strong>
          ${hasDeadlines ? `<span class="badge bg-danger">${monthDeadlines.length}</span>` : ''}
        </div>
        <div class="card-body">
          <div class="calendar-days">
    `;
    
    // Add day names header
    const dayNames = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'];
    monthHTML += '<div class="calendar-days-header">';
    for (let d = 0; d < 7; d++) {
      monthHTML += `<div class="calendar-day-name">${dayNames[d]}</div>`;
    }
    monthHTML += '</div>';
    
    // Add empty cells for days before the first day of the month
    const firstDayOfWeek = firstDay.getDay();
    monthHTML += '<div class="calendar-days-grid">';
    for (let d = 0; d < firstDayOfWeek; d++) {
      monthHTML += '<div class="calendar-day empty"></div>';
    }
    
    // Add days of the month
    const today = new Date();
    for (let d = 1; d <= daysInMonth; d++) {
      const date = new Date(year, i, d);
      const isToday = date.getFullYear() === today.getFullYear() && 
                      date.getMonth() === today.getMonth() && 
                      date.getDate() === today.getDate();
      
      // Check if there are deadlines on this day
      const dayDeadlines = monthDeadlines.filter(deadline => deadline.date.getDate() === d);
      const hasIS = dayDeadlines.some(dl => dl.taxType.toLowerCase() === 'is');
      const hasIR = dayDeadlines.some(dl => dl.taxType.toLowerCase() === 'ir');
      const hasTVA = dayDeadlines.some(dl => dl.taxType.toLowerCase() === 'tva');
      
      // Create day cell with appropriate classes and indicators
      let dayClass = 'calendar-day';
      if (isToday) dayClass += ' today';
      if (dayDeadlines.length > 0) dayClass += ' has-deadline';
      
      monthHTML += `<div class="${dayClass}" data-bs-toggle="tooltip" data-bs-placement="top" title="${dayDeadlines.map(dl => dl.title).join('\n')}">${d}`;
      
      // Add indicators for deadlines
      if (hasIS) monthHTML += '<div class="deadline-dot is"></div>';
      if (hasIR) monthHTML += '<div class="deadline-dot ir"></div>';
      if (hasTVA) monthHTML += '<div class="deadline-dot tva"></div>';
      
      monthHTML += '</div>';
    }
    
    // Add empty cells for days after the last day of the month
    const lastDayOfWeek = lastDay.getDay();
    for (let d = lastDayOfWeek; d < 6; d++) {
      monthHTML += '<div class="calendar-day empty"></div>';
    }
    
    // Close the HTML structure
    monthHTML += `
          </div>
        </div>
      </div>
      ${hasDeadlines ? `
        <div class="deadline-list mt-2">
          <small>
            <ul class="list-unstyled small">
              ${monthDeadlines.map(dl => `<li><span class="badge deadline-${dl.taxType.toLowerCase()}">${dl.taxType}</span> ${dl.date.getDate()}: ${dl.title}</li>`).join('')}
            </ul>
          </small>
        </div>
      ` : ''}
    </div>
    `;
    
    monthCard.innerHTML = monthHTML;
    calendarGrid.appendChild(monthCard);
  }
  
  container.appendChild(calendarGrid);
  
  // Initialize tooltips
  const tooltipTriggerList = [].slice.call(container.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl, {
      boundary: document.body
    });
  });
}

/**
 * Initialize countdown display for upcoming deadlines
 */
function initDeadlineCountdown() {
  const countdownElements = document.querySelectorAll('[data-countdown]');
  
  countdownElements.forEach(element => {
    const targetDateStr = element.getAttribute('data-countdown');
    if (!targetDateStr) return;
    
    const targetDate = new Date(targetDateStr);
    
    // Update countdown immediately
    updateCountdown(element, targetDate);
    
    // Update countdown every day
    setInterval(() => {
      updateCountdown(element, targetDate);
    }, 86400000); // 24 hours
  });
}

/**
 * Update countdown display
 * @param {HTMLElement} element - The element to update
 * @param {Date} targetDate - The target date to count down to
 */
function updateCountdown(element, targetDate) {
  const now = new Date();
  
  // Calculate difference in days
  const diffTime = targetDate - now;
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  
  // Update element content
  if (diffDays > 0) {
    element.textContent = `${diffDays} days`;
    
    // Add urgency classes
    if (diffDays <= 7) {
      element.className = 'badge bg-danger countdown';
    } else if (diffDays <= 30) {
      element.className = 'badge bg-warning text-dark countdown';
    } else {
      element.className = 'badge bg-primary countdown';
    }
  } else if (diffDays === 0) {
    element.textContent = 'Today!';
    element.className = 'badge bg-danger countdown';
  } else {
    element.textContent = 'Passed';
    element.className = 'badge bg-secondary countdown';
  }
}

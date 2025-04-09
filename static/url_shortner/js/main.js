// Theme toggle function
document.addEventListener('DOMContentLoaded', function() {
  const themeToggleBtn = document.getElementById('theme-toggle-btn');
  const htmlElement = document.documentElement;
  
  // saved theme
  const savedTheme = localStorage.getItem('theme') || 'light';
  htmlElement.setAttribute('data-theme', savedTheme);
  
  themeToggleBtn.addEventListener('click', function() {
    const currentTheme = htmlElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    htmlElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
  });
});

// Copy to clipboard function
function copyToClipboard() {
  const shortUrl = document.getElementById('short-url-text');
  const message = document.getElementById('copy-message');
  
  // Create a temporary input element
  const tempInput = document.createElement('input');
  tempInput.value = shortUrl.textContent;
  document.body.appendChild(tempInput);
  
  // Select and copy the text
  tempInput.select();
  document.execCommand('copy');
  
  // Remove the temporary element
  document.body.removeChild(tempInput);
  
  // Show success message
  message.textContent = "Copied to clipboard!";
  
  // Hide message after 2 seconds
  setTimeout(() => {
    message.textContent = "";
  }, 2000);
}

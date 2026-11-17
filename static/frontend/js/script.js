// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function () {
    const searchIcon = document.querySelector('.search-icon');
    const searchContainer = document.querySelector('.search-container');
  
    searchIcon.addEventListener('click', function () {
      searchContainer.classList.toggle('active');
    });
  });

  

  document.getElementById("search-icon").addEventListener("click", function () {
    const query = document.getElementById("search-input").value.toLowerCase();
    const content = document.getElementById("main-content");
  
    if (!query) return;
  
    // Remove previous highlights
    const highlights = content.querySelectorAll("mark");
    highlights.forEach(mark => {
      const parent = mark.parentNode;
      parent.replaceChild(document.createTextNode(mark.textContent), mark);
      parent.normalize(); // Combine adjacent text nodes
    });
  
    // Search and highlight matches
    const textNodes = Array.from(content.childNodes).filter(node => node.nodeType === 3 || node.nodeType === 1);
    textNodes.forEach(node => {
      if (node.nodeType === 3 && node.textContent.toLowerCase().includes(query)) {
        const regex = new RegExp(`(${query})`, "gi");
        const newHtml = node.textContent.replace(regex, `<mark>$1</mark>`);
        const span = document.createElement("span");
        span.innerHTML = newHtml;
        node.replaceWith(span);
      }
    });
  });
  
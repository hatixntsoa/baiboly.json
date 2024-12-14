let category = ''; // Set default category to 'old'

// Automatically load the Old Testament by default
window.onload = function() {
  loadBooks('old');
}

function loadBooks(selectedCategory) {
  category = selectedCategory;
  fetch(`/books/${category}`)
    .then(response => response.json())
    .then(books => {
      const booksDropdown = document.getElementById('books');
      booksDropdown.innerHTML = books.map(book => `<option value="${book.file_name}">${book.display_name}</option>`).join('');
      // Reset and set to the first book (default)
      resetVerseSelections();
      loadChapters();
    });
}

function toRoman(num) {
  const romanNumerals = [
    ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
    ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
    ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
    ["", "M", "MM", "MMM"]
  ];

  let roman = "";
  let i = 0;

  while (num > 0) {
    let digit = num % 10;
    roman = romanNumerals[i][digit] + roman;
    num = Math.floor(num / 10);
    i++;
  }

  return roman;
}

function loadChapters() {
  const book = document.getElementById('books').value;
  if (!book) return; // Don't proceed if no book is selected

  fetch(`/chapters/${category}/${book}`)
    .then(response => response.json())
    .then(chapters => {
      const chaptersDropdown = document.getElementById('chapters');
      // Map the chapter numbers to Roman numerals only in the displayed text
      chaptersDropdown.innerHTML = chapters.map(ch => 
        // `<option value="${ch}">${toRoman(parseInt(ch))}</option>`
        `<option value="${ch}">${parseInt(ch)}</option>`
      ).join('');

      // Set the chapter to 1 and load verses
      document.getElementById('chapters').value = '1';
      loadVerses();
    });
}

function loadVerses() {
  const book = document.getElementById('books').value;
  const chapter = document.getElementById('chapters').value;
  if (!chapter) return; // Don't proceed if no chapter is selected
  fetch(`/verses/${category}/${book}/${chapter}`)
    .then(response => response.json())
    .then(verses => {
      const startDropdown = document.getElementById('start-verse');
      const endDropdown = document.getElementById('end-verse');
      startDropdown.innerHTML = verses.map(verse => `<option value="${verse}">${verse}</option>`).join('');
      endDropdown.innerHTML = verses.map(verse => `<option value="${verse}">${verse}</option>`).join('');
      // Set the start and end verse to 1, then render the verse
      const lastVerse = verses[verses.length - 1];
      document.getElementById('start-verse').value = '1';
      // document.getElementById('end-verse').value = '1';
      document.getElementById('end-verse').value = lastVerse;
      renderVerses();
    });
}

function updateEndVerseOptionsAndRender() {
  const startVerse = parseInt(document.getElementById('start-verse').value, 10);
  const book = document.getElementById('books').value;
  const chapter = document.getElementById('chapters').value;

  fetch(`/verses/${category}/${book}/${chapter}`)
    .then(response => response.json())
    .then(verses => {
      // Filter the verses so that the end verse is greater than or equal to the start verse
      const validEndVerses = verses.filter(verse => parseInt(verse, 10) >= startVerse);

      const endDropdown = document.getElementById('end-verse');
      endDropdown.innerHTML = validEndVerses.map(verse => `<option value="${verse}">${verse}</option>`).join('');
      // Also, set the end verse to the same value as the start verse
      // document.getElementById('end-verse').value = startVerse;

      // Set the end verse to the last verse
      const lastVerse = verses[verses.length - 1];
      document.getElementById('end-verse').value = lastVerse;

      renderVerses(); // Render verses immediately after updating the start verse
    });
}

function renderVerses() {
  const book = document.getElementById('books').value;
  const chapter = document.getElementById('chapters').value;
  const start = document.getElementById('start-verse').value;
  const end = document.getElementById('end-verse').value;

  if (!start || !end) return; // Don't render if no start or end verse is selected

  fetch(`/render/${category}/${book}/${chapter}/${start}/${end}`)
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById('data-container'); // The textarea itself

      // Prepare the verses content
      let versesContent = '';
      for (const [key, value] of Object.entries(data)) {
        // Decode Unicode escape sequences
        const decodedValue = value.replace(/\\u[\dA-F]{4}/gi, (match) => {
            return String.fromCharCode(parseInt(match.replace(/\\u/g, ''), 16));
        });

        versesContent += `<span class="verse-title">${key}</span> ${decodedValue}<br>`;
      }

      // Set the content inside the textarea (data-container)
      container.innerHTML = versesContent;
  })
  .catch(error => {
    console.error('Error fetching verses:', error);
    const container = document.getElementById('data-container');
    container.value = 'Failed to load verses. Please try again later.';
  });
}


function resetVerseSelections() {
  // Reset the start and end verse selections to 1
  document.getElementById('start-verse').value = '1';
  document.getElementById('end-verse').value = '1';
}

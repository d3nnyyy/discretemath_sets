const form = document.querySelector('form');
const uniqueElementsResult = document.querySelector('#unique-elements-result');

form.addEventListener('submit', event => {
    event.preventDefault();
    const input = document.querySelector('#array-input');
    const arrayInputValue = input.value.trim();
    const array = arrayInputValue.split(/\s+/).map(item => parseInt(item.trim())).filter(item => !isNaN(item));
    const uniqueArray = [...new Set(array)];
    uniqueElementsResult.textContent = `Результат: [${uniqueArray.join(', ')}]`;
});
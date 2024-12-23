const inputEl = document.getElementById('input');

const outputController = new OutputController("output");

inputEl.addEventListener('input', (evt) => display(evt, outputController));
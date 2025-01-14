

function processText() {
    const textInput = document.getElementById('text').value;
    const resultOutput = document.getElementById('result');
    const removeNumbers = document.getElementById('remove-numbers').checked;
    const addTonics = document.getElementById('add-tonics').checked;

    let text = " " + textInput;
    if (removeNumbers) {
        text = text.replace(/\d/gm, '');
    }
    if (addTonics) {
        let words = text.split(" ");
        let result = "";
        for (let word of words) {
            let syllables = separarTexto(word).split("-");
            let tonicNumber = tonica(syllables);
            tonicNumber = syllables.length - tonicNumber;
            syllables[tonicNumber] = "<b>" + syllables[tonicNumber] + "</b>";

            result += syllables.join("-") + " ";
        }
        resultOutput.innerHTML = result;
        return;
    }
    const processedText = separateWord(text);
    resultOutput.innerHTML = processedText;
}


async function processText() {
    const inputText = document.getElementById('inputText').value;
    
    const datas = await (await fetch('datas.json')).json()

    let resultText = inputText;
    for (let data of datas) {
        const [, replacement, original] = data;
        console.log(replacement, original)
        const regex = new RegExp(original, 'g');
        resultText = resultText.replace(regex, replacement);
    }

    document.getElementById('result').innerText = resultText;
}

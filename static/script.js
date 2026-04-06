const input = document.getElementById("textInput")

input.addEventListener("input",async() =>{
    const response = await fetch("/analyze" , {
        method:"POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({text: input.value})
})
const data = await response.json()

document.getElementById("words").innerText = data.word_count
document.getElementById("sentences").innerText = data.sentence_count
document.getElementById("time").innerText = data.reading_time
document.getElementById("tone").innerText = data.tone

const list = document.getElementById("common")
list.innerHTML = ""
data.common_words.forEach(item => {
    const li = document.createElement("Li")
    li.innerText = item[0] + " (" + item[1]+ ") "
    list.appendChild(li)
    })
})
const toneElement = document.getElementById("tone")
toneElement.innerText = data.tone

toneElement.classList.remove("positive", "negative", "neutral")

if (data.tone === "Positive") {
    toneElement.classList.add("positive")
} else if (data.tone === "Negative") {
    toneElement.classList.add("negative")
} else {
    toneElement.classList.add("neutral")
}

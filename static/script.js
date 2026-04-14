const input = document.getElementById("textInput")

input.addEventListener("input", async () => {

    if (input.value.trim() === "") return

    const response = await fetch("/analyze", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text: input.value})
    })

    const data = await response.json()

    document.getElementById("words").innerText = data.word_count
    document.getElementById("sentences").innerText = data.sentence_count
    document.getElementById("time").innerText = data.reading_time

    const toneElement = document.getElementById("tone")
    toneElement.innerText = data.tone

    toneElement.classList.remove("positive", "negative", "neutral")

    if (data.tone.includes("Positive")) {
        toneElement.classList.add("positive")
    } else if (data.tone.includes("Negative")) {
        toneElement.classList.add("negative")
    } else {
        toneElement.classList.add("neutral")
    }

    document.getElementById("toneMessage").innerText = data.tone_message
    document.getElementById("formatType").innerText = data.format_type
    document.getElementById("formatSuggestion").innerText = data.format_suggestion

    const list = document.getElementById("common")
    list.innerHTML = ""

    data.common_words.forEach(item => {
        const li = document.createElement("li")
        li.innerText = item[0] + " (" + item[1] + ")"
        list.appendChild(li)
    })
})

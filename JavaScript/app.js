const speech = new SpeechSynthesisUtterance();

document.getElementById("button").addEventListener("click", () => {
  setTimeout(() => {
    speech.text = document.getElementById("voice").value;
    window.speechSynthesis.speak(speech);
  }, 200);
});

// Gerar um número aleatório entre 1 e 10
const randomNumber = Math.floor(Math.random() * 10) + 1;
console.log("Número gerado:", randomNumber);  // Para debug durante o desenvolvimento

// Consequências em caso de erro
const consequences = [
    "Escolha alguem para falar uma verdade sobre alguém do grupo!",
    "Agora você deve beber um copo de água.",
    "Cante sua música favorita!",
    "Dê uma volta pela casa!",
    "Você perdeu, dance por 30 segundos!",
    "Faça uma careta engraçada!",
    "Conte uma piada para alguém!",
    "Faça uma corrida no lugar por 20 segundos.",
    "Você precisa fazer uma tarefa que estava adiando!",
    "Tente novamente!"
];

document.getElementById("submitBtn").addEventListener("click", function() {
    const userInput = parseInt(document.getElementById("userInput").value);
    const resultElement = document.getElementById("result");
    const consequenceElement = document.getElementById("consequence");

    if (!userInput || userInput < 1 || userInput > 10) {
        resultElement.textContent = "Por favor, insira um número entre 1 e 10.";
        resultElement.style.color = "red";
        consequenceElement.textContent = "";
    } else if (userInput === randomNumber) {
        resultElement.textContent = "Parabéns! Você acertou!";
        resultElement.style.color = "green";
        consequenceElement.textContent = "";
    } else {
        resultElement.textContent = "Errou! Tente novamente.";
        resultElement.style.color = "red";
        // Exibir uma consequência aleatória
        const randomConsequence = consequences[Math.floor(Math.random() * consequences.length)];
        consequenceElement.textContent = randomConsequence;
    }
});

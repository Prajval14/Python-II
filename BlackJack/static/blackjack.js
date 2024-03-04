document.addEventListener("DOMContentLoaded", function() {
    let game_dealer_hand = JSON.parse(document.getElementById("game-dealer-hand").textContent);
    let game_player_hand = JSON.parse(document.getElementById("game-player-hand").textContent);  
    let game_dealer_score = JSON.parse(document.getElementById("game-dealer-score").textContent);
    let game_player_score = JSON.parse(document.getElementById("game-player-score").textContent);    

    // Initial game setup
    distributeCardsAndScore(game_dealer_hand, game_player_hand, game_dealer_score, game_player_score);

    //Button click functions
    document.getElementById('hit-button').addEventListener('click', () => handleAction('/hit', updatePlayerCardsAndScore));
    document.getElementById('stay-button').addEventListener('click', () => handleAction('/stay', updateDealerCardsAndScore));
    document.getElementById('restart-game').addEventListener('click', () => location.reload());
});

// Function to handle hit or stay actions
function handleAction(endpoint, updateFunction) {
    fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
    })
    .then(response => response.json())
    .then(data => updateFunction(data))
    .catch(error => console.error('Error:', error));
}

// Funtion to initially add cards in hana and score
function distributeCardsAndScore(dealerHand, playerHand, dealerScore, playerScore) {
    for (const hand of [dealerHand, playerHand]) {
        for (const card of hand) {
            const cardImg = createCardImage(card);
            document.getElementById(hand === dealerHand ? "dealer-cards" : "player-cards").append(cardImg);
        }
    }
    document.getElementById("dealer-score").innerText = dealerScore;
    document.getElementById("player-score").innerText = playerScore;
}

// Function to create card image element
function createCardImage(card) {
    const cardImg = document.createElement("img");
    cardImg.src = `../static/images/cards/${card.name}-${card.suit}.png`;
    return cardImg;
}

// Function to update player's cards and score
function updatePlayerCardsAndScore(response) {
    const cardImg = createCardImage(response[0]);
    document.getElementById("player-cards").append(cardImg);
    document.getElementById("player-score").innerText = response[1];
    if (response.length > 2) declareWinner(response[2]);
}

// Function to update dealer's cards and score
async function updateDealerCardsAndScore(response) {
    let hiddenImg = document.getElementById('hidden-img');
    const dealerScoreElem = document.getElementById("dealer-score");
    let dealerScore = parseInt(dealerScoreElem.innerText);
    
    // The first hidden card is revealed
    hiddenImg.src = "../static/images/cards/" + response[0][0].name + "-" + response[0][0].suit + ".png";
    dealerScore += response[0][0].value;
    dealerScoreElem.innerText = dealerScore;

    for(let i = 1; i < response[0].length; i++) {
        const cardImg = createCardImage(response[0][i]);
        await new Promise(resolve => setTimeout(resolve, 1000)); // Pause execution for 1 second
        document.getElementById("dealer-cards").append(cardImg);
        dealerScore += response[0][i].value;
        dealerScoreElem.innerText = dealerScore;
    }
    
    declareWinner(response[1]);
}

// Function to declare the winner and end the game
function declareWinner(status) {
    const overlayImg = document.createElement("img");
    const messages = {
        'dealer-busted': ["../static/images/busted.png", "You Won!"],
        'player-busted': ["../static/images/busted.png", "Dealer Won!"],
        'tie': ["../static/images/winner.png", "It's a Tie!"],
        'dealer-win': ["../static/images/winner.png", "Dealer Won!"],
        'player-win': ["../static/images/winner.png", "You Won!"]
    };

    const [imgSrc, msg] = messages[status] || ['../static/images/error.png', 'Game Error!'];

    overlayImg.src = imgSrc;
    document.getElementById("over-lay-image").append(overlayImg);
    document.getElementById("over-lay-msg").innerText = msg;
    document.getElementById("over-lay").style.display = 'block';
}
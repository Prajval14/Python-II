document.addEventListener("DOMContentLoaded", function() {
    let dealer_hand = JSON.parse(document.getElementById("dealer-hand").textContent);
    let player_hand = JSON.parse(document.getElementById("player-hand").textContent); 
    let deck_instance = JSON.parse(document.getElementById("deck").textContent); 
    // console.log(deck_instance);
    // debugger
    let dealerSum = 0;
    let playerSum = 0;

    const scores = startGame(dealer_hand, player_hand, dealerSum, playerSum);
    
    document.getElementById("hit-button").addEventListener("click", function() {
        hit(deck_instance, scores.dealerSum, scores.playerSum);
    });
    document.getElementById("stay-button").addEventListener("click", function() {
        stay(deck_instance, scores.dealerSum, scores.playerSum);
    });
});

function startGame(dealer_hand, player_hand, dealerSum, playerSum) {
    for(let card in dealer_hand) {        
        dealerSum += dealer_hand[card].value;
        
        let cardImg = document.createElement("img");
        cardImg.src = "../static/images/cards/" + dealer_hand[card].value + "-" + dealer_hand[card].suit + ".png";
        document.getElementById("dealer-cards").append(cardImg);
    }
    for(let card in player_hand) {        
        playerSum += player_hand[card].value;
        
        let cardImg = document.createElement("img");
        cardImg.src = "../static/images/cards/" + player_hand[card].value + "-" + player_hand[card].suit + ".png";
        document.getElementById("player-cards").append(cardImg);
    }
    
    document.getElementById("dealer-score").innerText = dealerSum;
    document.getElementById("player-score").innerText = playerSum;

    return { dealerSum, playerSum };
}

function hit(deck_instance, dealerSum, playerSum) {
    // debugger
    let playerName = "Player";  
    fetch('/hit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ player_name: playerName, deck_instance:deck_instance, dealer_score: dealerSum, player_score: playerSum })
    });
}

function stay(dealerSum, playerSum) {
    let playerName = "Player";
    fetch('/stay', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ player_name: playerName, dealer_score: dealerSum, player_score: playerSum })
    });
}
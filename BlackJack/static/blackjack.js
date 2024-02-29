document.addEventListener("DOMContentLoaded", function() {
    var dealer_hand = JSON.parse(document.getElementById("dealer-hand").textContent);
    var player_hand = JSON.parse(document.getElementById("player-hand").textContent);
    
    startGame(dealer_hand, player_hand)
});

function startGame(dealer_hand,player_hand) {
    let dealerSum = 0;
    let playerSum = 0;

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
}
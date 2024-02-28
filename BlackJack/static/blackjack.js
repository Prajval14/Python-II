document.addEventListener("DOMContentLoaded", function() {
    var dealer_hand = JSON.parse(document.getElementById("dealer-hand").textContent);
    
    startGame(dealer_hand)
});

function startGame(dealer_hand) {
    let dealerSum = 0;

    for(let card in dealer_hand) {        
        dealerSum += dealer_hand[card].value;
        
        let cardImg = document.createElement("img");
        cardImg.src = "../static/images/cards/" + dealer_hand[card].value + "-" + dealer_hand[card].suit + ".png";
        document.getElementById("dealer_cards").append(cardImg);
    }
    console.log(dealerSum);    
}
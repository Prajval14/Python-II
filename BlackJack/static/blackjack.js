document.addEventListener("DOMContentLoaded", function() {
    let game_dealer_hand = JSON.parse(document.getElementById("game-dealer-hand").textContent);
    let game_player_hand = JSON.parse(document.getElementById("game-player-hand").textContent);  
    let game_dealer_score = JSON.parse(document.getElementById("game-dealer-score").textContent);
    let game_player_score = JSON.parse(document.getElementById("game-player-score").textContent);     

    distributeCardsAndScore(game_dealer_hand, game_player_hand, game_dealer_score, game_player_score);

    //vanilla JavaScript's fetch API.
    document.getElementById('hit-button').addEventListener('click', function() {
        fetch('/hit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
        })
        .then(response => response.json())
        .then(data => {
            updatePlayerCardsAndScore(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });    
});

function distributeCardsAndScore(game_dealer_hand, game_player_hand, game_dealer_score, game_player_score) {
    for(let card in game_dealer_hand) {                
        let cardImg = document.createElement("img");
        cardImg.src = "../static/images/cards/" + game_dealer_hand[card].value + "-" + game_dealer_hand[card].suit + ".png";
        document.getElementById("dealer-cards").append(cardImg);
    }
    for(let card in game_player_hand) {                
        let cardImg = document.createElement("img");
        cardImg.src = "../static/images/cards/" + game_player_hand[card].value + "-" + game_player_hand[card].suit + ".png";
        document.getElementById("player-cards").append(cardImg);
    }
    
    document.getElementById("dealer-score").innerText = game_dealer_score;
    document.getElementById("player-score").innerText = game_player_score;
}

function updatePlayerCardsAndScore(response) {
    console.log(response)
    let cardImg = document.createElement("img");
    cardImg.src = "../static/images/cards/" + response[0].value + "-" + response[0].suit + ".png";
    document.getElementById("player-cards").append(cardImg);
}
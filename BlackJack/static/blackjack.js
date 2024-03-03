document.addEventListener("DOMContentLoaded", function() {
    let game_dealer_hand = JSON.parse(document.getElementById("game-dealer-hand").textContent);
    let game_player_hand = JSON.parse(document.getElementById("game-player-hand").textContent);  
    let game_dealer_score = JSON.parse(document.getElementById("game-dealer-score").textContent);
    let game_player_score = JSON.parse(document.getElementById("game-player-score").textContent);    

    distributeCardsAndScore(game_dealer_hand, game_player_hand, game_dealer_score, game_player_score);

    document.getElementById('hit-button').addEventListener('click', function() {
        //vanilla JavaScript's fetch API.
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
    
    document.getElementById('stay-button').addEventListener('click', function() {
        fetch('/stay', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
        })
        .then(response => response.json())
        .then(data => {
            updateDealerCardsAndScore(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    document.getElementById('restart-game').addEventListener('click', function() {
        location.reload();
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

    document.getElementById("player-score").innerText = response[1];

    if(response[1] > 21){
        busted('Dealer');
    }
}

function updateDealerCardsAndScore(response) { 
    console.log(response)

    let hiddenImg = document.getElementById('hidden-img');
    hiddenImg.src = "../static/images/cards/" + response[0][0].value + "-" + response[0][0].suit + ".png";

    for(let i = 1; i < response[0].length; i++) {
        let cardImg = document.createElement("img");
        cardImg.src = "../static/images/cards/" + response[0][i].value + "-" + response[0][i].suit + ".png";
        setTimeout(function() {
            document.getElementById("dealer-cards").append(cardImg);
        }, 1000 * i);        
    }

    document.getElementById("dealer-score").innerText = response[1];

    // if(response[1] > 21){
    //     busted('You');
    // }    
}

function busted(playerName) {
    let overlayImg = document.createElement("img");
    overlayImg.src = "../static/images/busted.png"
    document.getElementById("over-lay-image").append(overlayImg);
    document.getElementById("over-lay-msg").innerText = playerName + ' Won!';
    document.getElementById("over-lay").style.display = 'block';
}
document.addEventListener("DOMContentLoaded", function() {
    let game_dealer_hand = JSON.parse(document.getElementById("game-dealer-hand").textContent);
    let game_player_hand = JSON.parse(document.getElementById("game-player-hand").textContent);  
    let game_dealer_score = JSON.parse(document.getElementById("game-dealer-score").textContent);
    let game_player_score = JSON.parse(document.getElementById("game-player-score").textContent);    

    // Initial game setup
    distributeCardsAndScore(game_dealer_hand, game_player_hand, game_dealer_score, game_player_score);

    //JS fetch API to make a post request to backend
    document.getElementById('hit-button').addEventListener('click', function() {        
        fetch('/hit', {
            method: 'POST', //Not passing any data so can be GET as well
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
    
    // Same API for stay scenario from player
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

// Funtion to initially add cards in hana and score
function distributeCardsAndScore(game_dealer_hand, game_player_hand, game_dealer_score, game_player_score) {
    for(let card in game_dealer_hand) {                
        let cardImg = document.createElement("img");
        cardImg.src = "../static/images/cards/" + game_dealer_hand[card].name + "-" + game_dealer_hand[card].suit + ".png";
        document.getElementById("dealer-cards").append(cardImg);
    }
    for(let card in game_player_hand) {                
        let cardImg = document.createElement("img");
        cardImg.src = "../static/images/cards/" + game_player_hand[card].name + "-" + game_player_hand[card].suit + ".png";
        document.getElementById("player-cards").append(cardImg);
    }
    
    document.getElementById("dealer-score").innerText = game_dealer_score;
    document.getElementById("player-score").innerText = game_player_score;
}

// Function to set player's hand if player chooses to hit
function updatePlayerCardsAndScore(response) {    
    let cardImg = document.createElement("img");
    cardImg.src = "../static/images/cards/" + response[0].name + "-" + response[0].suit + ".png";
    document.getElementById("player-cards").append(cardImg);
    document.getElementById("player-score").innerText = response[1];

    // If player is busted
    if(response.length > 2) {
        declareWinner(response[2]);
    }
}

// Function to set dealer's hand if player choose to stay
async function updateDealerCardsAndScore(response) {     
    let hiddenImg = document.getElementById('hidden-img');
    let dealerScore = parseInt(document.getElementById("dealer-score").innerText)

    // The first hidden card is revealed
    hiddenImg.src = "../static/images/cards/" + response[0][0].name + "-" + response[0][0].suit + ".png";
    dealerScore += response[0][0].value;
    document.getElementById("dealer-score").innerText = dealerScore;

    //If more than 1 card is drawn:
    for(let i = 1; i < response[0].length; i++) {
        let cardImg = document.createElement("img");
        cardImg.src = "../static/images/cards/" + response[0][i].name + "-" + response[0][i].suit + ".png";
        await new Promise(resolve => setTimeout(resolve, 1000)); // Pause execution for 1 second
        document.getElementById("dealer-cards").append(cardImg);
        dealerScore += response[0][i].value;
        document.getElementById("dealer-score").innerText = dealerScore;      
    }  
    
    //Finally declare winners and end game
    declareWinner(response[1]);
}

//Funtion to get game winner status and show in UI
function declareWinner(status){
    let overlayImg = document.createElement("img");
    let msg = ''
    if(status == 'dealer-busted') {
        overlayImg.src = "../static/images/busted.png"
        msg = "You Won!"
    }
    else if(status == 'player-busted') {
        overlayImg.src = "../static/images/busted.png"
        msg = "Dealer Won!"
    }
    else if(status == 'tie') {
        overlayImg.src = "../static/images/winner.png"
        msg = "It's a Tie!"
    }
    else if(status == 'dealer-win') {
        overlayImg.src = "../static/images/winner.png"
        msg = "Dealer Won!"
    }
    else if(status == 'player-win') {
        overlayImg.src = "../static/images/winner.png"
        msg = "You Won!"
    }
    else {
        alert('Game Error!')
    }

    document.getElementById("over-lay-image").append(overlayImg);
    document.getElementById("over-lay-msg").innerText = msg;
    document.getElementById("over-lay").style.display = 'block';
}
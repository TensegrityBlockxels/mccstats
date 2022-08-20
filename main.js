function random(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    let randomn = Math.floor(Math.random() * (max - min) + min);
    return randomn;
}
// function updateTotalScore() {
//     let total_score = document.querySelector("#total-score");
//     total_score.textContent = "Total coins: " + getScore();
// }
// function updateGameScore() {
//     let game_score = document.querySelector("#game-score");
//     let select_game = document.querySelector(".game-selector")
//     let selected_game = select_game.options[select_game.selectedIndex].text
//     console.log(selected_game)
//     game_score.textContent = selected_game + " coins: " + getScore();
// }



// let today = new Date();
// if (today.getDay() == 4) {
//     updateTotalScore();
// }



let score = 0;
let newScore;
console.log("start");
const testCode = async () => {
    const response = await fetch(`http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1`);
    const myjson = await response.json();
    for (let i = 0; i < myjson.dates[0].games.length; i++){
       //console.log(myjson.dates[0].games[i].teams.home.team.name);
       //console.log(myjson.dates[0].games[i].status.statusCode);
   if (myjson.dates[0].games[i].teams.home.team.name == "New York Mets" && myjson.dates[0].games[i].status.statusCode == `I`){
    console.log("Found");
  console.log(myjson.dates[0].games[i].teams.home.score);
  newScore = myjson.dates[0].games[i].teams.home.score;
  console.log("The score of the game is " + newScore);
  console.log(score);
    }
    else{
        console.log("Miami Marlins not found in JSON");
    }
}
if(newScore > score){
console.log("homerun");
score = newScore;
console.log(score);
}
//    console.log(myjson.dates[0].games);
//console.log(myjson.dates[0].games[0].teams.home.score);
}
testCode();
//[0]['teams']['home']['score']
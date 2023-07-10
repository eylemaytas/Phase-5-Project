import React from "react";
import Game from "./Game";

function GameList({games, gameFocusSelector}) {

    const game = games.map(game => {
        return <Game game={game} key={game.id} gameFocusSelector={gameFocusSelector}/>
    })

    return(
        <div className="game-grid">
            {game}
        </div>
    )
}

export default GameList
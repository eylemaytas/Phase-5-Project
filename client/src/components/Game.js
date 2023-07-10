import React from "react";

function Game({game, gameFocusSelector}) {
    
    return(
        <div className="game-card">
            <img onClick={gameFocusSelector} src={game.image} alt={game.id} />
            <h2>{game.name}</h2>
        </div>
    )
}

export default Game
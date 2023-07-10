import React from "react";

function DeveloperFocusCard({game}) {

    return(
        <div className="developer-focus-card">
            <img src={game.image} alt="hi" />
            <p>{game.name}</p>
        </div>
    )
}

export default DeveloperFocusCard
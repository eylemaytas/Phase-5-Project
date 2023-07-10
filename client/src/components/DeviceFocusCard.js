import React from "react";

function DeviceFocusCard({game}) {

    return(
        <div className="device-focus-card">
            <img src={game.image} alt="hi" />
            <p>{game.name}</p>
        </div>
    )
}

export default DeviceFocusCard
import React from "react";

function Continent({continent, continentFocusSelector}) {

    return(
        <div className="continent-card">
            <h2>{continent.name}</h2>
            <img onClick={continentFocusSelector} src={continent.image} alt={continent.id} />
        </div>
    )
}

export default Continent
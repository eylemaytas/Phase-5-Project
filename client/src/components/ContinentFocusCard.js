import React from "react";

function ContinentFocusCard({city}) {

    return(
        <div className="continent-focus-card">
            <img src={city.image} alt="cityimage" />
            <p>{city.name}</p>
        </div>
    )
}

export default ContinentFocusCard
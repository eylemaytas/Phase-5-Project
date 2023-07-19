import React from "react";

function ContinentFocusCard({city}) {

    return(
        <div className="continent-focus-card">
            <p>{city.name}</p>
            <img src={city.image} alt="cityimage" />
        </div>
    )
}

export default ContinentFocusCard
import React from "react";

function City({city, cityFocusSelector}) {
    
    return(
        <div className="city-card">
            <img onClick={cityFocusSelector} src={city.image} alt={city.id} />
            <h2>{city.name}</h2>
            <p>Language: {city.language}</p>
        </div>
    )
}

export default City
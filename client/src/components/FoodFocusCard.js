import React from "react";

function FoodFocusCard({city}) {

    return(
        <div className="food-focus-card">
            <img src={city.image} alt="cityimage" />
            <p>{city.name}</p> 
        </div>
    )
}

export default FoodFocusCard




import React from "react";

function Food({food, foodFocusSelector}) {

    return(
        <div className="food-card">
            <img onClick={foodFocusSelector} src={food.image} alt={food.id} />
            <h2>{food.name}</h2>
        </div>
    )
}

export default Food
import React from "react";
import Food from "./Food";

function FoodList({foods, foodFocusSelector}) {

    const food = foods.map(food => {
        return <Food food={food} foodFocusSelector={foodFocusSelector}/>
    })
    return(
        <div className="food-grid">
            {food}
        </div>
    )
}

export default FoodList
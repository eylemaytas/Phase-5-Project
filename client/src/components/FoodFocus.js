import React, { useEffect, useState } from "react";
import FoodFocusCard from "./FoodFocusCard";

function FoodFocus({focusFood}) {

    const [selectedFood, setSelectedFood] = useState([])
    
    useEffect(() => {
        fetch(`http://127.0.0.1:7001/foods/${focusFood}`)
        .then(res => res.json())
        .then(selectedFood => setSelectedFood(selectedFood))
      }, [focusFood])

    if(!selectedFood.cities){
        return(
            <h1>Loading...</h1>
        )
    }

    

    const focusCard = selectedFood.cities.map(city => {
        return <FoodFocusCard key={city.id} city={city}/>
    })

    return(
        <div className="food-focus-page">
            <h2>{selectedFood.name}</h2>
            <img src={selectedFood.image} alt="food" />
            <p>{selectedFood.description}</p>
            <p>You should try it at {selectedFood.restaurant_recommendation} Restaurant.</p>
            <p>This restaurant is in:</p>
            {focusCard}
        </div>
    )
}

export default FoodFocus



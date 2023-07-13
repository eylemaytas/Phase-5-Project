import React, { useEffect, useState } from "react";
import ContinentFocusCard from "./ContinentFocusCard";

function ContinentFocus({focusContinent}) {

    const [selectedContinent, setSelectedContinent] = useState([])

    useEffect(() => {
        fetch(`http://127.0.0.1:7001/continents/${focusContinent}`)
        .then(res => res.json())
        .then(selectedContinent => setSelectedContinent(selectedContinent))
      }, [focusContinent])

    if(!selectedContinent.cities){
        return(
            <h1>Loading...</h1>
        )
    }

    const focusCard = selectedContinent.cities.map(city => {
        return <ContinentFocusCard key={city.id} city={city}/>
    })

    return(
        <div className="continent-focus-page">
            <h2>{selectedContinent.name}</h2>
            <img src={selectedContinent.image} alt="continentimage" />
            <h2>Popular cities in this continent:</h2>
            {focusCard}
        </div>
    )
}

export default ContinentFocus
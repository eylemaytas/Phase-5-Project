import React, { useEffect, useState } from "react";

function CityFocus({focusCity}) {

    const [selectedCity, setSelectedCity] = useState([])
    const [cityContinents, setCityContinents] = useState([])

    useEffect(() => {
        fetch(`http://127.0.0.1:7001/cities/${focusCity}`)
        .then(res => res.json())
        .then(selectedCity => setSelectedCity(selectedCity), setCityContinents(selectedCity.continents))
    }, [])

    if(!selectedCity.continents){
        return(
            <h1>Loading...</h1>
        )
    }

    const continents = selectedCity.continents.map(continent => {
        return (
            <div className="continent-focus-card">
                <img src={continent.image} alt={continent.id} />
                <p>{continent.name}</p>
            </div>
        )
    })

    console.log(selectedCity.continents)

    return(
        <div className="city-focus">
            <h2>{selectedCity.name}</h2>
            <img className="city-focus-img" src={selectedCity.image} alt="selectedcityimage" />
            <p>{selectedCity.description}</p>
            <p>Language: {selectedCity.language}</p>
            <h2>Foods:</h2>
            <div className="continent-focus-card">
                <img src={selectedCity.foods[0].image}/>
                <p>{selectedCity.foods[0].name}</p>
            </div>
            <h2>This city is in :</h2>
            {continents}
        </div>
    )
}

export default CityFocus
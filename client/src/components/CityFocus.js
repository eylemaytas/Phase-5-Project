import React, { useEffect, useState } from "react";

function CityFocus({ focusCity }) {

    const [selectedCity, setSelectedCity] = useState(null);
    const [cityContinents, setCityContinents] = useState([]);

    useEffect(() => {
        fetch(`http://127.0.0.1:7001/cities/${focusCity}`)
        .then(res => res.json())
        .then(selectedCityData => {
            setSelectedCity(selectedCityData);
            setCityContinents(selectedCityData.continents);
        })
        .catch(error => {
            console.error("Error fetching city data:", error);
        });
    }, [focusCity]);

    if (!selectedCity) {
        return (
            <h1>Loading...</h1>
        );
    }

    const continents = selectedCity.continents.length > 0 ? selectedCity.continents.map(continent => (
        <div className="city-focus-card" key={continent.id}>
            <img src={continent.image} alt={continent.id} />
            <p>{continent.name}</p>
        </div>
    )) : <p>No continent available.</p>;

    const cityFoods = selectedCity.foods.map(food => (
        <div className="city-focus-card1" key={food.id}>
            <img src={food.image} alt="city-food" />
            <p>{food.name}</p>
        </div>
    ));

    return (
        <div className="city-focus">
            <h2>{selectedCity.name}</h2>
            <img className="city-focus-img" src={selectedCity.image} alt="selectedcityimage" />
            <p>{selectedCity.description}</p>
            <p>Language: {selectedCity.language}</p>
            <h2>The most popular foods are:</h2>
            {cityFoods.length > 0 ? cityFoods : <p>No foods available.</p>}
            <h2>{selectedCity.name} is in :</h2>
            {continents}
        </div>
    );
}

export default CityFocus;

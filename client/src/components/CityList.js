import React from "react";
import City from "./City";

function CityList({cities, cityFocusSelector}) {

    const city = cities.map(city => {
        return <City city={city} key={city.id} cityFocusSelector={cityFocusSelector}/>
    })

    return(
        <div className="city-grid">
            {city}
        </div>
    )
}

export default CityList
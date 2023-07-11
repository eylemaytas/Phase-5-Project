import React from "react";
import Continent from "./Continent";

function ContinentList({continents, continentFocusSelector}) {

    const continent = continents.map((continent) => {
        return <Continent key={continent.id} continent={continent} continentFocusSelector={continentFocusSelector}/>
    })

    return(
        <div className="continent-grid">
            {continent}
        </div>
    )
}

export default ContinentList
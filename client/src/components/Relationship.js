import React from "react";

function Relationship({relationship}) {

    return(
        <>
        <div className="continent-card">
            <h2>{relationship.city.name}</h2>
            <img src={relationship.city.image} />
        </div>
        <div className="continent-card">
            <h2>{relationship.continent.name}</h2>
            <img src={relationship.continent.image} />
        </div>
        </>
    )
}

export default Relationship
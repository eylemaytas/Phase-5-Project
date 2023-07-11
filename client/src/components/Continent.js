import React from "react";

function Continent({continent, continentFocusSelector}) {

    return(
        <div className="continent-card">
            <h2>{continent.name}</h2>
            <img onClick={continentFocusSelector} src={continent.image} alt={continent.id} />
        </div>
    )
}

export default Continent




// import React from "react";

// function Device({device, deviceFocusSelector}) {

//     return(
//         <div className="device-card">
//             <h2>{device.name}</h2>
//             <img onClick={deviceFocusSelector} src={device.image} alt={device.id} />
//             <p>{device.type}</p>
//         </div>
//     )
// }

// export default Device
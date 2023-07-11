import React from "react";

function FoodFocusCard({city}) {

    return(
        <div className="food-focus-card">
            <img src={city.image} alt="cityimage" />
            <p>{city.name}</p>
        </div>
    )
}

export default FoodFocusCard



// import React from "react";

// function DeveloperFocusCard({game}) {

//     return(
//         <div className="developer-focus-card">
//             <img src={game.image} alt="hi" />
//             <p>{game.name}</p>
//         </div>
//     )
// }

// export default DeveloperFocusCard
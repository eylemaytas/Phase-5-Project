import React from "react";

function Food({food, foodFocusSelector}) {

    return(
        <div className="food-card">
            <img onClick={foodFocusSelector} src={food.image} alt={food.id} />
            <h2>{food.name}</h2>
        </div>
    )
}

export default Food




// import React from "react";

// function Developer({developer, developerFocusSelector}) {

//     return(
//         <div className="developer-card">
//             <img onClick={developerFocusSelector} src={developer.logo} alt={developer.id} />
//             <h2>{developer.name}</h2>
//         </div>
//     )
// }

// export default Developer
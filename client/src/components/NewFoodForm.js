import React, { useState } from "react";

function NewFoodForm({ addFood, updateNewFood }) {
  const [formSubmitted, setFormSubmitted] = useState(false);

  return (
    <div className="food-form">
      <div className="food-card1">
        <h2>Add A New Food</h2>
        {formSubmitted ? (
          <h1>Added New Food To The List</h1>
        ) : (
          <form
            className="contact-form"
            onSubmit={(event) => {
              addFood(event);
              setFormSubmitted((formSubmitted) => !formSubmitted);
            }}
          >
            <div className="form-group">
              <label htmlFor="foodname">Food Name</label>
              <br />
              <input
                onChange={updateNewFood}
                type="text"
                id="name"
                name="foodname"
              ></input>
            </div>
            <div className="form-group">
              <label htmlFor="foodimage">Food Image</label>
              <br />
              <input
                onChange={updateNewFood}
                type="text"
                id="image"
                name="foodimage"
              ></input>
            </div>
            <div>
              <label htmlFor="description">Description</label>
              <br />
              <input
                onChange={updateNewFood}
                type="text"
                id="description"
                name="description"
              ></input>
            </div>
            <div className="form-group">
              <label htmlFor="citylanguage">Restaurant Recommendation</label>
              <br />
              <input
                onChange={updateNewFood}
                type="text"
                id="recom"
                name="restaurant"
              ></input>
            </div>
            <button type="submit">Add New Food</button>
          </form>
        )}
      </div>
    </div>
  );
}

export default NewFoodForm;











// import React, {useState} from "react";

// function NewFoodForm({addFood, updateNewFood}){

//     const [formSubmitted, setFormSubmitted] = useState(false)

//     return(
//         <div className="food-form">
//             <body className="food-card">
//                 <h2>Add A New Food</h2>
//                 {formSubmitted ? <h1>Added New Food To The List</h1> :
//                 <form className="contact-form" onSubmit={(event => {
//                     addFood(event)
//                     setFormSubmitted(formSubmitted => !formSubmitted)
//                 })}>
//                     <div className="form-group">
//                         <label htmlFor="foodname">Food Name</label><br></br>
//                         <input onChange={updateNewFood} type="text" id="name" name="foodname"></input>
//                     </div>
//                     <div className="form-group">
//                         <label htmlFor="foodimage">Food Image</label><br></br>
//                         <input onChange={updateNewFood} type="text" id="image" name="foodimage"></input>
//                     </div>
//                     <div>
//                         <label htmlFor="form-group">
//                             <label htmlFor="description">Description</label><br></br>
//                             <input onChange={updateNewFood} type="text" id="description" name="description"></input>
//                         </label>
//                     </div>
//                     <div className="form-group">
//                         <label htmlFor="citylanguage">Restaurant Recommendation</label><br></br>
//                         <input onChange={updateNewFood} type="text" id="recom" name="restaurant"></input>
//                     </div>
//                         <button type="submit">Add New Food</button>
//                 </form>}
//             </body>
//         </div>
//     )
// }

// export default NewFoodForm
// import React, {useState} from "react";

// function NewCityForm({addCity, updateFormData}){

//     const [formSubmitted, setFormSubmitted] = useState(false)

//     return(
//         <div className="city-form">
//             <div className="city-card">
              

//                 {formSubmitted ? <h1>Added New City To The Library</h1> :
//                 <form className="contact-form" onSubmit={(event => {
//                     addCity(event)
//                     setFormSubmitted(formSubmitted => !formSubmitted)
//                 })}>
//                     <div className="form-group">
//                         <label htmlFor="cityname">City Name</label><br></br>
//                         <input onChange={updateFormData} type="text" id="name" name="cityname"></input>
//                     </div>
//                     <div className="form-group">
//                         <label htmlFor="cityimage">City Image</label><br></br>
//                         <input onChange={updateFormData} type="text" id="image" name="cityimage"></input>
//                     </div>
//                     <div className="form-group">
//                         <label htmlFor="citylanguage">City Language</label><br></br>
//                         <input onChange={updateFormData} type="text" id="language" name="citylanguage"></input>
//                     </div>
//                     <div>
//                         <label htmlFor="form-group">
//                             <label htmlFor="description">Description</label><br></br>
//                             <input onChange={updateFormData} type="text" id="description" name="description"></input>
//                         </label>
//                     </div>
//                         <button type="submit">Add New City</button>
//                 </form>}
//             </div>
//         </div>
//     )
// }

// export default NewCityForm

// import React from "react";

// function NewCityForm({ addCity, updateFormData }) {
//   return (
//     <div className="city-form">
//       <h2>Add A New City</h2>
//       <form
//         className="contact-form"
//         onSubmit={(event) => {
//           addCity(event);
//         }}
//       >
//         <div className="form-group">
//           <div className="form-row">
//             <div className="form-column">
//               <label htmlFor="cityname">City Name</label>
//               <input
//                 onChange={updateFormData}
//                 type="text"
//                 id="name"
//                 name="cityname"
//               />
//             </div>
//             <div className="form-column">
//               <label htmlFor="cityimage">City Image</label>
//               <input
//                 onChange={updateFormData}
//                 type="text"
//                 id="image"
//                 name="cityimage"
//               />
//             </div>
//           </div>
//           <div className="form-row">
//             <div className="form-column">
//               <label htmlFor="citylanguage">City Language</label>
//               <input
//                 onChange={updateFormData}
//                 type="text"
//                 id="language"
//                 name="citylanguage"
//               />
//             </div>
//             <div className="form-column">
//               <label htmlFor="description">Description</label>
//               <input
//                 onChange={updateFormData}
//                 type="text"
//                 id="description"
//                 name="description"
//               />
//             </div>
//           </div>
//         </div>
//         <button type="submit">Add New City</button>
//       </form>
//     </div>
//   );
// }

// export default NewCityForm;


import React, { useState } from "react";

function NewCityForm({ addCity, updateFormData }) {
  const [isCityAdded, setIsCityAdded] = useState(false);

  const handleFormSubmit = (event) => {
    event.preventDefault();
    addCity(event);
    setIsCityAdded(true);
  };

  return (
    <div className="city-form">
      {isCityAdded ? (
        <h2>Thank you for adding a new city!♥</h2>
      ) : (
        <h2>Add A New City</h2>
      )}
      <form className="contact-form" onSubmit={handleFormSubmit}>
        <div className="form-group">
          <div className="form-row">
            <div className="form-column">
              <label htmlFor="cityname">City Name</label>
              <input
                onChange={updateFormData}
                type="text"
                id="name"
                name="cityname"
              />
            </div>
            <div className="form-column">
              <label htmlFor="cityimage">City Image</label>
              <input
                onChange={updateFormData}
                type="text"
                id="image"
                name="cityimage"
              />
            </div>
          </div>
          <div className="form-row">
            <div className="form-column">
              <label htmlFor="citylanguage">City Language</label>
              <input
                onChange={updateFormData}
                type="text"
                id="language"
                name="citylanguage"
              />
            </div>
            <div className="form-column">
              <label htmlFor="description">Description</label>
              <input
                onChange={updateFormData}
                type="text"
                id="description"
                name="description"
              />
            </div>
          </div>
        </div>
        <button type="submit">Add New City</button>
      </form>
    </div>
  );
}

export default NewCityForm;

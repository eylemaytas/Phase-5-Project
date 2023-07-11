import React, {useState} from "react";

function NewFoodForm({addFood, updateFormData}){

    const [formSubmitted, setFormSubmitted] = useState(false)

    return(
        <div className="food-form">
            <body className="food-card">
                <h2>Add A New Food</h2>
                {formSubmitted ? <h1>Added New Food To The List</h1> :
                <form className="contact-form" onSubmit={(event => {
                    addFood(event)
                    setFormSubmitted(formSubmitted => !formSubmitted)
                })}>
                    <div className="form-group">
                        <label for="foodname">Food Name</label><br></br>
                        <input onChange={updateFormData} type="text" id="name" name="foodname"></input>
                    </div>
                    <div className="form-group">
                        <label for="foodimage">Food Image</label><br></br>
                        <input onChange={updateFormData} type="text" id="image" name="foodimage"></input>
                    </div>
                    <div>
                        <label for="form-group">
                            <label for="description">Description</label><br></br>
                            <input onChange={updateFormData} type="text" id="description" name="description"></input>
                        </label>
                    </div>
                    <div className="form-group">
                        <label for="citylanguage">Restaurant Recommendation</label><br></br>
                        <input onChange={updateFormData} type="text" id="recom" name="restaurant"></input>
                    </div>
                        <button type="submit">Add New Food</button>
                </form>}
            </body>
        </div>
    )
}

export default NewFoodForm
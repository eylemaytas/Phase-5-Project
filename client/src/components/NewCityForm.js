import React, {useState} from "react";

function NewCityForm({addCity, updateFormData}){

    const [formSubmitted, setFormSubmitted] = useState(false)

    return(
        <div className="city-form">
            <body className="city-card">
                <h2>Add A New City</h2>
                {formSubmitted ? <h1>Added New City To The Library</h1> :
                <form className="contact-form" onSubmit={(event => {
                    addCity(event)
                    setFormSubmitted(formSubmitted => !formSubmitted)
                })}>
                    <div className="form-group">
                        <label htmlFor="cityname">City Name</label><br></br>
                        <input onChange={updateFormData} type="text" id="name" name="cityname"></input>
                    </div>
                    <div className="form-group">
                        <label htmlFor="cityimage">City Image</label><br></br>
                        <input onChange={updateFormData} type="text" id="image" name="cityimage"></input>
                    </div>
                    <div className="form-group">
                        <label htmlFor="citylanguage">City Language</label><br></br>
                        <input onChange={updateFormData} type="text" id="language" name="citylanguage"></input>
                    </div>
                    <div>
                        <label htmlFor="form-group">
                            <label htmlFor="description">Description</label><br></br>
                            <input onChange={updateFormData} type="text" id="description" name="description"></input>
                        </label>
                    </div>
                        <button type="submit">Add New City</button>
                </form>}
            </body>
        </div>
    )
}

export default NewCityForm
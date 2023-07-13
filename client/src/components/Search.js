import React from "react";

function Search({setSearchText}) {



    return(
        <div className="user-input">
            <label htmlFor="search">Search Cities:</label>
            <input
                className="form"
                type="text"
                id="search"
                placeholder="Search Cities..."
                onChange={(event) => {
                    setSearchText(event.target.value)
                }}
            />

        </div>
    )
}

export default Search
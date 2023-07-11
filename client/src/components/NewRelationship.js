import React from "react";

function NewRelationship({updateNewRelationship, addRelationship}) {

    return(
        <div className="user-input">
            <h2>New Relationship</h2>
            <form>
                <input onChange={updateNewRelationship} type="number" name="game_id" placeholder="City ID"/>
                <input onChange={updateNewRelationship} type="number" name="device_id" placeholder="Continent ID"/>
                <button onClick={addRelationship} className="login-button">Submit Relationship</button>
            </form>
        </div>
    )
}

export default NewRelationship
import React from "react";
import Developer from "./Developer";

function DeveloperList({developers, developerFocusSelector}) {

    const developer = developers.map(developer => {
        return <Developer developer={developer} developerFocusSelector={developerFocusSelector}/>
    })
    return(
        <div className="developer-grid">
            {developer}
        </div>
    )
}

export default DeveloperList
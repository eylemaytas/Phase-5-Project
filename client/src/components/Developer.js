import React from "react";

function Developer({developer, developerFocusSelector}) {

    return(
        <div className="developer-card">
            <img onClick={developerFocusSelector} src={developer.logo} alt={developer.id} />
            <h2>{developer.name}</h2>
        </div>
    )
}

export default Developer
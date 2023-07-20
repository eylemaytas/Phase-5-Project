import React from "react";

function Header({logoClick}) {

    return(
        <div className="logo">
            <img onClick={logoClick} src="/assets/travel.png" alt="Hi"/>
        </div>
    )
}

export default Header
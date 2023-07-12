import React from "react";

// function Homepage({belongsFocusSelector}) {
function Homepage(continentFocusSelector={continentFocusSelector}) {

    return(
        <div className="home-content">
            <div className="home1">
                <img onClick={continentFocusSelector} src="/assets/nintendo-logo.png" alt="Nintendo"/>
            </div>
            <div className="home1">
                {/* <img onClick={belongsFocusSelector} src="/assets/sony-logo.png" alt="Sony"/>
                <img onClick={belongsFocusSelector} src="/assets/microsoft-logo.png" alt="Microsoft"/> */}
            </div>
        </div>
    )
}

export default Homepage



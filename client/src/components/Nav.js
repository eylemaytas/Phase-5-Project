import React from "react";
import { NavLink } from "react-router-dom";

function Nav() {

    return(
        <div className="nav-bar">
            
            <NavLink to='/continents'>HOME</NavLink>
            <NavLink to='/cities'>CITIES</NavLink>
            <NavLink to='/foods'>FOODS</NavLink>
            <NavLink to='/blogs'>BLOG</NavLink>
            <NavLink to='/login'>LOGIN</NavLink>
            <NavLink to='/signup'>SIGNUP</NavLink>
        </div>
    )
}

export default Nav


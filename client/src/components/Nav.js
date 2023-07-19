// import React from "react";
// import { NavLink } from "react-router-dom";

// function Nav() {

//     return(
//         <div className="nav-bar">
            
//             <NavLink to='/continents'>HOME</NavLink>
//             <NavLink to='/cities'>CITIES</NavLink>
//             <NavLink to='/foods'>FOODS</NavLink>
//             <NavLink to='/blogs'>BLOG</NavLink>
//             <NavLink to="/add-blog">ADD BLOG</NavLink>
//             <NavLink to="/add-food">ADD FOOD</NavLink>
//             <NavLink to="/add-city">ADD CITY</NavLink>
//             <NavLink to='/login'>LOGIN</NavLink>
//             <NavLink to='/signup'>SIGNUP</NavLink>

//         </div>
//     )
// }

// export default Nav


// Nav.js
import React from "react";
import { NavLink } from "react-router-dom";

function Nav({ currentUser, logout }) {
  return (
    <div className="nav-bar">
      <NavLink to="/continents">HOME</NavLink>
      <NavLink to="/cities">CITIES</NavLink>
      <NavLink to="/foods">FOODS</NavLink>
      <NavLink to="/blogs">BLOG</NavLink>
      {currentUser && ( 
        <>
          <NavLink to="/add-blog">ADD BLOG</NavLink>
          <NavLink to="/add-food">ADD FOOD</NavLink>
          <NavLink to="/add-city">ADD CITY</NavLink>
          <button onClick={logout}>LOGOUT</button>
        </>
      )}
      {!currentUser && ( 
        <>
          <NavLink to="/login">LOGIN</NavLink>
          <NavLink to="/signup">SIGNUP</NavLink>
        </>
      )}
    </div>
  );
}

export default Nav;


// import React from "react";
// import { NavLink } from "react-router-dom";

// function Nav({ isLoggedIn, logout }) {
//   return (
//     <div className="nav-bar">
//       <NavLink to="/continents">HOME</NavLink>
//       <NavLink to="/cities">CITIES</NavLink>
//       <NavLink to="/foods">FOODS</NavLink>
//       <NavLink to="/blogs">BLOG</NavLink>
//       <NavLink to="add-blog">ADD BLOG</NavLink>
//       {isLoggedIn && (
//         <>
//           <button onClick={() => logout()}>Logout</button>
//         </>
//       )}
//       {!isLoggedIn && (
//         <>
//           <NavLink to="/login">LOGIN</NavLink>
//           <NavLink to="/signup">SIGNUP</NavLink>
//         </>
//       )}
//     </div>
//   );
// }

// export default Nav;


import React from "react";

function Login() {
    
    return(
        <div className="user-input">
            <h2>Login/Signup</h2>
            <form>
                <input type="text" name="username" placeholder="Username"/>
                <input type="text" name="password" placeholder="Password"/>
                <button className="login-button">Login/Signup</button>
            </form>
        </div>
    )
}

export default Login
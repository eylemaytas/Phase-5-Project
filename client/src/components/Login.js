import { useState } from 'react'

function Login({attemptLogin}) {

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const handleChangeUsername = e => setUsername(e.target.value)
  const handleChangePassword = e => setPassword(e.target.value)

  function handleSubmit(e) {
    e.preventDefault()
    attemptLogin({username, password})
  }

  return (
    <form onSubmit={handleSubmit} className="login-form">

      <input type="text"
      onChange={handleChangeUsername}
      value={username}
      placeholder='username'
      />

      <input type="text"
      onChange={handleChangePassword}
      value={password}
      placeholder='password'
      />

      <input type="submit"
      value='Login'
      />

    </form>
  )

}

export default Login














// import React from "react";

// function Login() {
    
//     return(
//         <div className="user-input">
//             <h2>Login/Signup</h2>
//             <form>
//                 <input type="text" name="username" placeholder="Username"/>
//                 <input type="text" name="password" placeholder="Password"/>
//                 <button className="login-button">Login/Signup</button>
//             </form>
//         </div>
//     )
// }

// export default Login
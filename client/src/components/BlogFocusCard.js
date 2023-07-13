import React from "react";

function BlogFocusCard({user}) {

    return(
        <div className="blog-focus-card">
            <p>{user.username}</p> 
        </div>
    )
}

export default BlogFocusCard
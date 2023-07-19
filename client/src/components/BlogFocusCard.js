import React from "react";

function BlogFocusCard({user}) {

    return(
        <div className="blog-focus-card">
            <p>Shared by:{user.username}.</p> 
        </div>
    )
}

export default BlogFocusCard
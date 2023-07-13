import React from "react";
import Blog from "./Blog";

function BlogList({blogs, blogFocusSelector}) {

    const blog = blogs.map(blog => {
        return <Blog key={blog.id} blog={blog} blogFocusSelector={blogFocusSelector}/>
    })
    return(
        <div className="blog-grid">
            {blog}
        </div>
    )
}

export default BlogList
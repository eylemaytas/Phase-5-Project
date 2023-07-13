import React from "react";

function Blog({blog, blogFocusSelector}) {

    return(
        <div className="blog-card">
            <img onClick={blogFocusSelector} src={blog.image} alt={blog.id} />
            <p>{blog.like_count} people liked.</p>
            <h2>{blog.title}</h2>
            <p>{blog.blog_post}</p>
        </div>
    )
}

export default Blog
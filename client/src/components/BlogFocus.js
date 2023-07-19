import React, { useEffect, useState } from "react";
import BlogFocusCard from "./BlogFocusCard";

function BlogFocus({focusBlog}) {

    const [selectedBlog, setSelectedBlog] = useState([])
    
    useEffect(() => {
        fetch(`http://127.0.0.1:7001/blogs/${focusBlog}`)
        .then(res => res.json())
        .then(selectedBlog => setSelectedBlog(selectedBlog))
      }, [focusBlog])

    if(!selectedBlog.users){
        return(
            <h1>Loading...</h1>
        )
    }

    const focusCard = selectedBlog.users.map(user => {
        return <BlogFocusCard key={user.id} user={user} />
    })

    return(
        <div className="blog-focus-page">
            <h2>{selectedBlog.title}</h2>
            <img src={selectedBlog.image} alt="blog" />
            <p>{selectedBlog.like_count} people liked.</p>
            <p>{selectedBlog.blog_post}</p>
            {focusCard}
        </div>
    )
}

export default BlogFocus
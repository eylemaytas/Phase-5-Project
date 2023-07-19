// import React from "react";

// function Blog({blog, blogFocusSelector}) {

//     return(
//         <div className="blog-card">
//             <img onClick={blogFocusSelector} src={blog.image} alt={blog.id} />
//             <p>{blog.like_count} people liked.</p>
//             <h2>{blog.title}</h2>
//             <p>{blog.blog_post}</p>
//         </div>
//     )
// }

// export default Blog




import React, { useState } from "react";

function Blog({ blog, likeBlog,blogFocusSelector }) {
  const [liked, setLiked] = useState(false);

  const handleLike = () => {
    if (!liked) {
      likeBlog(blog.id);
      setLiked(true);
    }
  };

  return (
    <div className="blog-card">
      <h2>{blog.title}</h2>
      <img onClick={blogFocusSelector} src={blog.image} alt={blog.id} />
      <button onClick={handleLike} disabled={liked}>
          {liked ? "Liked ❤️" : "Like 👍"}
        </button>
      <p>{blog.like_count} likes</p>
      <div className="like-button">
        
      </div>
    </div>
  );
}

export default Blog;


// import React from "react";
// import Blog from "./Blog";

// function BlogList({blogs, blogFocusSelector}) {

//     const blog = blogs.map(blog => {
//         return <Blog key={blog.id} blog={blog} blogFocusSelector={blogFocusSelector}/>
//     })
//     return(
//         <div className="blog-grid">
//             {blog}
//         </div>
//     )
// }

// export default BlogList



import React from "react";
import Blog from "./Blog";

function BlogList({ blogs, likeBlog, blogFocusSelector }) {
  return (
    <div className="blog-grid">
      {blogs.map((blog) => (
        <Blog key={blog.id} blog={blog} likeBlog={likeBlog} blogFocusSelector={blogFocusSelector} />
      ))}
    </div>
  );
}

export default BlogList;




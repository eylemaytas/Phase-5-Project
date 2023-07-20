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




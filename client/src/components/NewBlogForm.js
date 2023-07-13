import React, {useState} from "react";

function NewBlogForm({addBlog, updateNewBlog}){

    const [formSubmitted, setFormSubmitted] = useState(false)

    return(
        <div className="blog-form">
            <body className="blog-card">
                <h2>Add A New Blog</h2>
                {formSubmitted ? <h1>Your blog post has successfully added!</h1> :
                <form className="contact-form" onSubmit={(event => {
                    addBlog(event)
                    setFormSubmitted(formSubmitted => !formSubmitted)
                })}>
                    <div className="form-group">
                        <label htmlFor="blogtitle">Blog Title</label><br></br>
                        <input onChange={updateNewBlog} type="text" id="name" name="blogtitle"></input>
                    </div>
                    <div className="form-group">
                        <label htmlFor="blogimage">Blog Image</label><br></br>
                        <input onChange={updateNewBlog} type="text" id="image" name="blogimage"></input>
                    </div>
                    <div>
                        <label htmlFor="form-group">
                            <label htmlFor="blogpost">Blog Post</label><br></br>
                            <input onChange={updateNewBlog} type="text" id="blog_post" name="blogpost"></input>
                        </label>
                    </div>
                        <button type="submit">Add New Blog Post</button>
                </form>}
            </body>
        </div>
    )
}

export default NewBlogForm
import React, {useState} from "react";

function NewBlogForm({addBlog, updateNewBlog}){

    const [formSubmitted, setFormSubmitted] = useState(false)

    return(
        <div className="blog-form">
            <body className="blog-card1">
                <h2>Add A New Blog Post</h2>
                {formSubmitted ? <h1>Thank you for adding a new blog post!♥</h1> :
                <form className="contact-form1" onSubmit={(event => {
                    addBlog(event)
                    setFormSubmitted(formSubmitted => !formSubmitted)
                })}>
                    <div className="form-group1">
                        <label htmlFor="blogtitle">Blog Title</label><br></br>
                        <input onChange={updateNewBlog} type="text" id="name" name="blogtitle"></input>
                    </div>
                    <div className="form-group1">
                        <label htmlFor="blogimage">Blog Image</label><br></br>
                        <input onChange={updateNewBlog} type="text" id="image" name="blogimage"></input>
                    </div>
                    <div className="form-group1">
                        <label htmlFor="blogpost">Blog Post</label><br></br>
                        <input onChange={updateNewBlog} type="text" id="blog_post" name="blogpost"></input>
                        
                    </div>
                        <button type="submitt">Add New Blog Post</button>
                </form>}
            </body>
        </div>
    )
}

export default NewBlogForm
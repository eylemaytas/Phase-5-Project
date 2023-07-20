import '../App.css';
import {useState, useEffect} from 'react'
import { Route, Switch, useHistory } from "react-router-dom"

import Login from './Login';
import Signup from './Signup';
import UserDetails from './UserDetails';
import Homepage from './Homepage';
import Header from './Header'
import ContinentList from './ContinentList';
import CityList from './CityList';
import FoodList from './FoodList';
import Nav from './Nav';
import ContinentFocus from './ContinentFocus';
import FoodFocus from './FoodFocus';
import CityFocus from './CityFocus';
import Search from './Search';
import NewCityForm from './NewCityForm';
import NewFoodForm from './NewFoodForm';
import BlogList from './BlogList';
import BlogFocus from './BlogFocus';
import NewBlogForm from './NewBlogForm';


function App() {

  const history = useHistory()

  const [continents, setContinents] = useState([])
  const [cities, setCities] = useState([])
  const [foods, setFoods] = useState([])
  const [newFood,setNewFood] = useState({
    name:"Oreo",
    image:"https://i.ebayimg.com/images/g/W9UAAOSw3K1cS4iu/s-l1600.jpg",
    description: "Best thing ever",
    restaurant_recommendation: "A La Lopez",
    city_id: 1
  })
  const [focusContinents, setFocusContinents] = useState('')
  const [focusFood, setFocusFood] = useState('')
  const [focusCity, setFocusCity] = useState('')
  const [formData, setFormData] = useState({
    name:"Brugge",
    image:"https://media.timeout.com/images/105975972/1920/1080/image.jpg",
    language:"Flemish",
    description: "too good to be true!"
  })
  const [searchText, setSearchText] = useState('')
  const [blogs, setBlogs] = useState([])
  const [focusBlog, setFocusBlog] = useState('')
  const [newBlog, setNewBlog] = useState({
    title: "A Day in Athens",
    image:"https://static.independent.co.uk/s3fs-public/thumbnails/image/2021/06/02/20/istock-833264986.jpg?quality=75&width=990&crop=4%3A3%2Csmart&auto=webp",
    blog_post: "Very nice city.",
    like_count: 10,
    user_id: 1
  })

  const [currentUser, setCurrentUser] = useState(null) 
  
  useEffect(() => {
    fetch('/current_session')
    .then(res => {
      if (res.ok) {
        res.json()
        .then(user => setCurrentUser(user))
      }
    })
  }, [])

  function attemptLogin(userInfo) {
    fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accepts': 'application/json'
      },
      body: JSON.stringify(userInfo)
    })
    .then(res => {
      if (res.ok) {
        res.json()
        .then(user => setCurrentUser(user))
      }
    })
  }
  
  function attemptSignup(userInfo) {
    fetch('/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accepts': 'application/json'
      },
      body: JSON.stringify(userInfo)
    })
    .then(res => {
      if (res.ok) {
        res.json()
        .then(user => setCurrentUser(user))
      }
    })
  }

  function logout() {
    setCurrentUser(null)
    fetch('/logout', { method: 'DELETE' })
  }

  const likeBlog = (blogId) => {
    setBlogs((prevBlogs) =>
      prevBlogs.map((blog) =>
        blog.id === blogId ? { ...blog, like_count: blog.like_count + 1 } : blog
      )
    );
  }

  function addCity(event){
    event.preventDefault()

    fetch("http://localhost:7001/cities", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(newCity => setCities([...cities, newCity]))
  }

  useEffect(() => {
    fetch('http://127.0.0.1:7001/continents')
    .then(res => res.json())
    .then(continentData => setContinents(continentData))
  }, [])

  useEffect(() => {
    fetch('http://127.0.0.1:7001/cities')
    .then(res => res.json())
    .then(cityData => setCities(cityData))
  }, [])

  useEffect(() => {
    fetch('http://127.0.0.1:7001/foods')
    .then(res => res.json())
    .then(foodData => setFoods(foodData))
  }, [])

  useEffect(() => {
    fetch('http://127.0.0.1:7001/blogs')
    .then(res => res.json())
    .then(blogData => setBlogs(blogData))
  }, [])



  function continentFocusSelector(event) {
    setFocusContinents(event.target.alt)
    history.push('/continentfocus')
  }

  function foodFocusSelector(event) {
    setFocusFood(event.target.alt)
    history.push('/foodfocus')
  }

  function cityFocusSelector(event) {
    setFocusCity(event.target.alt)
    history.push('/cityfocus')
  }

  function blogFocusSelector(event) {
    setFocusBlog(event.target.alt)
    history.push('/blogfocus')
  }

  function logoClick() {
    history.push('/home')
  }

  function updateFormData(event) {
    setFormData({...formData, [event.target.id]: event.target.value})
  }

  function updateNewFood(event) {
    setNewFood({...newFood, [event.target.id]: event.target.value})
  }

  function updateNewBlog(event) {
    setNewBlog({...newBlog, [event.target.id]: event.target.value})
  }

  const filteredCities = cities.filter(city => {
    if(searchText === "") {
      return true
    }
    return city.name.toUpperCase().includes(searchText.toUpperCase())
  })

  function addFood(event){
    event.preventDefault()

    fetch("http://localhost:7001/foods", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(newFood)
    })
    .then(response => response.json())
    .then(newFoodd => setFoods([...foods, newFoodd]))
  }


  function addBlog(event){
    event.preventDefault()

    fetch("http://localhost:7001/blogs", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(newBlog)
    })
    .then(response => response.json())
    .then(newBlogg => setBlogs([...blogs, newBlogg]))
  }
  return (
    <div className="app">
      <div className='header'>
      <Header logoClick={logoClick}/>
        <Nav currentUser={currentUser} logout={logout} setCurrentUser={setCurrentUser} />
      </div>
      <Switch>
        <Route exact path="/home">
          {/* <Homepage continentFocusSelector={continentFocusSelector}/> */}
          <ContinentList continentFocusSelector={continentFocusSelector} continents={continents}/>
        </Route>
        <Route exact path="/continents">
          <ContinentList continentFocusSelector={continentFocusSelector} continents={continents}/>
        </Route>
        <Route exact path="/cities">
          <Search setSearchText={setSearchText}  />
          <CityList cities={filteredCities} cityFocusSelector={cityFocusSelector} />
        </Route>
        <Route exact path="/foods">
          <FoodList foods={foods} foodFocusSelector={foodFocusSelector} />
        </Route>
        <Route exact path="/blogs">
          <BlogList  blogs={blogs} blogFocusSelector={blogFocusSelector} likeBlog={likeBlog}/>
        </Route>
        <Route exact path="/continentfocus">
          <ContinentFocus focusContinent={focusContinents} />
        </Route>
        <Route exact path="/foodfocus">
          <FoodFocus focusFood={focusFood} />
        </Route>
        <Route exact path="/cityfocus">
          <CityFocus focusCity={focusCity}/>
        </Route>
        <Route exact path="/blogfocus">
          <BlogFocus focusBlog={focusBlog} />
        </Route> 
        <Route exact path="/add-blog">
          {currentUser && <NewBlogForm updateNewBlog={updateNewBlog} addBlog={addBlog}/>}
        </Route>
        <Route exact path="/add-food">
          {currentUser && <NewFoodForm updateNewFood={updateNewFood} addFood={addFood}/>}
        </Route>
        <Route exact path="/add-city">
          {currentUser && <NewCityForm  updateFormData={updateFormData} addCity={addCity}/>}
        </Route>
        <Route exact path="/login">
          { !currentUser ? <Login attemptLogin={attemptLogin} /> : null }
          { currentUser ? <UserDetails currentUser={currentUser} logout={logout} /> : null }
        </Route>
        <Route exact path="/signup">
          { !currentUser ? <Signup attemptSignup={attemptSignup} /> : null }
          
        </Route>
      </Switch>
    </div>
  );
}

export default App;
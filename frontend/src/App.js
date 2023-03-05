import './App.css';
import { Routes, Route, Link } from "react-router-dom";
import Nav from "./components/Nav";
import Home from './pages/Home';

// import SocialFollow from "./components/SocialFollow";

function App() {
  return (
    <div className="App">
      <div className="">
      <header className="">
      <logo className="nav-items">
          <Link to="/"><img src={require('./logo.png')} className="logo" alt="logo" /></Link>
      </logo>

{/*
        <form className="d-flex col-lg-3">
          <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search" onSearch={(e)=>setQuery(e.currentTarget.value)}/>
          <button className="btn btn-outline-info" type="submit" onClick={()=>SearchMe(query)}>Search</button>
        </form> */}

        <div className="col-lg-6">

        </div>

        <div className="navbar navbar-expand-lg" style={{ backgroundColor: '#4B0082', color: 'white'}}>
          <Nav/>
        </div>

        {/* <div className="socials nav-items col-lg-3">
          <SocialFollow />
        </div> */}

      </header>

      </div>
      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
        </div>
        <footer>
        {/* <Footer/> */}
        </footer>
    </div>
  );
}

export default App;

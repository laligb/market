import React,  { Component} from 'react'
import { Link, useNavigate} from 'react-router-dom'
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import {useParams} from 'react-router-dom'


function Nav() {
    const navigate=useNavigate()
    const Logout=()=>{
        localStorage.removeItem('auth')
        navigate('/login')

        const {id}=useParams();
    }
    return (
      <>

    <div className='container-fluid'>
              <ul>
                <li class="navigator"><a href="{% url 'index' %}">Home</a></li>
                <li class="navigator"><a href="{% url 'product-list' %}">Products</a></li>
                <li class="navigator"><a href="{% url 'customer-list' %}">Customers</a></li>
              </ul>
          </div>
      <nav className="nav-items">


        <DropdownButton
          as={ButtonGroup}
          key='Info'
          id="dropdown-variants-Info"
          title="👨"
          variant="Info"
        >
        { localStorage.getItem('auth')!=null?
          (

            <Dropdown.Item eventKey="1"><Link to="/" onClick={Logout}>Logout</Link></Dropdown.Item>

          ):
            <Dropdown.Item eventKey="1"> <Link to="/login">Login</Link></Dropdown.Item>
        }
        {/* <Dropdown.Item eventKey="2"> <Link to="/users/:id">Profile</Link></Dropdown.Item> */}
        <Dropdown.Item eventKey="3"> <Link to="/posts">Posts</Link></Dropdown.Item>
        <Dropdown.Item eventKey="4"><Link to="/users">Users</Link></Dropdown.Item>

        </DropdownButton>
      </nav>


          </>

        )
  }


export default Nav;

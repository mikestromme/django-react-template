import { useState } from 'react'
import './App.css'
import {Routes, Route} from 'react-router-dom'
import Home from './components/Home';
import About from './components/About';
import Create from './components/Create';
import Timekeeping from './components/Timekeeping';
import NavBar from './components/NavBar';


function App() {
  const [count, setCount] = useState(0)
  const myWidth = 220
  return (
    <div className='App'>
      <NavBar drawerWidth={myWidth} 
      content = {
      
          <Routes>
            <Route path="" element={<Home/>}/>
            <Route path="/about" element={<About/>}/>
            <Route path="/create" element={<Create/>}/>
            <Route path="/timekeeping" element={<Timekeeping/>}/>
          </Routes>

        }
      />


    </div>
  );
}

export default App

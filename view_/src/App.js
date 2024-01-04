import React from 'react';
import './App.css';
import { Header } from './Components/Header/Header.js';
import {
  BrowserRouter,
  Routes,
  Route
} from 'react-router-dom';
import { Contact } from "./Components/Contact/Contact.js";
import { Home } from "./Components/Home/Home.js";
import { UserProfile } from './Components/UserProfile/UserProfile.js';

function App() {

  return (
    <>
      <BrowserRouter >
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Contact" element={<Contact />} />
          <Route path="/Profile" element={<UserProfile />} />
        </Routes>
      </BrowserRouter >
    </>

  );
}

export default App;
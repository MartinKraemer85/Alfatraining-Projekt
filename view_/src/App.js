import React from 'react';
import './App.css';
import { Footer } from './Components/Footer/Footer.js';
import { Filter } from './Components/Filter/Filter.js';
import { Header } from './Components/Header/Header.js';
import { Article } from './Components/Article/Article.js';
function App() {

  return (
    <>
      <Header />

      <Filter />
      <div className='Container'>
        <Article />
      </div>

      <Footer />
    </>

  );
}

export default App;
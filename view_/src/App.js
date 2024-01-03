import React, { useState, useEffect } from 'react';
import './App.css';
import { Footer } from './Components/Footer/Footer.js';
import { Filter } from './Components/Filter/Filter.js';
import { Header } from './Components/Header/Header.js';
import { Article } from './Components/Article/Article.js';
import { post } from './helper/CRUD.js'

function App() {
  const [genre, setGenre] = useState([]);
  const [subGenre, setSubGenre] = useState([]);
  const [filterList, setFilterList] = useState([])

  useEffect(() => {
    post({
      url: "/select",
      body: {
        "table": "genre",
        "fields": ["name", "0 as 'isChecked'"]
      }
    }).then(res => res.json()
    ).then(data => {
      setGenre(data)
    })

  }, []);


  useEffect(() => {
    post({
      url: "/select",
      body: {
        "table": "sub_genre",
        "fields": ["name", "0 as 'isChecked'"]
      }
    }).then(res => res.json()
    ).then(data => {
      setSubGenre(data)
    })

  }, []);

  return (
    <>
      <Header />
      <Filter genre={genre} subGenre={subGenre} filterList={filterList} setFilterList={setFilterList} />

      <Article filterList={filterList} />


      <Footer />
    </>

  );
}

export default App;
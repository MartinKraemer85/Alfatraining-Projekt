import React, { Fragment } from 'react';
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
import { AddArticle } from './Components/Article/AddArticle/AddArticle.js';
import { GenreContextProvider } from './contexts/genre.js';
import { ArticleOverview } from './Components/ArticleOverview/ArticleOverview.js';
import { Footer } from "./Components/Footer/Footer.js";

function App() {

  return (
    <>
      <BrowserRouter >
        <Header />
        <Routes>
          <Route path="/" element={
            <GenreContextProvider>
              <Home />
            </GenreContextProvider>} />
          <Route path="/Contact" element={<Contact />} />
          <Route path="/Profile" element={<UserProfile />} />
          <Route path="/AddArticle" element={
            <GenreContextProvider>
              <AddArticle />
            </GenreContextProvider>} />
          <Route path="/Article" element={<ArticleOverview />} />
        </Routes>
        <Footer />
      </BrowserRouter >
    </>

  );
}

export default App;
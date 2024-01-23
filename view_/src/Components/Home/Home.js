import React, { useState, useContext } from 'react';
import { Filter } from "../Filter/Filter.js";
import { Article } from "../Article/Article.js";
import { Footer } from "../Footer/Footer.js"
import { GenreContext } from '../../contexts/genre.js';

export function Home() {
    const { genre, subGenre } = useContext(GenreContext)
    const [filterList, setFilterList] = useState([])

    return (
        <>
            <Filter genre={genre} subGenre={subGenre} filterList={filterList} setFilterList={setFilterList} />
            <Article filterList={filterList} />
            <Footer />
        </>
    )
}

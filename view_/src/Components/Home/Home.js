import React, { useContext } from 'react';
import { Filter } from "../Filter/Filter.js";
import { Article } from "../Article/Article.js";
import { GenreContext } from '../../contexts/genre.js';
import { useArticle } from '../../Hooks/useArticle.js';

export function Home() {
    const { genre, subGenre } = useContext(GenreContext)
    const { articles, filterList, setFilterList } = useArticle()

    return (
        <>
            <Filter genre={genre} subGenre={subGenre} filterList={filterList} setFilterList={setFilterList} />
            <Article articles={articles} />
        </>
    )
}

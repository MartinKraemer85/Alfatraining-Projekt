import React, { useContext } from 'react';
import { Filter } from "../Filter/Filter.js";
import { Article } from "../Article/Article.js";
import { GenreContext } from '../../contexts/GenreList.js';
import { useArticle } from '../../Hooks/useArticle.js';
import "./Home.css"

export function Home() {
    const { genre, subGenre } = useContext(GenreContext)
    const { articles, filterList, setFilterList } = useArticle()

    return (
        <>
            <Filter genre={genre} subGenre={subGenre} filterList={filterList} setFilterList={setFilterList} />
            <div className='articleWrapper'>
                <Article articles={articles} />
            </div>
        </>
    )
}

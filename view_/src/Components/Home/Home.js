import React, { useState, useEffect } from 'react';
import { Filter } from "../Filter/Filter.js";
import { Article } from "../Article/Article.js";
import { Footer } from "../Footer/Footer.js"
import { post } from '../../helper/CRUD.js';

const Home = () => {
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
            <Filter genre={genre} subGenre={subGenre} filterList={filterList} setFilterList={setFilterList} />
            <Article filterList={filterList} />
            <Footer />
        </>
    )
}

export { Home }
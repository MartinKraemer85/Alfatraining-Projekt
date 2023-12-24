import React, { useState, useEffect } from 'react';
import { post } from '../../helper/CRUD.js';
import './Filter.css'

const Filter = () => {
    const [genre, setGenre] = useState([]);

    useEffect(() => {
        post({
            url: "/select",
            body: {
                "table": "genre",
                "fields": ["name"]
            }
        }).then(res => res.json()
        ).then(data => {
            setGenre(data)
        })

    }, []);

    const [subGenre, setSubGenre] = useState([]);

    useEffect(() => {
        post({
            url: "/select",
            body: {
                "table": "sub_genre",
                "fields": ["name"]
            }
        }).then(res => res.json()
        ).then(data => {
            setSubGenre(data)
        })

    }, []);

    const createList = (data) => data.map((genre, index) => <li key={index}>{genre.name}</li>)


    return (
        <div className="Filter">
            <h2>Genre </h2>
            {createList(genre)}
            <h2>Sub Genre </h2>
            {createList(subGenre)}
        </div>
    )

}

export { Filter }
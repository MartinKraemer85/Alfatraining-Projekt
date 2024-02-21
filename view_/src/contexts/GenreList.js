import React, { createContext, useState, useEffect } from 'react'
import { post } from '../helper/CRUD';
export const GenreContext = createContext()

export function GenreContextProvider(props) {
    const [genre, setGenre] = useState([]);
    const [subGenre, setSubGenre] = useState([]);

    useEffect(() => {
        post({
            url: "/select",
            body: {
                "table": "genre",
                "fields": ["id", "name", "0 as 'isChecked'"]
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
                "fields": ["id", "name", "0 as 'isChecked'"]
            }
        }).then(res => res.json()
        ).then(data => {
            setSubGenre(data)
        })

    }, []);

    return (
        <GenreContext.Provider
            value={{
                genre,
                subGenre
            }}>
            {props.children}
        </GenreContext.Provider>
    )
}

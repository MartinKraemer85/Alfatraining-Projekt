import { useState, useEffect } from 'react';
import { post } from '../helper/CRUD.js';

export function useArticle() {
    const [articles, setArticle] = useState([])
    const [filterList, setFilterList] = useState([])

    useEffect(() => {
        post({
            url: "/select_all_articles",
            body: {
                "initial": true,
                "where": createWhere()
            }
        }).then(res => res.json()
        ).then(data => {
            setArticle(data)
        })
        // createWhere is a dependency because of the use of filter, but it's not really a dependency
        //  Line 47:8:  React Hook useEffect has a missing dependency: 'createWhere'. Either include it or remove the dependency array 
        // this line prevents the warning message (since the function doesn't make sense in the dependency array):
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [filterList]);

    function createWhere() {
        let where = ""
        // create the where clause, genre_1 / sub_genre_1 is because of the way sqlalchemie builds joined querys
        filterList.forEach((genre) => where ? where += ` AND (genre_1.name = '${genre.name}' OR sub_genre_1.name = '${genre.name}')` :
            // first iteration (without AND)    
            where += ` (genre_1.name = '${genre.name}' OR sub_genre_1.name = '${genre.name}')`
        )
        return where
    }

    return {
        articles,
        filterList,
        setFilterList
    }
}
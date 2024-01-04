import React, { useState, useEffect } from 'react';
import { post } from '../../helper/CRUD.js';
import { Tracks } from './Tracks.js';
import { Details } from './Details.js';
import { BuyBtn } from './BuyBtn.js'
import "./Article.css"

const Article = ({ filterList }) => {
    const [articles, setArticle] = useState([])
    const [filter, setFilter] = useState([...filterList]);


    const images = [
        "b&b.jpg",
        "bertram.jpg",
        "bocchi.jpg",
        "bocchi2.jpg",
        "essen.jpg",
        "geisterbocchi.jpg",
        "momo.jpg",
        "momo2.jpg",
        "tunnelmomo.jpg",
        "erdbeerbocchi.jpg",
        "muederBertram.jpg",
    ]



    useEffect(() => {
        setFilter(filterList)
    }, [filterList])

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
    }, [filter]);

    const createWhere = () => {
        let where = ""
        // create the where clause, genre_1 / sub_genre_1 is because of the way sqlalchemie builds joined querys
        filter.forEach((genre) => where ? where += ` AND (genre_1.name = '${genre.name}' OR sub_genre_1.name = '${genre.name}')` :
            where += ` (genre_1.name = '${genre.name}' OR sub_genre_1.name = '${genre.name}')`
        )
        return where
    }

    const rndNumber = (min, max) => ~~(Math.random() * (max - min + 1) + min);

    const getPicture = () => {
        return `./images/${images[rndNumber(0, images.length - 1)]}`;
    }

    return (
        <div className='articleWrapper'>
            {articles.map((article, index) => (
                <div className="Article" key={index}>
                    <div className="Details">
                        <Details content={article} />
                        <BuyBtn content={article.price} />
                    </div>
                    <div className='Cover-image'>
                        <div className="Cover">
                            <img src={getPicture()}
                                className='CoverImg'
                                alt='Wurde nicht geladen?!'
                            />
                            <Tracks content={article.tracks} />
                        </div>
                    </div>
                </div>
            ))}
        </div>

    )
}

export { Article }
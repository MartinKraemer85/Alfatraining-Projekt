import React, { useState, useEffect } from 'react';
import { post } from '../../helper/CRUD.js';
import { Tracks } from './Tracks.js';
import { Details } from './Details.js';
import { BuyBtn } from './BuyBtn.js'
import "./Article.css"

const Article = props => {
    const [articles, setArticle] = useState([])

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
        post({
            url: "/select_all_articles",
            body: {
                "initial": true,
            }
        }).then(res => res.json()
        ).then(data => {
            setArticle(data)
        })

    }, []);
    const rndNumber = (min, max) => ~~(Math.random() * (max - min + 1) + min);

    const getPicture = () => {
        return `./images/${images[rndNumber(0, images.length - 1)]}`;
    }


    const createArticle = (data) => data.map((article, index) => {
        return (
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
        )
    })

    return (
        <>
            {createArticle(articles)}
        </>
    )
}

export { Article }
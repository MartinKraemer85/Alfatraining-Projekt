import { Tracks } from './Tracks.js';
import { Details } from './Details.js';
import { useNavigate } from "react-router-dom";
import "./Article.css"

export function Article({ articles }) {
    const navigate = useNavigate();

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

    const rndNumber = (min, max) => ~~(Math.random() * (max - min + 1) + min);
    const getPicture = () => `./images/${images[rndNumber(0, images.length - 1)]}`;

    return (
        <>
            {articles?.map((article, index) => (
                <div className="Article" key={index} onClick={() => navigate("/Article", { state: { article: article, } })}>
                    <div className="Details">
                        <Details content={article} />
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
        </>
    )
}


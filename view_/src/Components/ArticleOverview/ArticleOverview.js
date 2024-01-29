import { useLocation } from "react-router-dom";
import { Article } from "../Article/Article.js";

export function ArticleOverview() {
    const location = useLocation();
    const article = [location.state.article]

    return (
        <>
            <div>
                <Article articles={article} />
            </div>
        </>
    )

}
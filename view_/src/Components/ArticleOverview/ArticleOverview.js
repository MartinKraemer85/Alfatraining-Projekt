import { useLocation } from "react-router-dom";
import { Article } from "../Article/Article.js";
import "./ArticleOverview.css"
export function ArticleOverview() {
    const location = useLocation();
    const article = [location.state.article]

    const state = ["very bad", "bad", "okay", "good", "original"]
    function addToCard(article) {
        console.log("test");;
        if (cartItems[article.id] == null) {
            // https://developer.mozilla.org/en-US/docs/Glossary/Deep_copy
            cartItems[article.id] = JSON.parse(JSON.stringify(article));
            cartItems[article.id].quantity = 1
        }

    }


    return (
        <>
            <div>
                <Article articles={article} />
            </div>
            <div>
                {article?.map((element, index) => (
                    element.seller.map((seller, index) => (
                        <div className="divTable">
                            <div className="overViewWrapper">
                                <div className="overviewColumn">Seller: {seller.dealer.username}</div>
                                <div className="overviewColumn">Price: {seller.price}</div>
                                <div className="overviewColumn">State: {state[seller.state - 1]}</div>
                                <div className="overviewColumn">Current Amount: {seller.amount}</div>
                                <div className="overviewColumn"><button className="addtocartBtn" onClick={addToCard}><i className="fa fa-shopping-cart" /> </button></div>


                            </div>
                        </div>
                    ))
                ))}
            </div >
        </>
    )

}
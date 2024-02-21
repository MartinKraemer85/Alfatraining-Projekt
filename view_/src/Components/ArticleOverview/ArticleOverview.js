import { useLocation } from "react-router-dom";
import React from 'react';
import { Article } from "../Article/Article.js";
import "./ArticleOverview.css"

export function ArticleOverview({ cartList, setCartList }) {
    const location = useLocation();
    const article = [location.state.article]

    const state = ["very bad", "bad", "okay", "good", "original"]
    function addToCart(article, seller) {
        const searchObject = cartList.find((item) => {
            return item.seller_id === seller.seller_id && item.article_id == article.id
        });
        // if article allready exists, increase amount instead of adding another article
        if (searchObject) {
            searchObject.currentAmount += 1
            setCartList([...cartList])
        } else {
            // else add the current list and a new article object
            setCartList([...cartList, {
                "seller_id": seller.seller_id,
                "article_id": article.id,
                "artist": article.artist,
                "title": article.title,
                "type": article.type,
                "price": seller.price,
                "amount": seller.amount,
                "currentAmount": 1
            }])
        }
    }

    return (
        <>
            <div>
                <Article articles={article} />
            </div>
            <div>
                {article?.map((element) => (
                    element.seller.map((seller, index) => (
                        <div className="divTable" key={`divTable${index}`} >
                            <div className="overViewWrapper" >
                                <div className="overviewColumn">Seller: {seller.dealer.username}</div>
                                <div className="overviewColumn">Price: {seller.price}</div>
                                <div className="overviewColumn">State: {state[seller.state - 1]}</div>
                                <div className="overviewColumn">Current Amount: {seller.amount}</div>
                                <div className="overviewColumn"><button className="addtocartBtn" onClick={() => addToCart(element, seller)}>
                                    <i className="fa fa-shopping-cart" />
                                </button></div>
                            </div>
                        </div>
                    ))
                ))}
            </div >
        </>
    )

}
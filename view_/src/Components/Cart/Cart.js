import React from 'react';
import "./Cart.css"

export function Cart({ cartList, setCartList }) {


    function setAmount(seller_id, article_id, amount, incrDecr) {
        const searchObject = cartList.find((item) => {
            return item.seller_id === seller_id && item.article_id === article_id
        });

        if (searchObject.currentAmount < amount) {
            searchObject.currentAmount += incrDecr
            setCartList([...cartList])
        }

        // remove article
        if (searchObject.currentAmount <= 0) {
            const index = cartList.indexOf(searchObject)
            console.log(cartList);
            setCartList(cartList.length == 1 ? [] : [...cartList.splice(index - 1, 1)])
            console.log(cartList);
        }
    }

    function calculatePrice() {
        let price = 0
        cartList.forEach(item => {
            price += item.currentAmount * item.price
        })
        return price
    }

    return (
        <>
            <div className="cartContainer" >
                <div className="cart" id="cartId">
                    {cartList?.map((item, index) => {
                        return <div className="cart-item" key={index}>
                            <div className="cart-header">
                                <h4>{item.artist}-{item.title}</h4>
                            </div>

                            <div className="product-details">
                                <p>type: {item.type}</p>
                            </div>
                            <div className="counter">
                                <button onClick={() => setAmount(item.seller_id, item.article_id, item.amount, -1)}>-</button>
                                <span>{item.currentAmount}</span>
                                <button onClick={() => setAmount(item.seller_id, item.article_id, item.amount, 1)}>+</button>
                            </div>
                            <div className="price-section">
                                <p>Price: {item.price * item.currentAmount}</p>
                            </div>
                        </div>
                    })}

                    <div className="checkout-section" id="checkoutId">
                        <p>Total: {calculatePrice()}</p>
                        <button className="checkoutBtn">Checkout</button>
                        <button className="closeBtn" onClick={() => document.querySelector('body').classList.remove('active')}>Close</button>
                    </div>
                </div>

            </div>



        </>
    )
}
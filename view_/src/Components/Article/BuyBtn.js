//import "./Article.css"

const BuyBtn = props => {

    return (
        <div className="BuyBtn">
            <button className="Btn">
                <span className="Price">{props.content}€</span>
                <span className="Shopping-cart"><i class="fa fa-shopping-cart" aria-hidden="true"></i></span>
                <span className="Buy">Buy</span>
            </button>
        </div >
    )

}

export { BuyBtn }
//import "./Article.css"

export function BuyBtn(props) {

    return (
        <div className="BuyBtn">
            <button className="Btn">
                <span className="Price">{props.content}€</span>
                <span className="Shopping-cart"><i className="fa fa-shopping-cart" aria-hidden="true"></i></span>
                <span className="Buy">Buy</span>
            </button>
        </div >
    )

}

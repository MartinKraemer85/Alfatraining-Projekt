import "./Footer.css"

const Footer = props => {
    /**
     * It doesnt make sense to create the footer for other pages again, 
     * so create it in a fucntion
     */
    return (
        <div className="Footer">
            <footer>
                <p>Hier kommt was rein aus der db</p>
            </footer>
        </div>
    )

}

export { Footer }
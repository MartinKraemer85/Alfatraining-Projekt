/* eslint-disable jsx-a11y/accessible-emoji */
import React from "react";
import "./Header.css";

const Header = () => {
    return (
        <header className="Header">
            <img src={"./images/bocchi2.jpg"} className="Logo" alt="logo" />
            <nav className="Nav">
                <a href="/">Add Article</a>
                <a href="/">Wer weiß was noch</a>
                <a href="/">Impressum?</a>
                <button>Logout</button>
            </nav>
        </header>
    );
}

export { Header };

// https://codesandbox.io/p/sandbox/responsive-animated-top-navigation-bar-with-react-forked-032o8o?file=%2Fsrc%2Fcomponents%2FHeader.css%3A1%2C1-148%2C1
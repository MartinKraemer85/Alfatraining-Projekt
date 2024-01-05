/* eslint-disable jsx-a11y/accessible-emoji */
import React from "react";
import "./Header.css";
import { UserMenu } from "./UserMenu/UserMenu";
import {
    Link
} from 'react-router-dom';


const Header = () => {
    return (
        <header className="Header">
            <div className="navbar">
                <Link className="active navLink" to="/" ><i className="fa fa-fw fa-home"></i> Home</Link>
                <Link className="navLink" to="/AddArticle"><i className='far fa-edit'></i>Add Article</Link>
                <Link className="navLink" to='/Contact'><i className="fa fa-fw fa-envelope"></i> Contact</Link>
                <UserMenu />
            </div>
        </header>
    );
}

export { Header };

// https://codesandbox.io/p/sandbox/responsive-animated-top-navigation-bar-with-react-forked-032o8o?file=%2Fsrc%2Fcomponents%2FHeader.css%3A1%2C1-148%2C1
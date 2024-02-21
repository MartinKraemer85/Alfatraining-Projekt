/* eslint-disable jsx-a11y/accessible-emoji */
import React from "react";
import "./Header.css";
import { UserMenu } from "./UserMenu/UserMenu";
import {
    Link
} from 'react-router-dom';


export function Header() {



    return (
        <header className="Header">
            <div className="navbar">
                <Link className="active navLink" to="/" ><i className="fa fa-fw fa-home"></i> Home</Link>
                <Link className="navLink" to="/AddArticle"><i className='far fa-edit'></i>Add Article</Link>
                <Link className="navLink" to='/Contact'><i className="fa fa-fw fa-envelope"></i> Contact</Link>
                <UserMenu />
                <button className="buyBtn" onClick={() => document.querySelector('body').classList.toggle('active')}>
                    <i className="fa fa-shopping-cart" />
                </button>
            </div>
        </header>
    );
}
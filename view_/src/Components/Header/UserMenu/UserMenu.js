import "./UserMenu.css"
import React, { useRef } from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUser } from "@fortawesome/free-regular-svg-icons"
import { Link } from "react-router-dom";

const UserMenu = () => {
    const menu = useRef()

    const handleClick = () => {
        menu.current.classList.toggle("show")
    }

    const closeOpenMenus = (e) => {
        if (!menu.current?.contains(e.target)) {
            menu.current?.classList.remove("show")
        }
    }
    document.addEventListener('mousedown', closeOpenMenus)

    return (
        <div className="Menu">
            <button onClick={handleClick} className="dropbtn"><FontAwesomeIcon icon={faUser} /></button>
            <div className="content" ref={menu}>
                <Link to="/Profile" className="profLink">Profile</Link>
                <Link to="/AddArticle" className="profLink">add Article</Link>
                <Link to="/Logout" className="profLink">Logout</Link>
            </div>
        </div>
    )
}

export { UserMenu }
'use strict';
import { dom } from "../dom.js"


const createFilter = ({ headerText = "Genre", bulletPoints } = {}) => {
    /**
     * Appends the genre / sub genre filter to the navigation
     * */
    const nav = document.querySelector("#nav")
    dom.create({
        type: "h2",
        content: headerText,
        parent: nav
    })

    bulletPoints.forEach((el) => {
        dom.create({
            type: "li",
            content: el.name,
            parent: nav
        })
    });
}

export { createFilter }
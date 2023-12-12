'use strict';
import { dom } from "../dom.js"

const createFilter = ({ headerText = "Genre", bulletPoints } = {}) => {
    /**
     * Appends the genre / sub genre filter to the navigation
     * */
    const nav = document.querySelector("#nav")
    const header = dom.create({
        type: "h2",
        content: headerText,
        parent: nav
    })

    bulletPoints.forEach((el) => {
        dom.create({
            type: "li",
            content: el.name,
            parent: header
        })
    });
}

export { createFilter }
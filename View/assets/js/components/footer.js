'use strict';
import { dom } from "../dom.js"


const createFooter = () => {
    /**
     * It doesnt make sense to create the footer for other pages again, 
     * so create it in a fucntion
     */
    return dom.create({
        content: `<h1>Hier kommen Footer Daten herein, welche auch immer das sein werden</h1>`,
        type: "footer",
    })
}

export { createFooter }
'use strict';
const createFooter = () => {
    /**
     * It doesnt make sense to create the footer for other pages again, 
     * so create it in a fucntion
     */
    const footer = document.createElement("footer")
    footer.innerHTML = 
    `
        <h1>Hier kommen Footer Daten herein, welche auch immer das sein werden</h1>
    `
    return footer
}

export {createFooter}
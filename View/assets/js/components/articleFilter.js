'use strict';
import { dom } from "../helper/dom.js"
import { elements } from "../settings.js";

let filterArr = []

const filterData = () => {
    /** 
     * A function for article filter purposes.
     * First, iterate over the articles via filter, check if article has a genre.
     * If this is the case, check if the filters array includes the genre name
     * Filter genre and sub genre aswell
    */

    console.log("test", elements.articles.filter(article => {
        article.filterGenre(filterArr)
    }))

    return filterArr.length ? elements.articles.filter(article => {
        article.filterGenre(filterArr)
    }) : elements.articles
}

const filterClick = (evt) => {
    /**
     *  Click event for the filter button. Adding an highlight class to the filter dom element
     *  on the navbar. Also or removes the clicked filter from the filter array.
     * */
    const target = evt.currentTarget;
    target.classList.toggle('highlight')
    if (target.classList.contains('highlight') &&
        !filterArr.includes(evt.currentTarget.innerText)) {
        // add to Filter array
        filterArr.push(evt.currentTarget.innerText);
    } else {
        // removing from the filters array
        filterArr = filterArr.filter(el => {
            el == evt.currentTarget.innerText ? 0 : 1
        })

        // if the filterarray is empty, reset the currentRowAmount to 10
        if (!filterArr.length) localStorage.setItem('currentRowAmount', "10")
    }
    // filter the data
    //const filterdData = filterData()
    //console.log(filterdData);
    // render the table with the applied filters
    //initTable(elements.tableHead, elements.tableBody, elements.tableFoot, elements.articles, elements.filterArr)
}




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
            parent: nav,
            listeners: {
                "click": (evt) => {
                    // first parent is the td, second parent is the tr
                    // TODO: rausfinden wie man vom aktuellen element das naechst hoehere x element sucht?!
                    //addToCard(data)
                    filterClick(evt)
                }
            }
        })
    });
}

export { createFilter }
'use strict';

import { get } from './helper/CRUD.js';
import { elements } from './settings.js';
import { initTable } from './Table.js';
import { initCart } from './components/cart.js'
import { createFooter } from './components/footer.js'
import { Article } from './models/article.js'
import { createFilter } from './components/filter.js'
import { dom, $ } from './helper/dom.js';

// KONSTANTEN / VARIABLEN
elements.articles = []

// FUNKTIONEN
const domMapping = () => {
    elements.tableHead = document.querySelector("#head")
    elements.tableBody = document.querySelector("#body")
    elements.tableFoot = document.querySelector("#foot")
    elements.filterArr = []
}

const appendEventlisteners = () => {
    /**
     * add the Eventlistener like the filter function for the genre / subegenre navbar
     * */

    // Genre / SubGenre click event
    for (const el of Array.from(document.querySelectorAll("li"))) {
        el.addEventListener('click', filterClick);
    }


}


const filterClick = (evt) => {
    /**
     *  Click event for the filter button. Adding an highlight class to the filter dom element
     *  on the navbar. Also or removes the clicked filter from the filter array.
     * */
    const target = evt.currentTarget;
    target.classList.toggle('highlight')
    if (target.classList.contains('highlight') &&
        !elements.filterArr.includes(evt.currentTarget.innerText)) {
        // add to Filter array
        elements.filterArr.push(evt.currentTarget.innerText);
    } else {
        // removing from the filters array
        elements.filterArr = elements.filterArr.filter(el => {
            el == evt.currentTarget.innerText ? 0 : 1
        })

        // if the filterarray is empty, reset the currentRowAmount to 10
        if (!elements.filterArr.length) localStorage.setItem('currentRowAmount', "10")
    }

    // render the table with the applied filters
    initTable(elements.tableHead, elements.tableBody, elements.tableFoot, elements.articles, elements.filterArr)
}

const loadData = async () => {
    /**
     * First, load all the data we need
     */

    const articles = await get({
        url: "http://192.168.0.2:5000/select_all_articles",
        body: { "initial": true }
    });

    articles.forEach(article => elements.articles.push(new Article(article)))
    console.log(articles);
    // set the genre / subgenres for the bulletpoints
    // also create an array with all genres so the filtering is easier 
    // (only one array instead of both genre and subgenre array)

    elements.genre = await get({
        url: "http://192.168.0.2:5000/select",
        body: {
            "table": "genre",
            "fields": ["name"]
        }
    });

    elements.subGenre = await get({
        url: "http://192.168.0.2:5000/select",
        body: {
            "table": "sub_genre",
            "fields": ["name"]
        }
    });


}

const init = async () => {
    domMapping();
    await loadData();
    createFilter({ bulletPoints: elements.genre });
    createFilter({ headerText: "Sub Genre", bulletPoints: elements.subGenre });
    appendEventlisteners();
    initTable(elements.tableHead, elements.tableBody, elements.tableFoot, elements.articles, elements.filterArr)
    initCart(elements.articles)
    $(".cardContainer").append(createFooter())
    /*
    const worker = new Worker('./assets/js/workers/initialFullLoad.js', { type: "module" })

    worker.postMessage(JSON.parse(JSON.stringify(elements)));
    worker.onmessage = (msg) => {
        console.log(msg.data);

    }
    */
}

// INIT
init();


'use strict';

import { get } from './helper/CRUD.js';
import { elements } from './settings.js';
import { cart } from './components/cart.js'
import { Article } from './models/article.js'
import { createFilter } from './components/articleFilter.js'
import { table } from './components/table/table.js';
import { $ } from './helper/dom.js';

// KONSTANTEN / VARIABLEN
elements.articles = []

// FUNKTIONEN
const domMapping = () => {
    elements.main = $("main")
    elements.tableHead = $("#head")
    elements.tableBody = $("#body")
    elements.tableFoot = $("#foot")
    elements.filterArr = []
}

const loadData = async () => {
    /**
     * First, load all the data we need
     */

    const articles = await get({
        url: "http://192.168.0.2:5000/select_all_articles",
        body: { "initial": true }
    });
    console.log(articles);
    articles.forEach(article => elements.articles.push(new Article(article)))
    let test = elements.articles.map(article => article.filterGenre("Black Metal")
    );
    console.log("test", test);
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
    elements.main.append(table(elements.articles))
    //initTable(elements.tableHead, elements.tableBody, elements.tableFoot, elements.articles, elements.filterArr)
    cart(elements.articles)
    //$(".cardContainer").append(createFooter())



    const worker = new Worker('./assets/js/workers/initialFullLoad.js', { type: "module" })

    worker.postMessage(JSON.parse(JSON.stringify(elements)));
    worker.onmessage = (msg) => {

    }

}

// INIT
init();


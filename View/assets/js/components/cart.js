'use strict';
import { create, $ } from "../helper/dom.js"
import { rndNumber, images } from "../settings.js";

// KONSTANTEN / VARIABLEN
const elements = {};
let cartItems = {};

// FUNKTIONEN
const domMapping = () => {
    elements.openShopping = $('.shopping');
    elements.closeShopping = $('.closeShopping');
    elements.list = $('.list');
    elements.listCard = $('.listCard');
    elements.body = $('body');
    elements.total = $('.total');
    elements.quantity = $('.quantity');
}

const appendEventlisteners = () => {
    elements.openShopping.addEventListener('click', () => {
        elements.body.classList.add('active');
    })
    elements.closeShopping.addEventListener('click', () => {
        elements.body.classList.remove('active');
    })
}

const addToCard =
    /**
    * Add an article per id to the cartItems that will be rendered on reloadCard
    * @date 11/29/2023 - 5:32:03 AM
    *
    * @param {*} article the current article that was added via add button
    */
    (article) => {

        if (cartItems[article.id] == null) {
            // https://developer.mozilla.org/en-US/docs/Glossary/Deep_copy
            cartItems[article.id] = JSON.parse(JSON.stringify(article));
            cartItems[article.id].quantity = 1
        }
        reloadCard();
    }


const append = /**
    * Description placeholder
    * @date 11/29/2023 - 5:31:37 AM
    *
    * @param {*} el domElement to append to
    * @param {...{}} toAppend domElements to append to the Element
    */
    (el, ...toAppend) => {
        toAppend.forEach(element => {
            el.append(element)
        });
    }

const reloadCard = /**
    * Iterate over the deep copy of the actual table data that was appended to an seperate card array.
    * If we don't work with a deep copy, we would change the price of the original element by reference.
    * @date 11/29/2023 - 5:34:24 AM
    */
    () => {
        elements.listCard.innerHTML = '';
        let totalPrice = 0;

        // seperate counter for the article amount, since we dont't have acces to the key after the
        // loop is finished.
        let count = 0;
        for (const [key, article] of Object.entries(cartItems)) {
            const org_article = elements.org_articles.filter(article => article.id == key)[0]
            totalPrice = totalPrice + article.price;
            count += cartItems[key].quantity;

            // create all the elements

            // -------------------- article stuff --------------------
            const newArticle = create({
                type: "li"
            })

            const imageContainer = create({
                type: "div",
                parent: newArticle
            })
            create({
                type: "img",
                attr: { src: images[rndNumber(0, images.length - 1)] },
                parent: imageContainer
            })
            create({
                content: `${article.artist} - ${article.title}`,
                type: "div",
                parent: newArticle
            })
            create({
                content: `${article.price.toLocaleString()}€`,
                type: "div",
                parent: newArticle
            })


            // --------------------- Bottom stuff ------------------------
            // set button listener to increase / decrease the amount a user want to buy

            const quantityContainer = create({
                type: "div",
                parent: newArticle
            })

            create({
                content: "-",
                type: "button",
                listeners: {
                    "click": () => {
                        cartItems[key].quantity -= 1;
                        if (article.quantity) cartItems[key].price = cartItems[key].quantity * org_article.price;
                        else delete cartItems[key];
                        reloadCard();
                    }
                },
                parent: quantityContainer
            })

            create({
                content: `${article.quantity}`,
                type: "div",
                parent: quantityContainer
            })

            create({
                content: "+",
                type: "button",
                listeners: {
                    "click": () => {
                        cartItems[key].quantity += 1;
                        cartItems[key].price = cartItems[key].quantity * org_article.price;
                        reloadCard();
                    }
                },
                parent: quantityContainer
            })

            // append the elements to the html
            elements.listCard.appendChild(newArticle);
        }
        elements.total.innerText = totalPrice;
        elements.quantity.innerText = count;
    }

const initCart = (articles) => {
    /* Init the cart elements
    * @param {*} articles The article list we've got from the get request
    */
    domMapping();
    appendEventlisteners();
    elements.org_articles = articles
}

export { initCart, addToCard }
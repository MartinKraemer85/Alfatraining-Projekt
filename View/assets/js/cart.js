'use strict';

const elements = {}

elements.images = [
    "./assets/images/bertram.jpg",
    "./assets/images/bocchi.jpg",
    "./assets/images/bocchi2.jpg",
    "./assets/images/momo.jpg",
    "./assets/images/momo2.jpg",
]
const createEl = (el) => document.createElement(el)
const selectEl = (el) => document.querySelector(el)

let cartItems = {};

const initCart = /**
    * Init the cart elements
    * @date 11/29/2023 - 5:35:19 AM
    *
    * @param {*} articles The article list we've got from the get request
    */
    (articles) => {

        elements.openShopping = selectEl('.shopping');
        elements.closeShopping = selectEl('.closeShopping');
        elements.list = selectEl('.list');
        elements.listCard = selectEl('.listCard');
        elements.body = selectEl('body');
        elements.total = selectEl('.total');
        elements.quantity = selectEl('.quantity');
        elements.org_articles = articles

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
            console.log(cartItems);
        }
        reloadCard();

    }
const createNumber = (min, max) => ~~(Math.random() * (max - min + 1) + min);

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
            const newArticle = createEl('li');
            const imageContainer = createEl("div")
            const img = createEl("img")
            const artist = createEl("div")
            const price = createEl("div")
            const quantityContainer = createEl("div")
            const buttonIncrease = createEl("button")
            const currentQuantity = createEl("div")
            const buttonDecrease = createEl("button")

            img.src = elements.images[createNumber(0, elements.images.length - 1)]
            artist.innerText = `${article.artist} - ${article.title}`
            price.innerText = `${article.price.toLocaleString()}€`

            // set button listener to increase / decrease the amount a user want to buy
            buttonIncrease.innerText = "+"
            buttonIncrease.addEventListener("click", () => {
                cartItems[key].quantity += 1;
                cartItems[key].price = cartItems[key].quantity * org_article.price;
                reloadCard();
            })

            currentQuantity.innerText = `${article.quantity}`

            buttonDecrease.innerText = "-"
            buttonDecrease.addEventListener("click", () => {
                cartItems[key].quantity -= 1;
                if (article.quantity) cartItems[key].price = cartItems[key].quantity * org_article.price;
                else delete cartItems[key];
                reloadCard();
            })

            // append the elements to the html
            imageContainer.append(img)
            append(quantityContainer, buttonDecrease, currentQuantity, buttonIncrease)
            append(newArticle, imageContainer, artist, price, quantityContainer)
            elements.listCard.appendChild(newArticle);
        }
        elements.total.innerText = totalPrice;
        elements.quantity.innerText = count;
    }


export { initCart, addToCard }

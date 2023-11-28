'use strict';

const elements = {}

elements.images = [
    "./assets/images/bertram.jpg",
    "./assets/images/bocchi.jpg",
    "./assets/images/bocchi2.jpg",
    "./assets/images/momo.jpg",
    "./assets/images/momo2.jpg",
]

let cartItems  = {};

const initCart = (document, articles) => {
    elements.openShopping = document.querySelector('.shopping');
    elements.closeShopping = document.querySelector('.closeShopping');
    elements.list = document.querySelector('.list');
    elements.listCard = document.querySelector('.listCard');
    elements.body = document.querySelector('body');
    elements.total = document.querySelector('.total');
    elements.quantity = document.querySelector('.quantity');
    elements.org_articles = articles
    elements.openShopping.addEventListener('click', ()=>{
        elements.body.classList.add('active');
    })
    elements.closeShopping.addEventListener('click', ()=>{
        elements.body.classList.remove('active');
    })


}

const addToCard = (article) => {

    if(cartItems[article.id] == null){
       // https://developer.mozilla.org/en-US/docs/Glossary/Deep_copy
       cartItems[article.id] = JSON.parse(JSON.stringify(article));
       cartItems[article.id].quantity = 1
       console.log(cartItems);
    }
    reloadCard();

}
const createNumber = (min, max) => ~~(Math.random() * (max - min + 1) + min);


const reloadCard =() => {
    elements.listCard.innerHTML = '';
    let totalPrice = 0;
    let count = 0;
    for (const [key, article] of Object.entries(cartItems)) {
        const org_article = elements.org_articles.filter(article => article.id == key)[0]
        console.log(org_article);
        totalPrice = totalPrice + article.price;
        count += cartItems[key].quantity;
        const newArticle = document.createElement('li');
        const imageContainer = document.createElement("div")
        const img = document.createElement("img")
        imageContainer.append(img)
        const artist = document.createElement("div")
        const price = document.createElement("div")
        const quantityContainer = document.createElement("div")
        const buttonIncrease = document.createElement("button")
        const currentQuantity = document.createElement("div")
        const buttonDecrease = document.createElement("button")
        
        img.src = elements.images[createNumber(0, elements.images.length - 1)]
        artist.innerText = `${article.artist} - ${article.title}`
        price.innerText = `${article.price.toLocaleString()}€`

        buttonIncrease.innerText = "+"
        buttonIncrease.addEventListener("click", () =>{
            cartItems[key].quantity += 1;
            cartItems[key].price = cartItems[key].quantity * org_article.price;  
            console.log(elements.articles);
            reloadCard();
        })

        currentQuantity.innerText = `${article.quantity}`
        
        buttonDecrease.innerText = "-"
        buttonDecrease.addEventListener("click", () =>{
            cartItems[key].quantity -= 1;
            if(article.quantity) cartItems[key].price = cartItems[key].quantity * org_article.price;
            else delete cartItems[key];
            reloadCard();
        })


        quantityContainer.append(buttonDecrease)
        quantityContainer.append(currentQuantity)
        quantityContainer.append(buttonIncrease)
        newArticle.append(imageContainer)
        newArticle.append(artist)
        newArticle.append(price)
        newArticle.append(quantityContainer)
        elements.listCard.appendChild(newArticle);        
    }
    elements.total.innerText = totalPrice;
    elements.quantity.innerText = count;
}


export { initCart , addToCard}

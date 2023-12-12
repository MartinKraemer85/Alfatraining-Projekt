'use strict';

const elements = {}

elements.images = [
    "./assets/images/b&b.jpg",
    "./assets/images/bertram.jpg",
    "./assets/images/bocchi.jpg",
    "./assets/images/bocchi2.jpg",
    "./assets/images/essen.jpg",
    "./assets/images/geisterbocchi.jpg",
    "./assets/images/momo.jpg",
    "./assets/images/momo2.jpg",
    "./assets/images/tunnelmomo.jpg",
]

const rndNumber = (min, max) => ~~(Math.random() * (max - min + 1) + min);


export { elements, rndNumber }
export let images = elements.images
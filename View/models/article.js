'use strict';

import { dom } from '../assets/js/dom.js'

class Article {

    genres = []
    sub_genres = []

    constructor (obj) {
        Object.assign(this, obj);  
    }

    createDom(tr) {
        console.log("muh");
    }
}

export {Article};
'use strict';

import { dom } from '../helper/dom.js'
import { addToCard } from '../components/cart.js'
import { createNumber } from '../helper/generalHelper.js'
import { images } from '../settings.js';

class Article {
    //genres = []
    //sub_genres = []

    constructor(obj) {
        Object.assign(this, obj);
    }
    getId() {
        return this.id
    }

    filterGenre(filter = []) {
        console.log(filter);

        return this.genres.filter((genre) => {
            return filter.includes(genre.genre.name)
        }) ? this : {}
    }

    filterSubGenre(filter = []) {
        this.sub_genres.filter((subGenre) => filter.includes(subGenre.subGenre.name)) ? this : {}
    }
}

export { Article };
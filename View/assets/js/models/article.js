'use strict';

import { dom } from '../dom.js'
import { addToCard } from '../cart.js'
import { createNumber } from '../helper.js'

class Article {
    genres = []
    sub_genres = []

    // only for testing 
    #images = [
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

    constructor(obj) {
        Object.assign(this, obj);
    }

    createTableRow(head = false, tableElement) {
        /**
         * Description placeholder
         * @date 12/11/2023 - 9:55:06 AM
         *
         * @type {*}
         */

        const tr = dom.create({
            type: "tr",
            classes: !head ? ["hover"] : [],
            listeners: {
                'click': (evt) => {
                    if (evt.target.tagName.toLowerCase().match("button|i")) return
                    const target = evt.currentTarget;
                    // convert to jQuery for the usage of slideUp /Down
                    const pTag = $(target.nextSibling);

                    $(pTag).is(":visible") ? $(pTag).slideUp('fast') : $(pTag).slideDown('fast')
                }
            },
            parent: tableElement
        });

        // fill the row with class properties
        for (const [key, value] of Object.entries(this)) {

            // Ignore relationships like the genre
            if (typeof value == 'object') continue;
            if (key.match('state')) continue;

            const thtd = dom.create({
                type: head ? "th" : "td",
                content: head ? key : value,
                // hide the id field from the user
                attr: key.match('id') ? { hidden: true, id: "articleId" } : {},
                parent: tr
            });
        }
        this.#addToCartButton(tr, head)
    }

    createInfoRow(head = false, tableElement, colsSpan) {
        this.infoRow = dom.create({
            type: "tr",
            classes: ["infoTr"],
            attr: { hidden: true }
        })

        this.infoTd = dom.create({
            type: "td",
            classes: ["infoTr"],
            attr: { colSpan: 6 },
            parent: this.infoRow
        })


        if (!head) this.#addCover(tableElement)
        if (!head) this.#addTrackInfo(tableElement)
        if (!head) this.#addVendorInfo(tableElement)

        tableElement.append(this.infoRow)
    }

    #addCover() {
        /**
         * Add the article cover to the hidden table row
         */
        const infoContainer = dom.create({
            type: "div",
            classes: ["infoDiv"],
            parent: this.infoTd
        })

        dom.create({
            type: "img",
            classes: ["cover"],
            attr: { alt: true, src: this.#images[createNumber(0, this.#images.length - 1)] },
            parent: infoContainer
        })

    }

    #addTrackInfo() {
        /** 
         * Iterate the tracks objects and add them to the info row
         */
        const infoContainer = dom.create({
            type: "div",
            classes: ["infoDiv"],
            parent: this.infoTd
        })

        const trackList = dom.create({
            type: "ul",
            parent: infoContainer
        })

        this.tracks.forEach(track => {
            dom.create({
                type: "li",
                content: `${track.title} (${track.length})`,
                parent: trackList
            })
        })
    }

    #addVendorInfo() {
        /** 
         * TODO
         */

        dom.create({
            type: "div",
            classes: ["infoDiv"],
            parent: this.infoTd,
            content: "todo: Händerfreude"
        })
    }

    #addToCartButton(tr, head) {
        /**
        * Takes the current row (if not the head) and adds the to cart button
        * @date 11/29/2023 - 5:37:45 AM
        *
        * @param {object} tr the current table row we want to fill / add
        * @param {Boolean} head determines if head or body element
        */

        if (head) {
            // just create an empty header column
            tr.append(dom.create({
                type: "th",
            }))
            return
        };

        const td = dom.create({
            type: "td",
            styles: { textAlign: "center" },
            parent: tr
        });

        const btn = dom.create({
            type: "button",
            parent: td,
            classes: ["addtocartBtn"],
            listeners: {
                "click": () => {
                    addToCard(this)
                }
            }
        });

        dom.create({
            type: "i",
            parent: btn,
            classes: ["fa", "fa-shopping-cart"]
        });



    }


}

export { Article };
'use strict';

import { dom } from "../../../../helper/dom.js";

const cartButton = (head) => {
    /**
    * Takes the current row (if not the head) and adds the to cart button
    * @date 11/29/2023 - 5:37:45 AM
    *
    * @param {object} tr the current table row we want to fill / add
    * @param {Boolean} head determines if head or body element
    */

    if (head) {
        // just create an empty header columnx
        return dom.create({
            type: "th",
        })
    };

    const td = dom.create({
        type: "td",
        styles: { textAlign: "center" },
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

    return td
}

export { cartButton }
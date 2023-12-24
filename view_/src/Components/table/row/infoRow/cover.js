'use strict';

import { dom } from "../../../../helper/dom.js";
import { images, rndNumber } from "../../../../settings.js";

const cover = () => {
    /**
     * Add the article cover to the hidden table row
     */
    const infoContainer = dom.create({
        type: "div",
        classes: ["infoDiv"]
    })

    dom.create({
        type: "img",
        classes: ["cover"],
        attr: { alt: true, src: images[rndNumber(0, images.length - 1)] },
        parent: infoContainer
    })
    return infoContainer
}

export { cover }
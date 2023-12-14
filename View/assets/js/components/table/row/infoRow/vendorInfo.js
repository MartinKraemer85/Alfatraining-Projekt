'use strict';

import { dom } from "../../../../helper/dom.js";

const vendorInfo = (td) => {
    /** 
     * TODO
     */

    return dom.create({
        type: "div",
        classes: ["infoDiv"],
        parent: td,
        content: "todo: Händerfreude"
    })

}

export { vendorInfo }
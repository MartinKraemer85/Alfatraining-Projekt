'use strict';

import { dom } from "../../../../helper/dom.js";

const trackInfo = (td, tracks) => {
    /** 
     * Iterate the tracks objects and add them to the info row
     */
    const trackContainer = dom.create({
        type: "div",
        classes: ["infoDiv"],
        parent: td
    })

    const trackList = dom.create({
        type: "ul",
        parent: trackContainer
    })

    tracks.forEach(track => {
        dom.create({
            type: "li",
            content: `${track.title} (${track.length})`,
            parent: trackList
        })
    })

    return trackContainer
}

export { trackInfo }
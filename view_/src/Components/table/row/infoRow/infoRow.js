'use strict';

import { dom } from "../../../../helper/dom.js";
import { cover } from "./cover.js";
import { trackInfo } from "./trackInfo.js";
import { vendorInfo } from "./vendorInfo.js";

const infoRow = ({ head = false, tracks = {}, vendor = {}, colsSpan = 6 } = {}) => {
    const tr = dom.create({
        type: "tr",
        classes: ["infoTr"],
        attr: { hidden: false }
    })

    const infoTd = dom.create({
        type: "td",
        classes: ["infoTr"],
        attr: { colSpan: colsSpan },
        parent: tr
    })


    if (!head) infoTd.append(cover())
    if (!head) infoTd.append(trackInfo(infoTd, tracks))
    if (!head) infoTd.append(vendorInfo(infoTd))

    return tr
}

export { infoRow }
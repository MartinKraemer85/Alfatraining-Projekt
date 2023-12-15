import { dom } from "../../../helper/dom.js"
import { infoRow } from "./infoRow/infoRow.js";
import { cartButton } from "./tableRow/cartButton.js";

const row = ({ head = false, data, addCartButton = true, addInfoRow = true, tbody } = {}) => {
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
    });

    // fill the row with class properties
    for (const [key, value] of Object.entries(data)) {

        // Ignore relationships like the genre
        if (typeof value == 'object') continue;
        if (key.match('state')) continue;

        dom.create({
            type: head ? "th" : "td",
            content: head ? key : value,
            // hide the id field from the user
            attr: key.match('id') ? { hidden: true, id: "articleId" } : {},
            parent: tr
        });
    }
    if (addCartButton) tr.append(cartButton(head))
    if (addInfoRow) tbody.append(infoRow({ head: head, tracks: data.tracks }))
    return tr
}

export { row }
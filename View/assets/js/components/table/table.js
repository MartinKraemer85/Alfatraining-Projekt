'use strict';

import { create, $ } from "../../helper/dom.js";
import { footer } from "./footer.js";
import { row } from "./row/row.js";
import { getCurrentRowAmount } from "../../helper/generalHelper.js";

const elements = {}

const removeElements = (el) => {
    while (el.firstChild) {
        el.removeChild(el.firstChild);
    }
    console.log(el);
}

const createTableStructure = () => {

    elements.table = create({
        type: "table",
        attr: { id: "table" },
        classes: ["dataTable"],
        parent: elements.tableContainer
    })

    elements.thead = create({
        type: "thead",
        attr: { id: "head" },
        parent: elements.table
    })

    elements.tbody = create({
        type: "tbody",
        attr: { id: "body" },
        parent: elements.table
    })

    elements.tfoot = create({
        type: "tfoot",
        attr: { id: "foot" },
        parent: elements.table
    })
}
const domMapping = () => {
    elements.tableContainer = $(".tableContainer")
}

const table = (tableData, cartButton = true, infoRow = true) => {
    /** 
     * Appends a table to a table head / body tag, and fills the table with the given data
     * 
     * @tabbleHead {domElement} the table head where the table should be append to
     * @tableBody {domElement} the table body element where the table should be append to
     * @tableFoot {domElement} the table footer element where the table should be append to
     * @tableData {Array[dict]} the data to fill the table
     * @filterArr {Array} the data to fill the table
     * i.e. [{
            "artist": "Mokturnal Mortum",
            "genres": [
                {
                    "genre": {
                        "id": 1,
                        "name": "Rock"
                    },
                    "genre_id": 1,
                    "record_id": 1
                },
                {
                    "genre": {
                        "id": 3,
                        "name": "Metal"
                    },
                    "genre_id": 3,
                    "record_id": 1
                }
            ],
            "id": 1,
            "price": 20.989999771118164,
            "state": 2,
            "sub_genres": [
                {
                    "record_id": 1,
                    "sub_genre": {
                        "id": 1,
                        "name": "DBM"
                    },
                    "sub_genre_id": 1
                }
            ],
            "title": "Lunar Poetry",
            "tracks": [
                {
                    "id": 1,
                    "length": "00:05:23",
                    "record_id": 1,
                    "title": "track1",
                    "track_number": 1
                },
                {
                    "id": 2,
                    "length": "00:05:23",
                    "record_id": 1,
                    "title": "track2",
                    "track_number": 2
                },
                {
                    "id": 3,
                    "length": "00:05:23",
                    "record_id": 1,
                    "title": "track3",
                    "track_number": 3
                }
            ],
            "type": "Vinyl",
            "year": 2008
        }]
    */

    // first, clear the old tabledata
    domMapping()
    removeElements($(".tableContainer"))
    // and create the table structure
    createTableStructure()

    let count = 0;
    console.log("-------------------");
    console.log(tableData);
    console.log(getCurrentRowAmount());
    console.log("-------------------");
    for (const obj of tableData) {
        // only render the amount the user has set
        if (count == getCurrentRowAmount()) break

        // row == 0 -> head row
        if (!count) {

            elements.thead.append(row({ data: obj, head: true, tbody: elements.tbody }))
            // set the max cols we have in the table
            elements.colspan = elements.thead.rows[0].cells.length;
        }

        elements.tbody.append(row({ data: obj, head: false, tbody: elements.tbody }))
        count++;
    }
    elements.tfoot.append(footer({ tableData: tableData }))
    return elements.container
}

export { table }
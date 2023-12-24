'use strict';

import { create, $ } from "../../helper/dom.js";
import { table } from "../table.js";
import { getCurrentPage, getCurrentRowAmount, setLocalStorage } from "../../helper/generalHelper.js";

const elements = {}
elements.rowAmounts = [5, 10, 25]
elements.paginationData = []

const setTablePadding = () => {
    // if there are 25 or more rows displayed, set the table padding so the footer isnt preventing
    // clicking on the menue
    /*
    const tableContainer = document.querySelector(".tableContainer");
    console.log(tableContainer);
    if (tableContainer.clientHeight >= 70) tableContainer.style.paddingBottom = "10em"
    else tableContainer.style.paddingBottom = "0em";
    */
}

const addRowAmountBtn = (tableData, tr) => {
    /** 
     * Appends the row amount buttons to the left of the footer tr
     * 
     * @tabbleHead {domElement} the table head where the table should be append to
     * @tableBody {domElement} the table body element where the table should be append to
     * @tableFoot {domElement} the table footer element where the table should be append to
     * @tableData {Array[dict]} the data to fill the table
     * @filter {Array} the data to fill the table
     * @tr {Array} the footer table row
     * */

    const tdLeft = create({
        type: "td",
        classes: ["tableBtnLeft"],
        attr: { colSpan: Math.floor(elements.columns / 2) },
        parent: tr
    })

    setTablePadding()
    // Displayed row amount:
    // iterate over the row amounts array (how many rows are displayed in the table)
    // for each entrie, add an button + event listener
    elements.rowAmounts.forEach(value => {
        create({
            type: "button",
            classes: ["tableBtnLeft"],
            content: value,
            listeners: {
                "click": (event) => {
                    // set the new row amount 
                    setLocalStorage({ key: 'currentRowAmount', value: event.target.innerText })
                    // also reset the page
                    setLocalStorage({ key: 'currentPage', value: 1 })
                    table(tableData)
                }
            },
            parent: tdLeft
        });
    })
}

const addPaginationBtn = (tableData, tr) => {
    /** 
     * Appends the pagination buttons to the right of the footer tr
     * 
     * @tabbleHead {domElement} the table head where the table should be append to
     * @tableBody {domElement} the table body element where the table should be append to
     * @tableFoot {domElement} the table footer element where the table should be append to
     * @tableData {Array[dict]} the data to fill the table
     * @filter {Array} the data to fill the table
     * @tr {Array} the footer table row
     * */
    const td = create({
        type: "td",
        classes: ["tableBtnRight"],
        attr: { colSpan: Math.ceil(elements.columns / 2) },
        parent: tr
    })

    // Pagination:
    // First, get the pagination amount by dividing the tabledata with the current amount of displayed
    // items. 
    // Use ceil to allways round up
    const paginationAmount = Math.ceil(tableData.length / getCurrentRowAmount())
    for (let i = 1; i <= paginationAmount; i++) {
        // create the pagination buttons and add them to the right column of the 
        // table footer element

        create({
            type: "button",
            classes: ["tableBtnLeft"],
            content: i,
            listeners: {
                "click": (event) => {
                    setLocalStorage({ key: 'currentPage', value: event.target.innerText })
                    console.log("innerhtml", event.target.innerText);
                    console.log("page?", getCurrentPage());
                    //render table again, but only use the data from the given page
                    table(tableData)
                }
            },
            parent: td
        });
    }
}

const footer = ({ tableData, columns = 6 } = {}) => {
    /** 
 * Appends the tablefooter, constisting of the pagination and the row amount buttons
 * 
 * @tabbleHead {domElement} the table head where the table should be append to
 * @tableBody {domElement} the table body element where the table should be append to
 * @tableFoot {domElement} the table footer element where the table should be append to
 * @tableData {Array[dict]} the data to fill the table
 * @filter {Array} the data to fill the table
 * */
    // create a new table row first, and place the buttons within the row later on
    elements.columns = columns
    const tr = create({
        type: "tr",
        classes: ["foot"]
    })
    console.log(tableData);
    // What we also need to do is setting the coolspan.
    // this way we can make sure that the buttons in the footer 
    // are in the correct place. 
    // --> row amount buttons left,
    // --> pagination buttons right

    // the buttons for the table amount (display 5,10,xx at once)
    addRowAmountBtn(tableData, tr)
    addPaginationBtn(tableData, tr)
    return tr
}

export { footer }
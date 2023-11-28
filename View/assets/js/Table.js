

'use strict';
import { addToCard } from './cart.js'

const elements = {}
elements.rowAmounts = [5, 10, 25]
elements.currentRowAmount = 10
elements.page = 1
elements.paginationData = []

// covers not implemented in the backend yet, so just take some piggi pics
elements.images = [
    "./assets/images/bertram.jpg",
    "./assets/images/bocchi.jpg",
    "./assets/images/bocchi2.jpg",
    "./assets/images/momo.jpg",
    "./assets/images/momo2.jpg",
]
const createNumber = (min, max) => ~~(Math.random() * (max - min + 1) + min);

const tableRowClick = (evt) => {

    if(evt.target.tagName.toLowerCase().match("button|i")) return
    const target = evt.currentTarget;
    // convert to jQuery for the usage of slideUp /Down
    const pTag = $(target.nextSibling);

    $(pTag).is(":visible") ? $(pTag).slideUp('fast') : $(pTag).slideDown('fast')

}

const addToCartClick = (evt) => {
    // first parent is the td, second parent is the tr
    const tr = evt.currentTarget.parentElement.parentElement;
    const articleId = Number(tr.querySelector("#articleId").innerText)
    const article = elements.tableData.filter(article => article.id == articleId)
    addToCard(article[0])
}

const addToCartButton = (tr, head) => {
    /** 
 * Takes the current row (if not the head) and adds the to cart button
 * @tr {domObject} the current table row we want to fill / add
 * @head {bool}  determines if head or body element 
 * */
    if (head) {
        tr.append(document.createElement("th"))

        return
    };

    const td = document.createElement("td")
    const btn = document.createElement("button")
    const iTag = document.createElement("i")
    td.style.textAlign = "center";
    iTag.classList.add("fa")
    iTag.classList.add("fa-shopping-cart")
    btn.classList.add("addtocartBtn")
    btn.addEventListener("click", addToCartClick)

    btn.append(iTag)
    td.append(btn)
    tr.append(td)

}

const addCover = (tr, td, data, tableElement) => {
    /** 
     * Adding a cover to the info Box
     *  
     * @tr {domObject} the current table row we want to fill / add to
     * @td {domObject} the currend td, with colSpan = header items
     * @data {object} the data object like an article i.e. {"artist" : "a artist", "year": "a year"}
     * @tableElement {domObject} the element where to append the row to(tableHead/tableBody)
    */
    const infoContainer = document.createElement('div')
    infoContainer.classList.add("infoDiv");
    const img = document.createElement("img")

    // for now, random image from an array, later on from the data object
    img.src = elements.images[createNumber(0, elements.images.length - 1)]
    img.alt = "alt"
    img.classList.add("cover")
    infoContainer.classList.add("infoDiv")
    infoContainer.append(img)
    td.append(infoContainer)
    tr.append(td)
    tableElement.append(tr)
}

const addTrackInfo = (tr, td, data, tableElement) => {
    /** 
     * Iterate the element.tracks objects and add them to a table row that will be appended
     * after the actual row is appended
     *  
     * @tr {domObject} the current table row we want to fill / add to
     * @td {domObject} the currend td, with colSpan = header items
     * @data {object} the data object like an article i.e. {"artist" : "a artist", "year": "a year"}
     * @tableElement {domObject} the element where to append the row to(tableHead/tableBody)
    */

    const infoContainer = document.createElement('div')
    const trackList = document.createElement('ul')

    infoContainer.classList.add("infoDiv")
    data.tracks.forEach(track => {
        const liTrack = document.createElement("li")
        liTrack.innerText = `${track.title} (${track.length})`
        trackList.append(liTrack)
    })

    infoContainer.append(trackList)
    td.append(infoContainer)
    tr.append(td)
    tableElement.append(tr)

}

const addVendorInfo = (tr, td, data, tableElement) => {
    /** 
     * Iterate the element.tracks objects and add them to a table row that will be appended
     * after the actual row is appended
     *  
     * @tr {domObject} the current table row we want to fill / add to
     * @td {domObject} the currend td, with colSpan = header items
     * @data {object} the data object like an article i.e. {"artist" : "a artist", "year": "a year"}
     * @tableElement {domObject} the element where to append the row to(tableHead/tableBody)
    */
    const infoContainer = document.createElement('div')
    infoContainer.classList.add("infoDiv")
    infoContainer.innerText = "todo: Händerfreude"
    td.append(infoContainer)
    tr.append(td)
    tableElement.append(tr)
}

const addRowToTable = ({ tr, data, head = false, tableElement } = {}) => {
    /** 
     * Iterates over the given table row 
     * @tr {domObject} the current table row we want to fill / add
     * @data {object} the data object like an article i.e. {"artist" : "a artist", "year": "a year"}
     * @head {bool}  determines if head or body element
     * @tableElement {domObject} the element where to append the row to(tableHead/tableBody)
    */
    tr.addEventListener('click', tableRowClick)

    for (const [key, value] of Object.entries(data)) {
        // Ignore relationships like the genre
        if (typeof value == 'object') continue;
        if (key.match('state')) continue;

        const thtd = document.createElement(head ? "th" : "td");

        if (key.match('id')) {
            thtd.hidden = true;
            thtd.id = "articleId"
        } 

        thtd.innerHTML = head ? key : value

        tr.append(thtd);
        tableElement.append(tr);
    }

    addToCartButton(tr, head)

    // InfoRow:
    // Add the tracklist and maybe other information to an slidable
    // <p> tag
    const infoRow = document.createElement('tr')
    infoRow.classList.add("infoTr")
    const td = document.createElement('td')
    td.colSpan = elements.colspan;
    infoRow.hidden = true

    if (!head) addCover(infoRow, td, data, tableElement)
    if (!head) addTrackInfo(infoRow, td, data, tableElement)
    if (!head) addVendorInfo(infoRow, td, data, tableElement)
}

const filterData = (filterArr, tableData) => {
    /** 
     * A function for article filter purposes.
     * First, iterate over the articles via filter, check if article has a genre.
     * If this is the case, check if the filters array includes the genre name
     * Filter genre and sub genre aswell
    */

    return filterArr.length ? tableData.filter(article => {
        const ret = 0;
        return article.genres.some(genre => {
            return filterArr.some(filter => {
                if (genre.genre.name == filter) return true
                return false;
            });
        }) || article.sub_genres.some(sub_genre => {
            return filterArr.some(filter => {
                if (sub_genre.sub_genre.name == filter) return true
                return false;
            });
        })
    }) : tableData

}


const removeElements = (el) => {
    while (el.firstChild) {
        el.removeChild(el.firstChild);
    }
}

const addRowAmount = (tableHead, tableBody, tableFoot, tableData, filter, tr) => {
    const tdLeft = document.createElement("td")
    tdLeft.colSpan = Math.floor(elements.colspan / 2);
    tdLeft.classList.add("tableBtnLeft")
    tr.append(tdLeft)

    // Displayed row amount:
    // iterate over the row amounts array (how many rows are displayed in the table)
    // for each entrie, add an button + event listener
    elements.rowAmounts.forEach(value => {
        const tableBtn = document.createElement('button')
        tableBtn.innerText = value
        tableBtn.addEventListener('click', (event) => {
            // set the new row amount 
            elements.currentRowAmount = Number(event.target.innerText)
            // also reset the page
            elements.page = 1
            table(tableHead, tableBody, tableFoot, tableData, filter)
        })
        tdLeft.append(tableBtn)
    })
}

const addPagination = (tableHead, tableBody, tableFoot, tableData, filter, tr) => {
    const tdRight = document.createElement("td")
    tdRight.colSpan = Math.ceil(elements.colspan / 2);
    tdRight.classList.add("tableBtnRight")
    tr.append(tdRight)

    // Pagination:
    // First, get the pagination amount by dividing the tabledata with the current amount of displayed
    // items. 
    // Use ceil to allways round up
    const paginationAmount = Math.ceil(tableData.length / elements.currentRowAmount)
    for (let i = 1; i <= paginationAmount; i++) {
        // create the pagination buttons and add them to the right column of the 
        // table footer element
        const paginationBtn = document.createElement('button')
        paginationBtn.innerText = i
        paginationBtn.addEventListener('click', (event) => {
            elements.pagination = Number(event.target.innerHTML)

            elements.page = Number(event.target.innerHTML)
            //render table again, but only use the data from the given page
            table(tableHead, tableBody, tableFoot, tableData, filter)
        })
        tdRight.append(paginationBtn)
    }
    tableFoot.append(tr)
}

const addTableFooter = (tableHead, tableBody, tableFoot, tableData, filter) => {
    // create a new table row first, and place the buttons within the row later on
    const tr = document.createElement("tr");


    // What we also need to do is setting the coolspan.
    // this way we can make sure that the buttons in the footer 
    // are in the correct place aka the row amount buttons left,
    // the pagination right, since we have only 2 rows over the whole table this way.

    // the buttons for the table amount (display 5,10,xx at once)
    tr.classList.add("foot")
    addRowAmount(tableHead, tableBody, tableFoot, tableData, filter, tr)
    addPagination(tableHead, tableBody, tableFoot, tableData, filter, tr)

}

const table = (tableHead, tableBody, tableFoot, tableData, filterArr) => {
    /** 
     * Appends a table to a table head / body tag, and fills the table with the given data
     * 
     * @tabbleHead {domElement} the table head where the table should be append to
     * @tableBody {domElement} the table body element where the table should be append to
     * @tableFooter {domElement} the table footer element where the table should be append to
     * @tableData {Array[dict]} the data to fill the table
     * @filter {Array} the data to fill the table
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
    removeElements(tableHead);
    removeElements(tableBody);
    removeElements(tableFoot);
    elements.tableData = tableData;

    let count = 0;
    const filteredData = filterData(filterArr, tableData)

    // calcualte the displayed data, since we only need to iterate over the data we want to display
    // Data depends on the page and row amount displayed
    const from = (elements.page - 1) * elements.currentRowAmount
    const to = elements.page * elements.currentRowAmount
    const pageData = filteredData.slice(from, to)

    for (const article of pageData) {
        // only render the amount the user has set
        if (count == elements.currentRowAmount) break
        if (!count) {
            const tr = document.createElement("tr");
            addRowToTable({ tr, data: article, head: true, tableElement: tableHead })
            // set the max cols we have in the table
            elements.colspan = tableHead.rows[0].cells.length;
        }
        const tr = document.createElement("tr");

        addRowToTable({ tr, data: article, head: false, tableElement: tableBody })
        count++;
    }
    addTableFooter(tableHead, tableBody, tableFoot, filteredData, filterArr)
}



export { table };
const rowAmounts = [5,10,25]
const currentRowAmount = [10]

const addToTable = ({ tr, tableRow, head = false , tableElement} = {}) => {
    /** 
     * Iterates over the given table row 
     * @tr {tableRow} 
     * @tableRow {object} 
     * @head {bool}  
    */
    for (const [key, value] of Object.entries(tableRow)) {
        // Ignore relationships like the genre and ignore the article id also
        if (typeof value =='object') continue;
        if (key.match('id')) continue;

        const thtd = document.createElement(head ? "th" : "td");
        thtd.innerHTML = head ? key : value
        tr.append(thtd);
        tableElement.append(tr);
    }
}

const filterData = (filterArr, tableData) => {
    /** 
     * A function for article filter purposes.
     * First, iterate over the articles via filter, check if article has a genre.
     * If this is the case, check if the filters array includes the genre name
     * Filter genre and sub genre aswell
    */
    
    return filterArr.length ? tableData.filter(article =>{
        const ret = 0;
        return article.genres.some(genre => {
            return filterArr.some(filter => {
                if (genre.genre.name == filter) return true
                return false;
            }) ;
        }) || article.sub_genres.some(sub_genre => {
            return filterArr.some(filter => {
                if (sub_genre.sub_genre.name == filter) return true
                return false;
            });
        }) 
    } ) : tableData

}


const removeElements = (el) => {
    while (el.firstChild) {
        el.removeChild(el.firstChild);
    }
}


const addTableFooter = (tableHead, tableBody, tableData, filter) => {
    // the buttons for the table amount (display 5,10,xx at once)
    // create a new table row first, and place the buttons within the row
    const tr = document.createElement("tr");
    rowAmounts.forEach(value => {
        const tableBtn = document.createElement('button')

        tableBtn.innerText = value
        tableBtn.addEventListener('click', (event) => {
            currentRowAmount.pop()
            currentRowAmount.push(Number(event.target.innerText))
            console.log("?");
            table(tableHead, tableBody, tableData, filter)
        })
        tr.append(tableBtn)
        tableBody.append(tr)
    })
    
}

const table = (tableHead, tableBody, tableData, filterArr) => {
    /** 
     * Appends a table to a table head / body tag, and fills the table with the given data
     * 
     * @tabbleHead {domElement} the table head where the table should be append to
     * @tableBody {domElement} the table body element where the table should be append to
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
    let tr = document.createElement("tr");
    let count = 0;
    for (const article of filterData(filterArr,tableData)) {
        // only render the amount the user has set
        if (count == currentRowAmount[0]) break
        if (!count) {
            addToTable({ tr, tableRow: article, head: true, tableElement: tableHead})
        }
        tr = document.createElement("tr");

        addToTable({ tr, tableRow: article, head: false, tableElement: tableBody })
        count ++;
    }
    addTableFooter(tableHead, tableBody, tableData, filterArr)
}



export { table, rowAmounts, currentRowAmount };
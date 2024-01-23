import React from 'react';
import './Filter.css'
import { CheckBox } from '../CheckBox/CheckBox.js'

export function Filter({ genre, subGenre, filterList, setFilterList }) {

    function handleOnChange(event, item) {
        const itemId = filterList.indexOf(item)
        item.isChecked = !(item.isChecked)
        // add item if it doesn't allready exist in the array, and the item state is checked
        // remove an item from the filter list if item is not checked and doesn't exist
        // We need a copy so a change will be detected by the setFilterList method from the app.js
        const newFilter = [...filterList]
        itemId === -1 && item.isChecked ? newFilter.push(item) : newFilter.splice(itemId, 1);
        setFilterList(newFilter)
    };

    return (
        <div className="Filter">
            <CheckBox list={genre} type={"genre"} onChange={handleOnChange} />
            <CheckBox list={subGenre} type={"subGenre"} onChange={handleOnChange} />
        </div>
    )

}


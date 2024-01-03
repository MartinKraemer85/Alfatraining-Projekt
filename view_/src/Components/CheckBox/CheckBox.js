import React from 'react';
import "./CheckBox.css"
const CheckBox = ({ list, type, onChange }) => {

    return (
        <fieldset>
            <legend>{type}</legend>
            {list?.map((item, index) => (
                <div key={type + "_" + index} className='CheckBox'>
                    <input
                        style={{ fontStyle: "normal" }}
                        type="checkbox"
                        checked={item.isAdded}
                        onChange={e => onChange(e, item)}
                    />
                    <label htmlFor={item.name}>
                        {item.name}
                    </label>
                </div>
            ))}
        </fieldset>
    );
};
export { CheckBox };
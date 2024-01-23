import './UserProfile.css';
import React, { useState, useEffect } from 'react';
import { post } from '../../helper/CRUD.js';

export function UserProfile() {

    const [formData, setFormData] = useState({
        id: -1, username: "", pwd: "",
        first_name: "", last_name: "", mail: ""
    });

    useEffect(() => {
        post({
            url: "/select",
            body: {
                "table": "customer",
                "fields": ["*"],
                "where": "where first_name = 'Bertram'"
            }
        }).then(res => res.json()
        ).then(data => {
            setFormData(...data)
        })
        // Line 26:8:  React Hook useEffect has a missing dependency: 'formData'. Either include it or remove the dependency array
        // with this useEffect we set the formData. If we add formData to the dependency array, it will loop endlessly
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    function handleClick(e) {

        post({
            url: "/update_customer",
            body: {
                "objectPath": "Model.CustomerDetails.Customer.Customer",
                "attributes": {
                    "id": formData.id,
                    "pwd": formData.pwd,
                    "first_name": formData.first_name,
                    "last_name": formData.last_name,
                    "mail": formData.mail
                }
            }
        }).then(res => console.log(res.status))
    }

    return (
        <div className="UserProfile">
            <form className='profile-form' >
                <p><b>Hello {formData.username}!</b> </p>
                <label htmlFor="fname">First Name</label>
                <input type="text" id="fname" name="firstname" required
                    value={formData.first_name}
                    onChange={(e) => setFormData({ ...formData, first_name: e.target.value })} />

                <label htmlFor="lname">Last Name</label>
                <input type="text" id="lname" name="lastname" required
                    value={formData.last_name}
                    onChange={(e) => setFormData({ ...formData, last_name: e.target.value })} />

                <label htmlFor="mail">Mailadress</label>
                <input type="text" id="mail" name="mail" required
                    value={formData.mail}
                    onChange={(e) => setFormData({ ...formData, mail: e.target.value })} />

                <label htmlFor="subject">Password</label>
                <input type="text" id="pwd" name="pwd" required
                    value={formData.pwd}
                    onChange={(e) => setFormData({ ...formData, pwd: e.target.value })} />

                <input type="Submit" value={"Save"} onClick={handleClick} readOnly />
            </form>
        </div>

    )
}

import './UserProfile.css';
import React, { useState, useEffect } from 'react';
import { post } from '../../helper/CRUD.js';

const UserProfile = () => {

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
            console.log(formData);
        })
        // Line 26:8:  React Hook useEffect has a missing dependency: 'formData'. Either include it or remove the dependency array
        // with this useEffect we set the formData. If we add formData to the dependency array, it will loop endlessly
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    const handleClick = (e) => {
        console.log(formData);
        e.preventDefault()
    }

    return (
        <div className="UserProfile">
            <form className='profile-form' >
                <p><b>Hallo {formData.username}</b> </p>
                <label htmlFor="fname">First Name</label>
                <input type="text" id="fname" name="firstname"
                    value={formData.first_name}
                    onChange={(e) => setFormData({ ...formData, firstName: e.target.value })} />

                <label htmlFor="lname">Last Name</label>
                <input type="text" id="lname" name="lastname"
                    value={formData.last_name}
                    onChange={(e) => setFormData({ ...formData, lastname: e.target.value })} />

                <label htmlFor="mail">Mailadress</label>
                <input type="text" id="mail" name="mail"
                    value={formData.mail}
                    onChange={(e) => setFormData({ ...formData, mail: e.target.value })} />

                <label htmlFor="subject">Subject</label>
                <input type="text" id="pwd" name="pwd"
                    value={formData.pwd}
                    onChange={(e) => setFormData({ ...formData, subject: e.target.value })} />

                <input type="Submit" value={"Save"} onClick={handleClick}></input>
            </form>
        </div>

    )
}

export { UserProfile };
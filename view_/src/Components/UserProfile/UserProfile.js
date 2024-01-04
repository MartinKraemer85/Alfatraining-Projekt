import './UserProfile.css';
import React, { useState, useEffect } from 'react';
import { post } from '../../helper/CRUD.js';

const UserProfile = () => {

    const [formData, setFormData] = useState({ lastname: "", firstName: "", mail: "", subject: "", issue: "" });

    return (
        <div className="Contact">
            <form className='contact-form' >
                <label htmlFor="fname">First Name</label>
                <input type="text" id="fname" name="firstname" placeholder="Name (*)"
                    value={formData.firstName}
                    onChange={(e) => setFormData({ ...formData, firstName: e.target.value })} />

                <label htmlFor="lname">Last Name</label>
                <input type="text" id="lname" name="lastname" placeholder="Last name (*)"
                    value={formData.lastname}
                    onChange={(e) => setFormData({ ...formData, lastname: e.target.value })} />

                <label htmlFor="mail">Mailadress</label>
                <input type="text" id="mail" name="lastname" placeholder="Subject (*)"
                    value={formData.mail}
                    onChange={(e) => setFormData({ ...formData, mail: e.target.value })} />

                <label htmlFor="subject">Subject</label>
                <input type="text" id="subject" name="lastname" placeholder="Subject (*)"
                    value={formData.subject}
                    onChange={(e) => setFormData({ ...formData, subject: e.target.value })} />


                <label htmlFor="issue">Issue</label>
                <textarea id="issue" name="issue" placeholder="Your issue (*)"
                    value={formData.issue}
                    onChange={(e) => setFormData({ ...formData, issue: e.target.value })} />
                <input type="Submit"></input>
            </form>
        </div>

    )
}

export { UserProfile };
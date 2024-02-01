import './Contact.css';
import React, { useState } from 'react';
import { post } from '../../helper/CRUD.js';

export function Contact() {

    const [formData, setFormData] = useState({ lastname: "", firstName: "", mail: "", subject: "", issue: "" });

    function handleSubmit(e) {
        console.log(formData.firstName);
        post({
            url: "/mail",
            body: {
                "first_name": String(formData.firstName),
                "last_name": String(formData.lastname),
                "mail_address": String(formData.mail_address),
                "subject": String(formData.subject),
                "issue": String(formData.issue)
            }
        }).then(res => { console.log(res.status) }// hier was machen wenn fehler
        )

    }

    return (
        <div className="Contact">
            <form className='contact-form' onSubmit={(e) => handleSubmit(e)}>
                <label htmlFor="fname">First Name</label>
                <input type="text" id="fname" name="firstname" placeholder="Name (*)" required
                    value={formData.firstName}
                    onChange={(e) => setFormData({ ...formData, firstName: e.target.value })} />

                <label htmlFor="lname">Last Name</label>
                <input type="text" id="lname" name="lastname" placeholder="Last name (*)" required
                    value={formData.lastname}
                    onChange={(e) => setFormData({ ...formData, lastname: e.target.value })} />

                <label htmlFor="mail">Mailadress</label>
                <input type="text" id="mail" name="mail" placeholder="Subject (*)" required
                    value={formData.mail}
                    onChange={(e) => setFormData({ ...formData, mail: e.target.value })} />

                <label htmlFor="subject">Subject</label>
                <input type="text" id="subject" name="subject" placeholder="Subject (*)" required
                    value={formData.subject}
                    onChange={(e) => setFormData({ ...formData, subject: e.target.value })} />


                <label htmlFor="issue">Issue</label>
                <textarea id="issue" name="issue" placeholder="Your issue (*)" required
                    value={formData.issue}
                    onChange={(e) => setFormData({ ...formData, issue: e.target.value })} />
                <input type="Submit" value={"Send"} readOnly />
            </form>
        </div>
    )
}

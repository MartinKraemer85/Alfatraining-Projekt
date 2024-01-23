import React, { useState, useContext } from 'react';
import { post } from '../../../helper/CRUD';
import { GenreContext } from '../../../contexts/genre';
import Select from 'react-select'

export function AddArticle() {
    const { genre, subGenre } = useContext(GenreContext)
    const currentYear = new Date().getFullYear();

    const [formData, setFormData] = useState({
        "objectPath": "Model.Vinyl.Record.Record",
        "title": "",
        "artist": "test",
        "type": "Vinyl",
        "year": "",
        "state": 0,
        "price": 0,
        "Model.Vinyl.Track.Track": [
            { "track_number": 1, "title": "track1", "length": "5:23" },
            { "track_number": 2, "title": "track2", "length": "5:23" },
            { "track_number": 3, "title": "track3", "length": "5:23" },
        ],
        "Model.Vinyl.Associations.AscGenre": [
        ],
        "Model.Vinyl.Associations.AscSubGenre": [
        ]
    });

    function handleClick(e) {
        post({
            url: "/add_article",
            body: {
                "objectPath": formData.objectPath,
                "attributes": {
                    "title": formData.title,
                    "artist": formData.artist,
                    "type": formData.type,
                    "year": formData.year,
                    "state": formData.state,
                    "price": formData.price,
                    "Model.Vinyl.Track.Track": formData['Model.Vinyl.Track.Track'],
                    "Model.Vinyl.Associations.AscGenre": formData['Model.Vinyl.Associations.AscGenre'].map(e => {
                        return { "genre_id": e.value }
                    }),
                    "Model.Vinyl.Associations.AscSubGenre": formData['Model.Vinyl.Associations.AscGenre'].map(e => {
                        return { "sub_genre_id": e.value }
                    }),
                }
            }
        }).then(res => console.log(res))
    }

    function createOptions(arr) {
        return arr.map((el) => {
            return { "value": el.id, "label": el.name }
        })
    }

    return (
        <>
            <div className="UserProfile">
                <form className='profile-form' >
                    <label htmlFor="artist">Artist</label>
                    <input type="text" id="artist" name="artist" required
                        value={formData.artist}
                        onChange={(e) => setFormData({ ...formData, artist: e.target.value })} />

                    <label htmlFor="title">Album Title</label>
                    <input type="text" id="title" name="title" required
                        value={formData.title}
                        onChange={(e) => setFormData({ ...formData, title: e.target.value })} />

                    <label htmlFor="type">Type</label>
                    <input type="text" id="type" name="type" required
                        value={formData.type}
                        onChange={(e) => setFormData({ ...formData, type: e.target.value })} readOnly />

                    <label htmlFor="year">Year (1900-{currentYear})</label>
                    <input type="number" min="1900" max={String(currentYear)} id="year" name="year" required
                        value={formData.year}
                        onChange={(e) => setFormData({ ...formData, year: e.target.value })} />

                    <label htmlFor="state">State (0-5)</label>
                    <input type="number" min="0" max="5" id="state" name="state" required
                        value={formData.state}
                        onChange={(e) => setFormData({ ...formData, state: e.target.value })} />

                    <label htmlFor="price">Price</label>
                    <input type="number" min="0" id="price" name="price" required placeholder="0.00" step="0.01" pattern="^\d+(?:\.\d{1,2})?$"
                        value={formData.price}
                        onChange={(e) => setFormData({ ...formData, price: e.target.value })} />

                    <label htmlFor="genre">Genre</label>
                    <Select id="genre" options={createOptions(genre)} isMulti required
                        onChange={(e) => formData['Model.Vinyl.Associations.AscGenre'] = (e)} />

                    <label htmlFor="subGenre">Sub Genre</label>
                    <Select id="subGenre" options={createOptions(subGenre)} isMulti required
                        onChange={(e) => formData['Model.Vinyl.Associations.AscSubGenre'] = (e.value)} />

                    <input id="subGenre" type="Submit" value={"Save"} onClick={handleClick} readOnly
                    />

                </form>
            </div>
        </>
    )
}

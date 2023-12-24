const Tracks = props => {

    const createTrackList = (data) => data.map((tracks, index) => <li key={index}>{tracks.title}:{tracks.length}</li>)

    return (

        <div className="Info">
            <h2> Tracks</h2>
            <ul>
                {createTrackList(props.content)}
            </ul>
        </div>


    )

}

export { Tracks }
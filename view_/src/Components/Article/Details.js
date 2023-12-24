const Details = props => {
    const getGenre = (genres) => genres.map((genres) => genres.genre.name)
    const getSubGenre = (genres) => genres.map((genres) => genres.sub_genre.name)

    const genre = props.content.genres
    const subGenre = props.content.sub_genres

    return (
        <>
            <h1>{props.content.artist}</h1>
            <p>Release: {props.content.year} </p>
            <p>Genre(s): {genre ? getGenre(genre).join(",") : ""} </p>
            <p>Sub Genre(s): {subGenre ? getSubGenre(subGenre).join(",") : ""}</p>
        </>
    )

}

export { Details }
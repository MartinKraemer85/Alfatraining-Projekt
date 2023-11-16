
const get = ({  url = "/",
                method = "post",
                headers = { 'content-type': 'application/json' },
                body = {} } = {}) => {
    const json = JSON.stringify(body);
    fetch(url, {
        method: method,
        headers: headers,
        body: json
    }).then(
        res => res.json()
    ).then(
        (json) => { console.log(json); }
    ).catch(
        console.log
    )
}


// exporting variables and function
export { get };
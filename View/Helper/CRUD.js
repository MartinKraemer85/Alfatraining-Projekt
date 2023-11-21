
const get = async ({ url = "/",
    method = "post",
    headers = { 'content-type': 'application/json' },
    body = {} } = {}) => {

    const response = await fetch(url, {
        method: method,
        headers: headers,
        body: JSON.stringify(body)
    })
    const json = await response.json()
    console.log(json)
    return json;
}



// exporting variables and function
export { get };
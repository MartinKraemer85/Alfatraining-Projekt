const Crud = {
    get: ({
        url = "/",
        headers = {
            'content-type': 'application/json',
            'Accept': 'application/json'
        },
    } = {}) => {
        return fetch(url, {
            method: "get",
            head: headers,
        })
    },
    post: ({
        url = "/",
        headers = {
            'content-type': 'application/json',
            'Accept': 'application/json'
        },
        body
    } = {}) => {
        return fetch(url, {
            method: "post",
            headers: headers,
            body: JSON.stringify(body),
        })
    },
}

export default Crud;
export const get = Crud.get;
export const post = Crud.post;
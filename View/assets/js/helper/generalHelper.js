'use strict';

const createNumber = (min, max) => ~~(Math.random() * (max - min + 1) + min);

const getCurrentRowAmount = () => {
    const rowAmount = Number(localStorage.getItem('currentRowAmount'))
    if (!rowAmount) return 10
    return rowAmount
}

const getCurrentPage = () => {
    const page = Number(localStorage.getItem('currentPage'))
    console.log(page);
    if (!page) return 1
    return page
}

const setLocalStorage = ({ key = 'currentRowAmount', value = 10 }) => {
    console.log("value:", value);
    console.log("key:", key);
    localStorage.setItem(key, value)
}

export { createNumber, getCurrentRowAmount, setLocalStorage, getCurrentPage }
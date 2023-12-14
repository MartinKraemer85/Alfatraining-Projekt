'use strict';

const createNumber = (min, max) => ~~(Math.random() * (max - min + 1) + min);

const getCurrentRowAmount = () => {
    const rowAmount = Number(localStorage.getItem('currentRowAmount'))
    if (!rowAmount) return 10
    return rowAmount
}

export { createNumber, getCurrentRowAmount }
'use strict';

const dom = {
    create({
        content = '',
        type = 'div',
        parent = false,
        classes = [],
        attr = {},
        listeners = {},
        styles = {},
        append = true,
    } = {}) {
        let element = document.createElement(type);
        if (content) element.innerHTML = content;
        if (classes.length) element.className = classes.join(' ');

        Object.entries(attr).forEach(el => element.setAttribute(...el));
        Object.entries(listeners).forEach(el => element.addEventListener(...el));
        Object.entries(styles).forEach(style => element.style[style[0]] = style[1]);

        if (parent) {
            if (!append) parent.prepend(element);
            else parent.append(element);
        }

        return element;
    },
    $(selector) {
        return document.querySelector(selector);
    },
    $$(selector) {
        return [...document.querySelectorAll(selector)];
    },
}

export { dom }
export let create = dom.create
export let $ = dom.$
export let $$ = dom.$$
'use strict';
import { get } from "../helper/CRUD.js";
import { elements } from "../settings.js";

onmessage = () => {
    elements.allArticles = get({
        url: "http://192.168.0.2:5000/select_all_articles"
    })
    // Um zwischen progress und done unterscheiden zu können, müssen wir die Nachrichten markieren
    self.postMessage(2);
}
/** @odoo-module */
import { Component, useState } from "@odoo/owl";

export class Content extends Component {
    static template = "my_owl_new.Content";

    setup(){
        this.state = useState({count:0});
    }

    increment(){
        this.state.count++
    }

    reset(){
        this.state.count = 0
    }
}

/** @odoo-module */
import { Component } from "@odoo/owl";
import { Header } from "./components/header";
import { Content } from "./components/content";
import { Footer } from "./components/footer";

export class Root extends Component {
    static template = "my_owl_new.Root";
    static components = { Header, Content, Footer };
}
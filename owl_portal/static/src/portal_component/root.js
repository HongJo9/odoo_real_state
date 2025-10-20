/** @odoo-module */
import { Component } from "@odoo/owl";
// Importas el registro global de Odoo
import { registry } from "@web/core/registry"

export class Root extends Component {
    static template = "owl_portal.Root";
    static props = {};
}

registry.category("public_components").add("owl_portal.Root", Root);
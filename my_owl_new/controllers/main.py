from odoo.http import request, route, Controller

class MyOwlNewController(Controller):
    @route("/my_owl_new/standalone_app", auth="public")
    def standalone_app(self):
        return request.render(
            'my_owl_new.standalone_app',
            {
                'session_info': request.env['ir.http'].get_frontend_session_info(),
            }
        )
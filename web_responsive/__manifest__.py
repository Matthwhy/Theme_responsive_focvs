

{
    "name": "Theme Responsive FOCVS",
    "summary": "Responsive web client, community-supported",
    "version": "16.0.1.2.10",
    "category": "Website",
    "website": "https://github.com/OCA/web",
    "author": "LasLabs, Tecnativa, ITerra, Onestein,Matheus Marques"
    "Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "installable": True,
    "depends": ["web", "mail"],
    "development_status": "Production/Stable",
    "maintainers": ["Tardo", "SplashS"],
    "excludes": ["web_enterprise"],
    "assets": {
        "web.assets_backend": [
            "/web_responsive/static/src/views/form/form_controller.esm.js",
            "/web_responsive/static/src/legacy/scss/web_responsive.scss",
            "/web_responsive/static/src/legacy/js/web_responsive.js",
            "/web_responsive/static/src/components/ui_context.esm.js",
            "/web_responsive/static/src/components/apps_menu/apps_menu.scss",
            "/web_responsive/static/src/components/apps_menu/apps_menu.esm.js",
            "/web_responsive/static/src/components/control_panel/control_panel.scss",
            "/web_responsive/static/src/components/control_panel/control_panel.esm.js",
            "/web_responsive/static/src/components/search_panel/search_panel.scss",
            "/web_responsive/static/src/components/search_panel/search_panel.esm.js",
            "/web_responsive/static/src/components/hotkey/hotkey.scss",
            "/web_responsive/static/src/legacy/xml/form_buttons.xml",
            "/web_responsive/static/src/components/apps_menu/apps_menu.xml",
            "/web_responsive/static/src/components/control_panel/control_panel.xml",
            "/web_responsive/static/src/components/search_panel/search_panel.xml",
            "/web_responsive/static/src/components/hotkey/hotkey.xml",
            "/web_responsive/static/src/components/chatter_topbar/chatter_topbar.esm.js",
            "/web_responsive/static/src/components/chatter_topbar/chatter_topbar.xml",
            "/web_responsive/static/src/components/attachment_viewer/attachment_viewer.scss",
            "/web_responsive/static/src/components/attachment_viewer/attachment_viewer.esm.js",
            "/web_responsive/static/src/components/attachment_viewer/attachment_viewer.xml",
            "/web_responsive/static/src/views/form/form_controller.scss",
        ],
        'web.assets_frontend':[
             '/web_responsive/static/src/legacy/scss/web_responsive.scss'
         ],
        "web.assets_tests": [
            "/web_responsive/static/tests/test_patch.js",
        ],
    },
    "sequence": 1,
}

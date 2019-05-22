from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from nva.footerviewlet.interfaces import IFooterSettingsSchema
from plone.z3cform import layout
from z3c.form import form

class FooterControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IFooterSettingsSchema

FooterControlPanelView = layout.wrap_form(FooterControlPanelForm, ControlPanelFormWrapper)
FooterControlPanelView.label = u"Footer Einstellungen"

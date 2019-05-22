# -*- coding: utf-8 -*-
from zope.component import getUtility
from plone.app.layout.viewlets import ViewletBase
from plone.registry.interfaces import IRegistry
from nva.footerviewlet.interfaces import IFooterSettingsSchema

class FooterViewlet(ViewletBase):

    def update(self):
        self.footercontent = self.get_footercontent()

    def get_footercontent(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IFooterSettingsSchema)
        return settings.footercontent

    def render(self):
        return super(FooterViewlet, self).render()

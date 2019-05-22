# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.interface import Interface
from zope.schema import Text

class INvaFooterviewletLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

class IFooterSettingsSchema(Interface):

    footercontent = Text(title=u'Inhalt des Footers',
                         description=u'Bitte tragen Sie hier den Inhalt des Footers als <HTML> ein.')


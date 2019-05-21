# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import nva.footerviewlet


class NvaFooterviewletLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=nva.footerviewlet)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'nva.footerviewlet:default')


NVA_FOOTERVIEWLET_FIXTURE = NvaFooterviewletLayer()


NVA_FOOTERVIEWLET_INTEGRATION_TESTING = IntegrationTesting(
    bases=(NVA_FOOTERVIEWLET_FIXTURE,),
    name='NvaFooterviewletLayer:IntegrationTesting',
)


NVA_FOOTERVIEWLET_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(NVA_FOOTERVIEWLET_FIXTURE,),
    name='NvaFooterviewletLayer:FunctionalTesting',
)


NVA_FOOTERVIEWLET_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        NVA_FOOTERVIEWLET_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='NvaFooterviewletLayer:AcceptanceTesting',
)

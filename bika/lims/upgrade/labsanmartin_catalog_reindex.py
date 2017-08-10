from Acquisition import aq_inner
from Acquisition import aq_parent
import sys
import traceback
from Products.CMFCore.utils import getToolByName
import transaction
from plone.api.portal import get_tool
from bika.lims.catalog import CATALOG_WORKSHEET_LISTING
from bika.lims import logger
from bika.lims.upgrade.utils import UpgradeUtils
from bika.lims.upgrade.v3_2_0_1706 import fix_ar_analyses_statuses_inconsistences

product = 'bika.lims'
version = '3.2.0.1707'
def upgrade(tool):
    portal = aq_parent(aq_inner(tool))
    ut = UpgradeUtils(portal)


    logger.info("Running upgrade for Labsanmartin")

    # Renames some guard expressions from several transitions
    # worksheet_catalog(portal)
    #logger.info("Updating role mappings...")
    #wf = get_tool('portal_workflow')
    #wf.updateRoleMappings()
    fix_ar_analyses_statuses_inconsistences(portal)
    return True


def worksheet_catalog(portal):
    catalog = getToolByName(portal, CATALOG_WORKSHEET_LISTING)
    logger.info('Soft cleaning and rebuilding %s...' % catalog.id)
    at = getToolByName(portal, 'archetype_tool')
    try:
        types = [k for k, v in at.catalog_map.items()
                 if catalog.id in v]
        counter = 0
        catalog.manage_catalogClear()
        # Getting UID catalog
        uid_c = getToolByName(portal, 'uid_catalog')
        brains = uid_c(portal_type=types)
        total = len(brains)
        for brain in brains:
            obj = brain.getObject()
            catalog.catalog_object(
                obj, idxs=catalog.indexes(),
                update_metadata=True)
            counter += 1
            if counter % 100 == 0:
                logger.info(
                    'Progress: {}/{} objects have been cataloged for {}.'
                        .format(counter, total, catalog.id))
                if counter % 1000 == 0:
                    transaction.commit()
                    logger.info(
                        '{0} items processed.'
                            .format(counter))
        transaction.commit()
        logger.info(
            '{0} items processed.'
                .format(counter))
    except:
        logger.error(traceback.format_exc())
        e = sys.exc_info()
        logger.error(
            "Unable to clean and rebuild %s due to: %s" % (catalog.id, e))
    logger.info('%s cleaned and rebuilt' % catalog.id)

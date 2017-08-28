from Products.Archetypes.Registry import registerWidget
from AccessControl import ClassSecurityInfo
from . import SelectionWidget

class PrioritySelectionWidget(SelectionWidget):
    """
    Displays a Selection List, but with styled options in accordance with the
    Priority value selected
    """
    _properties = SelectionWidget._properties.copy()
    security = ClassSecurityInfo()

registerWidget(PrioritySelectionWidget)

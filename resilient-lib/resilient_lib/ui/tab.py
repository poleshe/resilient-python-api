from .common import get_incident_tabs
import six

TABS_LABEL = "step_label"

UI_TAB_ELEMENT = "tab"
UI_TAB_FIELD_TYPE = "incident"

class RequiredTabFields(type):
    def __init__(cls, name, bases, attrs):
        if not bases:
            return  # No bases implies Tab, which doesn't need to define the properties
        for attr in ["UUID", "NAME", "SECTION", "CONTAINS"]:
            if not hasattr(cls, attr) or getattr(cls, attr) is None:
                raise AttributeError("{} is missing from class definition of a Tab".format(attr))
    

class Tab(six.with_metaclass(RequiredTabFields)):
    UUID = None
    NAME = None
    SECTION = None
    

    CONTAINS = None

    @classmethod
    def exists(cls, client):
        """
        Check if the tab exists in Resilient
        """
        return cls.exists_in(get_incident_tabs(client))

    @classmethod
    def exists_in(cls, tabs):
        """
        Checks if the tab exists in the list of tabs.
        """
        return cls.get_from_tabs(tabs) is not None

    @classmethod
    def get_from_tabs(cls, tabs):
        return next((x for x in tabs if x.get("predefined_uuid") == cls.UUID), None)

    @classmethod
    def as_dto(cls):
        return {
            "step_label": cls.NAME,
            "fields": [field.as_dto() for field in cls.CONTAINS] if cls.CONTAINS else [],
            "show_if": [],
            "element": UI_TAB_ELEMENT,
            "field_type": UI_TAB_FIELD_TYPE,
            "predefined_uuid": cls.UUID,
            "show_link_header": False
        }

    @classmethod
    def get_missing_fields(cls, tabs):
        """
        Given all the tabs
        """
        if not cls.exists_in(tabs):
            return False
        tab = cls.get_from_tabs(tabs)
        tab_fields = tab.get('fields', [])
        return [field.as_dto() for field in cls.CONTAINS if not field.exists_in(tab_fields)]
        


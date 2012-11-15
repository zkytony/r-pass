# This class requires the uw's restclients app.  here mainly as an example
# pacakge

from restclients.gws import GWS

class UWGroupService():
    def is_member_of_group(self, user_name, group_source_id):
        gws = GWS()
        if gws.is_effective_member(group_source_id, user_name):
            return True
        return False

    def group_display_name(self, source_id):
        return source_id

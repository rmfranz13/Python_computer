# Necessary to make a reliable connection programmatically.
# It takes in an arbitrary number of pin objects as arguments.
# When the connection is updated, if a pin was updated, this class ensures all other pins
# update to match the value.
# This could cause issues if multiple 'connected' pins update between updates to the
# connection object, so be careful to always update a connection object whenever chips 
# with output pins leading to a connection are updated. (Can this be automated?)


class Connection:
    def __init__(self, pin_array):
        self.pins = pin_array
        self.vals = [ii.val for ii in pin_array]

    def update(self):
        update_needed = False
        new_vals = [ii.val for ii in self.pins]
        for ii in range(len(new_vals)):
            if(self.vals[ii] != new_vals[ii]):
                first_changed_val = new_vals[ii]
                update_needed = True
                break
        if(update_needed):
            for ii in self.pins:
                ii.val = first_changed_val

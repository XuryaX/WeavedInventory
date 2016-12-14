__author__ = 'shaur'

class HasChangedMixin(object):
    """ this mixin gives subclasses the ability to set fields for which they want to monitor if the field value changes """
    monitor_fields = []

    def __init__(self, *args, **kwargs):
        super(HasChangedMixin, self).__init__(*args, **kwargs)
        self.field_trackers = {}

    def __setattr__(self, key, value):
        super(HasChangedMixin, self).__setattr__(key, value)
        if key in self.monitor_fields and key not in self.field_trackers:
            self.field_trackers[key] = value

    def changed_fields(self):
        """
        :return: `list` of `str` the names of all monitor_fields which have changed
        """
        changed_fields = []
        for field, initial_field_val in self.field_trackers.items():
            if getattr(self, field) != initial_field_val:
                changed_fields.append(field)

        return changed_fields

    def get_initial_value(self,field):
        return self.field_trackers[field]
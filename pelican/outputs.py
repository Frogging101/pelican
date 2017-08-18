class Output(object):
    def __init__(self, path, override_output=False,
                 send_finalized_signal=None):
        self.path = path
        self.override_output = override_output
        self.send_finalized_signal = send_finalized_signal

class FeedOutput(Output):
    def __init__(self, path, elements, feed_type='atom', feed_title=None,
                 override_output=False, send_finalized_signal=None):
        self.elements = elements
        self.feed_type = feed_type
        self.feed_title = feed_title

        super(FeedOutput, self).__init__(path, override_output,
                                         send_finalized_signal)

class HTMLOutput(Output):
    def __init__(self, path, template, relative_urls=False, paginated=None,
                 override_output=False, send_finalized_signal=None, **kwargs):
        self.template = template
        self.relative_urls = relative_urls
        self.paginated = paginated
        self.template_vars = kwargs
        self.template_vars["output"] = self

        super(HTMLOutput, self).__init__(path, override_output,
                                         send_finalized_signal)

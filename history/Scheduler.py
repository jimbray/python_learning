# -*- coding: utf-8 -*-
__author__ = 'jimbray'

from threading import Timer


class Scheduler():
    def __init__(self, delay_time, function):
        self.delay_time = delay_time
        self.function = function
        self._t = None

    def start(self):
        if self._t is None:
            self._t = Timer(self.delay_time, self._run)
            self._t.start()
        else:
            raise Exception('This timer is already running.')

    def _run(self):
        self.function()
        self._t = Timer(self.delay_time, self._run)
        self._t.start()

    def stop(self):
        if self._t is not None:
            self._t.cancel()
            self._t = None
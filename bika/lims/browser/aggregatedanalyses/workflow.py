# -*- coding: utf-8 -*-
#
# This file is part of Bika LIMS
#
# Copyright 2011-2017 by it's authors.
# Some rights reserved. See LICENSE.txt, AUTHORS.txt.

from bika.lims.browser.worksheet.workflow import WorksheetWorkflowAction


class AggregatedAnalysesWorkflowAction(WorksheetWorkflowAction):
    """ Workflow actions taken in Aggregated Analyses View.
        This function is called to do the worflow actions
        that apply to analyses in the view.
        This class inherits from WorksheetWorkflowAction.
    """
    def __call__(self):
        WorksheetWorkflowAction.__call__(self)

    def submit(self):
        WorksheetWorkflowAction.submit(self)

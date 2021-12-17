from __future__ import print_function, absolute_import
from inspect import currentframe, getframeinfo

import os
import uuid
import json
import warnings
from pathlib import Path


from jupyter_core.paths import jupyter_path
from traitlets import HasTraits, Unicode, List, Dict, Bool, default, observe, validate
from traitlets.config import Config
from traitlets.utils.importstring import import_item
from jupyter_core.paths import jupyter_path
from jinja2 import (
    TemplateNotFound, Environment, ChoiceLoader, FileSystemLoader, BaseLoader,
    DictLoader
)

from nbconvert import templateexporter;
templateexporter.TemplateExporter

class CustomTemplateExporter(templateexporter.TemplateExporter):
    @default('extra_template_basedirs')
    def _default_extra_template_basedirs(self):
        return ['/home/aswin/plog_project/postbook/templates']
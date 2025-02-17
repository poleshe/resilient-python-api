#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

import os

import pkg_resources

PATH_RES_DEFAULT_DIR = os.path.abspath(os.path.join(os.path.expanduser("~"), ".resilient"))
PATH_RES_DEFAULT_LOG_DIR = os.path.join(PATH_RES_DEFAULT_DIR, "logs")
PATH_RES_DEFAULT_LOG_FILE = os.path.join(PATH_RES_DEFAULT_LOG_DIR, "app.log")

LOGGER_NAME = "resilient_sdk_log"
LOG_DIVIDER = "\n------------------------\n"
ENV_VAR_DEV = "RES_SDK_DEV"
ENV_VAR_APP_CONFIG_FILE = "APP_CONFIG_FILE"

RESILIENT_LIBRARIES_VERSION = "47.1.0"
RESILIENT_LIBRARIES_VERSION_DEV = "47.1.0"
RESILIENT_VERSION_WITH_PROXY_SUPPORT = (42, 0, 0)
CURRENT_SOAR_SERVER_VERSION = None
MIN_SOAR_SERVER_VERSION_PLAYBOOKS = 44.0

MIN_SUPPORTED_PY_VERSION = (3, 6)
SDK_PACKAGE_NAME = "resilient-sdk"
SDK_RESOURCE_NAME = "resilient_sdk"
CIRCUITS_PACKAGE_NAME = "resilient-circuits"

SUB_CMD_OPT_PACKAGE = ("--package", "-p")
SUB_CMD_OPT_SDK_SETTINGS = ("--settings", )

# file for SDK settings
SDK_SETTINGS_PARSER_NAME = "sdk_settings_file"
SDK_SETTINGS_FILENAME = ".sdk_settings.json"
SDK_SETTINGS_FILE_PATH = os.path.join(PATH_RES_DEFAULT_DIR, SDK_SETTINGS_FILENAME)
SDK_SETTINGS_BANDIT_SECTION_NAME = "bandit"

SUB_CMD_OPT_GATHER_RESULTS = "--gather-results"

# Resilient export file suffix.
RES_EXPORT_SUFFIX = ".res"
# Endpoint url for importing a configuration
IMPORT_URL = "/configurations/imports"

# Path to package templates for jinja rendering
PACKAGE_TEMPLATE_PATH = os.path.join("data", "codegen", "templates", "package_template")
PACKAGE_TEMPLATE_PACKAGE_DIR = os.path.join(PACKAGE_TEMPLATE_PATH, "package")
DOCGEN_TEMPLATE_PATH = os.path.join("data", "docgen", "templates")
BASE_PATH_VALIDATE_DATA = os.path.join("data", "validate")
VALIDATE_TEMPLATE_PATH = os.path.join(BASE_PATH_VALIDATE_DATA, "templates")
VALIDATE_REPORT_TEMPLATE_NAME = "validate_report.md.jinja2"

# docker test constants (used in validate)
DOCKER_BASE_REPO = "registry.access.redhat.com/ubi8/python-39:latest"
DOCKER_COMMAND_DICT = {
    "from_command": "FROM",         # sets base image to build on top of
    "set_argument": "ARG",          # sets variables to use during building of image
    "set_env_var": "ENV",           # sets environment variables that persist after image is built
    "user": "USER",                 # changes user
    "run_command": "RUN",           # runs a shell command
    "copy_command": "COPY",         # copies from one directory to another (i.e. 'cp' command)
    "entrypoint": "ENTRYPOINT",     # sets the entrypoint for the image
    "change_directory": "WORKDIR",  # changes current directory while building image (i.e. 'cd' command)
}

# Temp File Prefixes
TMP_PYPI_VERSION = "latest_pypi_version.json"

# URLs
URL_PYPI_VERSION = "https://pypi.org/pypi/resilient-sdk/json"

# setup.py constants (for validate)
SETUP_PY_INSTALL_REQ_NAME = "install_requires"

# tox tests constants (used in validate)
TOX_PACKAGE_NAME = "tox"
TOX_INI_FILENAME = "tox.ini"
TOX_TEMP_PATH_XML_REPORT = ".validate_tmp_dir"
TOX_TESTS_DEFAULT_ARGS = ['--resilient_email', '"integrations@example.org"', '--resilient_password', '"supersecret"', '--resilient_host', '"example.com"', '--resilient_org', '"Test Organization"']
TOX_MIN_ENV_VERSION = "py36" # the last character here must be a number and will be used as the base value for checks of envlist
TOX_MIN_PACKAGE_VERSION = (3, 24, 4)

# pylint constants (for validate)
PYLINT_PACKAGE_NAME = "pylint"
PATH_VALIDATE_PYLINT_RC_FILE = pkg_resources.resource_filename(SDK_RESOURCE_NAME, os.path.join(BASE_PATH_VALIDATE_DATA, ".pylintrc"))
PYLINT_MIN_VERSION = (2, 12) # minimum pylint version that has stats objs rather than stats dictionary
                             # this is the min required for bug in pylint that was found in pylint 2.6.0

# bandit constants (for validate)
BANDIT_PACKAGE_NAME = "bandit"
BANDIT_DEFAULT_ARGS = ["--exclude", "customize.py,tests/*", "--format", "screen", "-n", "1"]
BANDIT_DEFAULT_SEVERITY_LEVEL = ["-ll"]
BANDIT_VERBOSE_FLAG = ["-v"]

# icon sizing constants (for validate)
ICON_APP_LOGO_REQUIRED_WIDTH = 200
ICON_APP_LOGO_REQUIRED_HEIGHT = 72
ICON_COMPANY_LOGO_REQUIRED_WIDTH = 100
ICON_COMPANY_LOGO_REQUIRED_HEIGHT = 100

# resilient-sdk codegen
CODEGEN_JSON_SCHEMA_URI = "http://json-schema.org/draft-06/schema"

# resilient-sdk docgen
DOCGEN_PLACEHOLDER_STRING = "::CHANGE_ME::"

# resilient-sdk validate
VALIDATE_LOG_LEVEL_CRITICAL = "CRITICAL"
VALIDATE_LOG_LEVEL_ERROR = VALIDATE_LOG_LEVEL_CRITICAL
VALIDATE_LOG_LEVEL_WARNING = "WARNING"
VALIDATE_LOG_LEVEL_INFO = "INFO"
VALIDATE_LOG_LEVEL_DEBUG = "DEBUG"

# INFO Messages
INFO_MIN_PB_SUPPORT = "Only IBM SOAR >= v{0} supported".format(MIN_SOAR_SERVER_VERSION_PLAYBOOKS)

# WARNING Messages
WARNING_DRAFT_PB_SIDE_EFFECTS = "WARNING: Using the --draft-playbook option may have unexpected side effects. Please ensure your cloned Playbook is behaving as expected"

# ERROR Messages
ERROR_NOT_FIND_DIR = "Could not find directory"
ERROR_NOT_FIND_FILE = "Could not find file"
ERROR_WRONG_PYTHON_VERSION = "Please install Python >= 3.6 to use this functionality"
ERROR_PLAYBOOK_SUPPORT = "Playbooks are only supported in {0} for IBM SOAR >= {1}. Current version: {2}.".format(SDK_RESOURCE_NAME, MIN_SOAR_SERVER_VERSION_PLAYBOOKS, CURRENT_SOAR_SERVER_VERSION)

# Resilient Customizations
CUST_PLAYBOOKS = "playbooks"

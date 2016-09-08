# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "tea_garden"
app_title = "Tea Garden"
app_publisher = "frappe"
app_description = "app for tea gardens"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@frappe.io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tea_garden/css/tea_garden.css"
# app_include_js = "/assets/tea_garden/js/tea_garden.js"

# include js, css files in header of web template
# web_include_css = "/assets/tea_garden/css/tea_garden.css"
# web_include_js = "/assets/tea_garden/js/tea_garden.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "tea_garden.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "tea_garden.install.before_install"
# after_install = "tea_garden.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tea_garden.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tea_garden.tasks.all"
# 	],
# 	"daily": [
# 		"tea_garden.tasks.daily"
# 	],
# 	"hourly": [
# 		"tea_garden.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tea_garden.tasks.weekly"
# 	]
# 	"monthly": [
# 		"tea_garden.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "tea_garden.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tea_garden.event.get_events"
# }


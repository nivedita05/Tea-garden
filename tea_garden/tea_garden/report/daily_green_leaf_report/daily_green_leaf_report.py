# Copyright (c) 2013, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from tea_garden.tea_garden.doctype import daily_green_leaf_in_details

def execute(filters=None):
	column=get_columns()
	data=[]
	return column,data





def get_columns():
	columns = [{
		"fieldname": "section_name",
		"label": _("Section"),
		"fieldtype": "Link",
		"options": "daily_green_leaf_in_details",
		"width": 120
	}]
	columns.append({
			"fieldname": "original_area",
			"label": _("Area"),
			"fieldtype": "Link",
			"options": "daily_green_leaf_in_details",
			"width": 70
    })

    	columns.append({
			"fieldname": "area",
			"label": _("Area Plucked"),
			"fieldtype": "Link",
			"options": "daily_green_leaf_in_details",
			"width":100

			
		})


    	columns.append({
			"fieldname": "Green_leaf_per_hector",
			"label": _("Green Leaf/Hector"),
			"fieldtype":"Data",
			"options": "",
			"width":133
		})


    	columns.append({
			"fieldname": "pluckers_per_hector",
			"label": _("Pluckers/Hector"),
			"fieldtype": "Data",
			"options": "",
			"width":135
		})


    	columns.append({
			"fieldname": "plucking_average",
			"label": _("Plucking Average"),
			"fieldtype": "data",
			"options": "",
			"width":130
		})


    	columns.append({
			"fieldname": "round",
			"label": _("Round"),
			"fieldtype": "data",
			"options": "",
			"width":90
		})


    	columns.append({
			"fieldname": "r_per_days",
			"label": _("R/Days"),
			"fieldtype": "Float",
			"options": "",
			"width":90
		})


    	columns.append({
			"fieldname": "yield_hector",
			"label": _("yield/Hector"),
			"fieldtype": "Float",
			"options": "",
			"width":90
		})


    	columns.append({
			"fieldname": "percent_of_year_crop",
			"label": _("% Of Year Crop"),
			"fieldtype": "float",
			"options": "",
			"width":120
		})


	
	

	return columns
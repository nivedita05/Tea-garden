# Copyright (c) 2013, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe import utils
from frappe.utils import flt
from datetime import datetime
#import timedelta
#import json

def execute(filters=None):
	columns = get_columns()
	report_entries = get_report_entries(filters)
	data = []
	
	

	for sle in report_entries:

		
		todate_round=get_round(sle.section_id,filters)
		section_detail = get_section_details(sle.section_id,filters)
		
		to_date=get_to_date(sle.section_id,filters)
		from_date=get_from_date(sle.section_id,filters)
		act=get_actual_to_date_green_leaf(sle.section_id,filters)
		done_or_not_done=find_round(sle.section_id,filters)
		data.append([sle.division_name,sle.section_id,sle.section_name,section_detail,todate_round,from_date,to_date,act,done_or_not_done])
		
	return columns, data


	


# , sle.section_area, sle.area, sle.prune_type, sle.bush_type


def get_report_entries(filters):
	return frappe.db.sql("""select distinct section_id,section_name,division_name from `tabDaily Green Leaf in details` where estate_name = %s and prune_type=%s and bush_type=%s and date BETWEEN %s AND %s ORDER BY section_id ASC""",(filters.estate_name,filters.prune_type,filters.bush_type,'2016-01-01', filters.date),as_dict=1)

def get_section_details(section_id,filters):
	return frappe.db.sql("""select min(section_area) from `tabDaily Green Leaf in details` where section_id = %s and date BETWEEN %s and %s""",(section_id,'2016-01-01',filters.date)) 


def get_round(section_id,filters):
	return frappe.db.sql("""select sum(area)/section_area from `tabDaily Green Leaf in details` where section_id = %s and date BETWEEN %s AND %s ORDER BY date DESC LIMIT 1 """,(section_id, '2016-01-01',filters.date))





def get_to_date(section_id,filters):
	return frappe.db.sql("""select max(date) from `tabDaily Green Leaf in details` where section_id = %s and date between %s and %s""",(section_id,'2016-01-01',filters.date))
	

def get_from_date(section_id,filters):
	date1=get_to_date(section_id,filters)
	single_day=find_round(section_id,filters)
	plucked_area=frappe.db.sql("""select area from `tabDaily Green Leaf in details` where section_id=%s and date=%s """,(section_id,date1))
	original_area=get_section_details(section_id,filters)
	if single_day=="complete":
		if round(float(plucked_area[0][0]),3)==round(float(original_area[0][0]),3):
			return frappe.db.sql("""select max(date) from `tabDaily Green Leaf in details` where section_id = %s and date between %s and %s""",(section_id,'2016-01-01',filters.date))
	
	

def get_actual_to_date_green_leaf(section_id,filters):
	date1=get_to_date(section_id,filters)
	return frappe.db.sql("""select round(leaf_count/area,0) from `tabDaily Green Leaf in details` where section_id = %s and date between %s and %s""",(section_id,date1,filters.date))






def find_round(section_id,filters):
	todate_round=get_round(section_id,filters)
	if todate_round[0][0].is_integer():
		return "complete"
	else:
		return "incomplete"


	
	



def get_sle_conditions(filters):
	conditions = []
	return "and {}".format(" and ".join(conditions)) if conditions else ""



def get_columns():
		
		columns = [{
			"fieldname": "division_name",
				"label": _("Division"),
				"fieldtype": "Link",
				"options": "Division",
				"width": 80

		}]

		columns.append({
				"fieldname": "section_id",
				"label": _("Section Id"),
				"fieldtype": "Link",
				"options": "Section",
				"width": 90
	    })

		columns.append({
				"fieldname": "section_name",
				"label": _("Section Name"),
				"fieldtype": "Link",
				"options": "Section",
				"width": 90
	    })
		
		columns.append({
				"fieldname": "original_area",
				"label": _("Area"),
				"fieldtype": "Float",
				"options": "daily_green_leaf_in_details",
				"width": 70
	    })


		
		columns.append({
			"label": _("Round"),
			"fieldtype": "round(Float,5)",
			"width":71
		})

		columns.append({
			"label": _("From"),
			"fieldtype": "Data",
			"width":71
		})

		
		columns.append({
			"label": _("To"),
			"fieldtype": "Data",
			"width":71
		})

		columns.append({
			"label": _("Act"),
			"fieldtype": "round(float,0)",
			"width":71
		})

		columns.append({
			"label": _("done or not done"),
			"fieldtype": "data",
			"width":71
		})


		
		return columns

	
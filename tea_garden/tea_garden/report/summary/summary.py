# Copyright (c) 2013, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe import utils
from frappe.utils import flt
from datetime import datetime,timedelta
from tea_garden.tea_garden.report.last_round_report.last_round_report import get_to_date,get_actual_budget,get_section_details
import operator
#import timedelta
#import json

def execute(filters=None):
	columns = get_columns()
	report_entries = get_report_entries(filters)
	data = []
	t_section_area = 0
	
	for sle in report_entries:
		
		
		area = get_area(sle.prune_type,sle.bush_type,filters)
		yield_act=todate_yield_act(sle.prune_type,sle.bush_type,filters)
		bud=todate_yield_budget(sle.prune_type,sle.bush_type,filters)

		plus_minus=todate_yield_plus_minus(sle.prune_type,sle.bush_type,filters)
		made=made_tea(sle.prune_type,sle.bush_type,filters)

		data.append([sle.prune_type,sle.bush_type,area,yield_act,bud,plus_minus,made])

	return columns, data



def get_report_entries(filters):
	return frappe.db.sql("""select distinct prune_type,bush_type from `tabDaily Green Leaf in details` where estate_name = %s order by bush_type """,(filters.estate_name),as_dict=1)

def get_area(prune_type,bush_type,filters):
	return frappe.db.sql("""select sum(distinct(section_area)) from `tabDaily Green Leaf in details` where prune_type= %s and bush_type=%s  and date BETWEEN %s and %s""",(prune_type,bush_type,datetime(datetime.now().year, 1, 1),filters.date)) 


def todate_yield_act(prune_type,bush_type,filters):
	todate_yield=frappe.db.sql("""select sum(leaf_count) from `tabDaily Green Leaf in details` where  prune_type=%s and date between %s and %s """,(prune_type,datetime(datetime.now().year, 1, 1),filters.date))
	area=get_area(prune_type,bush_type,filters)
	return round((todate_yield[0][0]*0.225)/area[0][0],2)


def todate_yield_budget(prune_type,bush_type,filters):
	t_budget=0
	sections=frappe.db.sql("""select distinct section_id,section_area from `tabDaily Green Leaf in details` where prune_type=%s and bush_type=%s and date between %s and %s  """,(prune_type,bush_type,datetime(datetime.now().year, 1, 1),filters.date),as_dict=1)
	area=get_area(prune_type,bush_type,filters)
	for sle in sections:
		budget = get_actual_budget(sle.section_id,filters,prune_type)
		t_budget += budget * sle.section_area
	return round((t_budget/area[0][0]),2)	


def todate_yield_plus_minus(prune_type,bush_type,filters):
	act=todate_yield_act(prune_type,bush_type,filters)
	budget=todate_yield_budget(prune_type,bush_type,filters)
	return round(act-budget,2)


def made_tea(prune_type,bush_type,filters):
	act=todate_yield_act(prune_type,bush_type,filters)
	budget=todate_yield_budget(prune_type,bush_type,filters)
	area=get_area(prune_type,bush_type,filters)
	return round((act-budget)* area[0][0],0)


def get_columns():
		
		columns = [{
			"fieldname": "prune_type",
				"label": _("Prune"),
				"fieldtype": "Link",
				"options": "Prune Type",
				"width": 80

		}]

		columns.append({
				"fieldname": "bush_type",
				"label": _("Bush "),
				"fieldtype": "Data",
				"width": 90
	    })


		columns.append({
				"label": _(" Area "),
				"fieldtype": "Data",
				"width": 90
	    })
	    

	    	columns.append({
				"label": _(" Todate Yield "),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"label": _(" Budget "),
				"fieldtype": "Data",
				"width": 90
	    })
	    
	    	columns.append({
				"label": _("Todate Yield +/- "),
				"fieldtype": "Data",
				"width": 100
	    })


	    	columns.append({
				"label": _("Made Tea"),
				"fieldtype": "Data",
				"width": 100
	    })
	    


		
		
		return columns


	
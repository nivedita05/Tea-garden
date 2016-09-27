# Copyright (c) 2013, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe import utils
from frappe.utils import flt
from datetime import datetime,timedelta
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

		data.append([sle.prune_type,sle.bush_type,area,yield_act])

	return columns, data



def get_report_entries(filters):
	return frappe.db.sql("""select distinct prune_type,bush_type from `tabDaily Green Leaf in details` where estate_name = %s order by bush_type """,(filters.estate_name),as_dict=1)

def get_area(prune_type,bush_type,filters):
	return frappe.db.sql("""select sum(distinct(section_area)) from `tabDaily Green Leaf in details` where prune_type= %s and bush_type=%s  and date BETWEEN %s and %s""",(prune_type,bush_type,'2016-01-01',filters.date)) 


def todate_yield_act(prune_type,bush_type,filters):
	todate_yield=frappe.db.sql("""select sum(leaf_count) from `tabDaily Green Leaf in details` where  prune_type=%s and date between %s and %s """,(prune_type,'2016-01-01',filters.date))
	area=get_area(prune_type,bush_type,filters)
	return round((todate_yield[0][0]*0.225)/area[0][0],2)



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
	    
	    


		
		
		return columns


	
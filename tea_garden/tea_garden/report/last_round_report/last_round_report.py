

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
import calendar
import os
from tea_garden.tea_garden.report.comparison_of_budget_and_actual_crop.comparison_of_budget_and_actual_crop import \
get_month_wise_budget_for_jan,get_month_wise_budget_for_feb,get_month_wise_budget_for_mar,get_month_wise_budget_for_apr,\
get_month_wise_budget_for_may,get_month_wise_budget_for_jun,get_month_wise_budget_for_jul,get_month_wise_budget_for_aug,\
get_month_wise_budget_for_sep,get_month_wise_budget_for_oct,get_month_wise_budget_for_nov,get_month_wise_budget_for_dec,\
get_monthly_budget,get_budget_for_a_particular_mon
#import timedelta
#import json

def execute(filters=None):
	columns = get_columns()
	report_entries = get_report_entries(filters)
	data = []

	#data.append([])
	#data.append([])

	#data.append(['','','Date',filters.date,'','Garden',filters.estate_name,'','Bush',filters.bush_type,'','Prune',filters.prune_type])
	#data.append([])




	t_area=0
	t_yield=0
	t_year_budget=0
	

	for sle in report_entries:
		area=get_section_area(sle.section_id,filters)
		round_=get_round(sle.section_id,filters)

		from_date=get_from_date(sle.section_id,filters)
		to_date=get_to_date(sle.section_id,filters)


		act=get_act_to_date(sle.section_id,filters)
		bud=get_bud_to_date(sle.section_id,filters)
		perc=get_plus_minus_percentage(sle.section_id,filters)


		act_yield=get_actual_todate_yield(sle.section_id,filters)
		bud_yield=get_budget_todate_yield(sle.section_name,filters,frappe.utils.get_datetime(filters.date).strftime('%m'))
		perc_yield=round((act_yield-bud_yield)*100/bud_yield,2)


		proj_yield=get_proj_yield(sle.section_id,filters)
		achv_perc=get_achive_percentage(sle.section_id,filters)


		t_area+=area[0][0]
		t_yield+=area[0][0]*bud_yield
		t_year_budget+=area[0][0]*proj_yield[0][0]
		

		data.append([sle.division_name,sle.section_id,sle.section_name,area,round(float(round_[0][0]),0),from_date,to_date,act,bud,perc,act_yield,bud_yield,perc_yield,proj_yield,achv_perc])

	todate_yield=todate_yield_act(filters)	
	t_actual=round(todate_yield/t_area,2)
	t_budget=round(t_yield/t_area ,2)
	t_perc=round(((t_actual-t_budget)*100)/t_budget,2)
	t_yearly_budget=round(t_year_budget/t_area,2)
	t_achieve_percentage=round((t_actual/t_yearly_budget)*100,2)

	
	data.append(["<b>"+'Total'+"</b>",'','',"<b>"+str(t_area)+"</b>",'','',"<b>"+'Todate Yield'+"</b>","<b>"+str(t_actual)+"</b>","<b>"+str(t_budget)+"</b>",'','','','',"<b>"+str(t_yearly_budget)+"</b>","<b>"+str(t_achieve_percentage)+"</b>"])	
	return columns, data




def todate_yield_act(filters):
	todate_yield=frappe.db.sql("""select sum(leaf_count) from `tabDaily Green Leaf in details` where  prune_type=%s and date between %s and %s """,(filters.prune_type,datetime(datetime.now().year, 1, 1),filters.date))
	return todate_yield[0][0]*0.225


def get_report_entries(filters):
	return frappe.db.sql("""select distinct section_id,section_name,division_name,section_area from `tabDaily Green Leaf in details` where estate_name = %s and prune_type=%s and bush_type=%s and date BETWEEN %s AND %s ORDER BY section_id ASC""",(filters.estate_name,filters.prune_type,filters.bush_type,datetime(datetime.now().year, 1, 1), filters.date),as_dict=1)

def get_section_area(section_id,filters):
	return frappe.db.sql("""select min(section_area) from `tabDaily Green Leaf in details` where section_id = %s and date BETWEEN %s and %s""",(section_id,datetime(datetime.now().year, 1, 1),filters.date)) 

def get_round(section_id,filters):
	return frappe.db.sql("""select round(sum(area)/section_area,2) from `tabDaily Green Leaf in details` where section_id = %s and date BETWEEN %s AND %s ORDER BY date DESC LIMIT 1 """,(section_id, datetime(datetime.now().year, 1, 1),filters.date))


def get_from_date(section_id,filters):

	to_date=frappe.db.sql("""select max(date) from `tabDaily Green Leaf in details` where section_id=%s and mark='Yes' and date between %s and %s """,(section_id,datetime(datetime.now().year, 1, 1),filters.date))
	area_plucked=frappe.db.sql("""select area from `tabDaily Green Leaf in details` where section_id=%s and date=%s """,(section_id,to_date))
	original_area=get_section_area(section_id,filters)
	if area_plucked[0][0]== original_area[0][0]:
		from_date=to_date
	else:
		date1=frappe.db.sql("""select max(date) from `tabDaily Green Leaf in details` where section_id=%s and mark='Yes' and date<%s """,(section_id,to_date))
		from_date=frappe.db.sql("""select min(date) from`tabDaily Green Leaf in details` where section_id=%s and date between %s and %s and mark='No'""",(section_id,date1,to_date))
	return from_date


def get_to_date(section_id,filters):
	to_date=frappe.db.sql("""select max(date) from `tabDaily Green Leaf in details` where section_id=%s and mark='Yes' and date between %s and %s """,(section_id,datetime(datetime.now().year, 1, 1),filters.date))
	return to_date



def get_act_to_date(section_id,filters):
	from_date=get_from_date(section_id,filters)
	to_date=get_to_date(section_id,filters)
	leaf_c=frappe.db.sql("""select round(sum(leaf_count),0) from `tabDaily Green Leaf in details` where section_id = %s and date between %s and %s""",(section_id,from_date,to_date))
	area=get_section_area(section_id,filters)
	act=round(leaf_c[0][0]/area[0][0],0)
	
	return act

def get_bud_to_date(section_id,filters):
	to_date=get_to_date(section_id,filters)
	return frappe.db.sql("""select round((round_days*today_budget)/0.225,0) from `tabDaily Green Leaf in details` where section_id = %s and date=%s""",(section_id,to_date)) 
	

def get_plus_minus_percentage(section_id,filters):
	act=get_act_to_date(section_id,filters)
	bud=get_bud_to_date(section_id,filters)
	percentage=round((act-bud[0][0])*100/bud[0][0],2)
	return percentage

def get_actual_todate_yield(section_id,filters):

	from_date=get_from_date(section_id,filters)
	to_date=get_to_date(section_id,filters)
	leaf_c=frappe.db.sql("""select round(sum(leaf_count)*0.225,0) from `tabDaily Green Leaf in details` where section_id = %s and date between %s and %s""",(section_id,datetime(datetime.now().year, 1, 1),filters.date))
	area=get_section_area(section_id,filters)
	act=leaf_c[0][0]/area[0][0]
	return round(act,0)



def get_budget_todate_yield(section_name,filters,month):
	month=frappe.utils.get_datetime(filters.date).strftime('%m')
	bud = 0.0
	for i in range(1,int(month),1):
		bud +=float(get_monthly_budget(section_name,filters,str(i).zfill(2))[0][0])

	bud_mon=float(get_budget_for_a_particular_mon(section_name,filters,month))
	bud=bud+bud_mon
	return round(bud)

def get_proj_yield(section_id,filters):
	return frappe.db.sql("""select projected_yield from `tabPruning Cycle` where section_id=%s """,(section_id))


def get_achive_percentage(section_id,filters):
	proj=get_proj_yield(section_id,filters)
	act=get_actual_todate_yield(section_id,filters)
	achv_perc=(act*100)/proj[0][0]
	return round(achv_perc,2)



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
				"fieldtype": "round(Float,2)",
				"options": "daily_green_leaf_in_details",
				"width": 70
	    })


	    	columns.append({
				"fieldname": "rnd",
				"label": _("Round"),
				"fieldtype": "round(Float,0)",
				"width": 70
	    })


	    	columns.append({
				"fieldname": "frm",
				"label": _("From"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "to",
				"label": _("To"),
				"fieldtype": "Data",
				"width": 90
	    })

	    	columns.append({
				"fieldname": "act",
				"label": _("Act"),
				"fieldtype": "Data",
				"width": 70
	    })

	    	columns.append({
				"fieldname": "bud",
				"label": _("Bud"),
				"fieldtype": "Data",
				"width": 70
	    })

	    	columns.append({
				"fieldname": "plus_minus",
				"label": _("(+/-) %"),
				"fieldtype": "Float",
				"width": 70
	    })


	    	columns.append({
				"fieldname": "act_y",
				"label": _("Act Yield"),
				"fieldtype": "Data",
				"width": 70
	    })

	    	columns.append({
				"fieldname": "bud_y",
				"label": _("Bud Yield"),
				"fieldtype": "Data",
				"width": 70
	    })


	    	columns.append({
				"fieldname": "plus_minus_y",
				"label": _("+/- %"),
				"fieldtype": "Data",
				"width": 70
	    })


	    	columns.append({
				"fieldname": "projected_yield",
				"label": _("Total"),
				"fieldtype": "Data",
				"width": 70
	    })

	    	columns.append({
				"fieldname": "achv_perc",
				"label": _("Achv %"),
				"fieldtype": "Data",
				"width": 70
	    })








		
		
		return columns


	

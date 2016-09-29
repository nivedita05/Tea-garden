# Copyright (c) 2013, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe import utils
from frappe.utils import flt
from datetime import datetime,timedelta



def execute(filters=None):
	columns = get_columns()
	report_entries = get_report_entries(filters)
	data = []

	for sle in report_entries:
		month_wise_budget_for_jan=get_month_wise_budget_for_jan(sle.section_name,filters)
		month_wise_budget_for_feb=get_month_wise_budget_for_feb(sle.section_name,filters)
		
		month_wise_budget_for_mar=get_month_wise_budget_for_mar(sle.section_name,filters)
		month_wise_budget_for_apr=get_month_wise_budget_for_apr(sle.section_name,filters)

		month_wise_budget_for_may=get_month_wise_budget_for_may(sle.section_name,filters)
		month_wise_budget_for_jun=get_month_wise_budget_for_jun(sle.section_name,filters)

		month_wise_budget_for_jul=get_month_wise_budget_for_jul(sle.section_name,filters)
		month_wise_budget_for_aug=get_month_wise_budget_for_aug(sle.section_name,filters)

		month_wise_budget_for_sep=get_month_wise_budget_for_sep(sle.section_name,filters)
		month_wise_budget_for_oct=get_month_wise_budget_for_oct(sle.section_name,filters)

		month_wise_budget_for_nov=get_month_wise_budget_for_nov(sle.section_name,filters)
		month_wise_budget_for_dec=get_month_wise_budget_for_dec(sle.section_name,filters)

		total=get_projected_yield(sle.section_name,filters)
		vac=get_vacancy_percentage(sle.section_name,filters)




		month_wise_act_for_jan=get_act_for_jan(sle.section_name,filters)
		month_wise_act_for_feb=get_act_for_feb(sle.section_name,filters)

		month_wise_act_for_mar=get_act_for_mar(sle.section_name,filters)
		month_wise_act_for_apr=get_act_for_apr(sle.section_name,filters)


		month_wise_act_for_may=get_act_for_may(sle.section_name,filters)
		month_wise_act_for_jun=get_act_for_jun(sle.section_name,filters)

		month_wise_act_for_jul=get_act_for_jul(sle.section_name,filters)
		month_wise_act_for_aug=get_act_for_aug(sle.section_name,filters)

		month_wise_act_for_sep=get_act_for_sep(sle.section_name,filters)
		month_wise_act_for_oct=get_act_for_oct(sle.section_name,filters)


		month_wise_act_for_nov=get_act_for_nov(sle.section_name,filters)
		month_wise_act_for_dec=get_act_for_dec(sle.section_name,filters)


		act_total=get_act_for_year(sle.section_name,filters)

		percent=round((act_total[0][0]*100)/total[0][0],0)
		

		jan_diff=get_diff_jan(sle.section_name,filters)
		feb_diff=get_diff_feb(sle.section_name,filters)

		mar_diff=get_diff_mar(sle.section_name,filters)
		apr_diff=get_diff_apr(sle.section_name,filters)

		may_diff=get_diff_may(sle.section_name,filters)
		jun_diff=get_diff_jun(sle.section_name,filters)
		
		jul_diff=get_diff_jul(sle.section_name,filters)
		aug_diff=get_diff_aug(sle.section_name,filters)

		sep_diff=get_diff_sep(sle.section_name,filters)
		oct_diff=get_diff_oct(sle.section_name,filters)

		nov_diff=get_diff_nov(sle.section_name,filters)
		dec_diff=get_diff_dec(sle.section_name,filters)
		
		
		tot_diff=total[0][0]-act_total[0][0]

		data.append([sle.division_name,sle.section_name,'Budget',month_wise_budget_for_jan,month_wise_budget_for_feb,month_wise_budget_for_mar,month_wise_budget_for_apr,month_wise_budget_for_may,month_wise_budget_for_jun,month_wise_budget_for_jul,month_wise_budget_for_aug,month_wise_budget_for_sep,month_wise_budget_for_oct,month_wise_budget_for_nov,month_wise_budget_for_dec,total,percent,vac])
		data.append(['','','Act',month_wise_act_for_jan,month_wise_act_for_feb,month_wise_act_for_mar,month_wise_act_for_apr,month_wise_act_for_may,month_wise_act_for_jun,month_wise_act_for_jul,month_wise_act_for_aug,month_wise_act_for_sep,month_wise_act_for_oct,month_wise_act_for_nov,month_wise_act_for_dec,act_total])
		data.append(['','','(+/-)',jan_diff,feb_diff,mar_diff,apr_diff,may_diff,jun_diff,jul_diff,aug_diff,sep_diff,oct_diff,nov_diff,dec_diff,tot_diff])
		data.append([])

	return columns, data


def get_report_entries(filters):
	return frappe.db.sql("""select distinct division_name ,section_name from `tabDaily Green Leaf in details` where estate_name = %s and prune_type=%s order by division_name""",(filters.estate_name,filters.prune_type),as_dict=1)

def get_month_wise_budget_for_jan(section_name,filters):
	return frappe.db.sql("""select january from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_feb(section_name,filters):
	return frappe.db.sql("""select february from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_mar(section_name,filters):
	return frappe.db.sql("""select march from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_apr(section_name,filters):
	return frappe.db.sql("""select april from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_may(section_name,filters):
	return frappe.db.sql("""select may from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_jun(section_name,filters):
	return frappe.db.sql("""select june from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_jul(section_name,filters):
	return frappe.db.sql("""select july from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_aug(section_name,filters):
	return frappe.db.sql("""select august from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_sep(section_name,filters):
	return frappe.db.sql("""select september from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_oct(section_name,filters):
	return frappe.db.sql("""select october from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_nov(section_name,filters):
	return frappe.db.sql("""select november from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_dec(section_name,filters):
	return frappe.db.sql("""select december from `tabPruning Cycle` where section_name=%s """,(section_name))


def get_month_wise_budget_for_any_month(section_name,filters):
	pass

def get_projected_yield(section_name,filters):
	return frappe.db.sql("""select projected_yield from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_vacancy_percentage(section_name,filters):
	return frappe.db.sql("""select vacancy_percentage from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_act_for_jan(section_name,filters):
	return frappe.db.sql("""select coalesce(sum(leaf_count)*0.225/section_area,0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 1, 1),datetime(datetime.now().year,1,31)))

def get_act_for_feb(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 2, 1),datetime(datetime.now().year,2,28)))
	

def get_act_for_mar(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 3, 1),datetime(datetime.now().year,3,31)))

def get_act_for_apr(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 4, 1),datetime(datetime.now().year,4,30)))

def get_act_for_may(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 5, 1),datetime(datetime.now().year,5,31)))
	
def get_act_for_jun(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 6, 1),datetime(datetime.now().year,6,30)))


def get_act_for_jul(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 7, 1),datetime(datetime.now().year,7,31)))

def get_act_for_aug(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 8, 1),datetime(datetime.now().year,8,21)))
	

def get_act_for_sep(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 9, 1),datetime(datetime.now().year,9,30)))

def get_act_for_oct(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 10, 1),datetime(datetime.now().year,10,31)))

def get_act_for_nov(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 11, 1),datetime(datetime.now().year,11,30)))
	
def get_act_for_dec(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 12, 1),datetime(datetime.now().year,12,31)))

def get_act_for_year(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 1, 1),datetime(datetime.now().year,12,31)))


def get_diff_jan(section_name,filters):
	jan_act=get_act_for_jan(section_name,filters)
	jan_bud=get_month_wise_budget_for_jan(section_name,filters)
	return round(jan_act[0][0]-float(jan_bud[0][0]),2)


def get_diff_feb(section_name,filters):
	feb_act=get_act_for_feb(section_name,filters)
	feb_bud=get_month_wise_budget_for_feb(section_name,filters)
	return round(feb_act[0][0]-float(feb_bud[0][0]),2)

def get_diff_mar(section_name,filters):
	mar_act=get_act_for_mar(section_name,filters)
	mar_bud=get_month_wise_budget_for_mar(section_name,filters)
	return round(mar_act[0][0]-float(mar_bud[0][0]),2)

def get_diff_apr(section_name,filters):
	apr_act=get_act_for_apr(section_name,filters)
	apr_bud=get_month_wise_budget_for_apr(section_name,filters)
	return round(apr_act[0][0]-float(apr_bud[0][0]),2)

def get_diff_may(section_name,filters):
	may_act=get_act_for_may(section_name,filters)
	may_bud=get_month_wise_budget_for_may(section_name,filters)
	return round(may_act[0][0]-float(may_bud[0][0]),2)

def get_diff_jun(section_name,filters):
	jun_act=get_act_for_jun(section_name,filters)
	jun_bud=get_month_wise_budget_for_jun(section_name,filters)
	return round(jun_act[0][0]-float(jun_bud[0][0]),2)

def get_diff_jul(section_name,filters):
	jul_act=get_act_for_jul(section_name,filters)
	jul_bud=get_month_wise_budget_for_jul(section_name,filters)
	return round(jul_act[0][0]-float(jul_bud[0][0]),2)


def get_diff_aug(section_name,filters):
	aug_act=get_act_for_aug(section_name,filters)
	aug_bud=get_month_wise_budget_for_aug(section_name,filters)
	return round(aug_act[0][0]-float(aug_bud[0][0]),2)

def get_diff_sep(section_name,filters):
	sep_act=get_act_for_sep(section_name,filters)
	sep_bud=get_month_wise_budget_for_sep(section_name,filters)
	return round(sep_act[0][0]-float(sep_bud[0][0]),2)

def get_diff_oct(section_name,filters):
	oct_act=get_act_for_oct(section_name,filters)
	oct_bud=get_month_wise_budget_for_oct(section_name,filters)
	return round(oct_act[0][0]-float(oct_bud[0][0]),2)

def get_diff_nov(section_name,filters):
	nov_act=get_act_for_nov(section_name,filters)
	nov_bud=get_month_wise_budget_for_nov(section_name,filters)
	return round(nov_act[0][0]-float(nov_bud[0][0]),2)

def get_diff_dec(section_name,filters):
	dec_act=get_act_for_dec(section_name,filters)
	dec_bud=get_month_wise_budget_for_dec(section_name,filters)
	return round(dec_act[0][0]-float(dec_bud[0][0]),2)

def get_columns():
		
	columns = [{
		"fieldname": "division_name",
		"label": _("Division"),
		"fieldtype": "Link",
		"options": "Division",
		"width": 80

	}]

	columns.append({
		"fieldname": "section_name",
		"label": _("Section"),
		"fieldtype": "Link",
		"options": "Section",
		"width": 150
	    })

	columns.append({
		"fieldname": " ",
		"label": _(" "),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "january",
		"label": _("JAN"),
		"options": "Data",
		"width": 70
	    })


	columns.append({
		"fieldname": "february",
		"label": _("FEB"),
		"options": "Data",
		"width": 70
	    })


	columns.append({
		"fieldname": "march",
		"label": _("MAR"),
		"options": "Data",
		"width": 70
	    })


	columns.append({
		"fieldname": "april",
		"label": _("APR"),
		"options": "Data",
		"width": 70
	    })


	columns.append({
		"fieldname": "may",
		"label": _("MAY"),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "june",
		"label": _("JUN"),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "july",
		"label": _("JUL"),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "august",
		"label": _("AUG"),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "september",
		"label": _("SEP"),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "october",
		"label": _("OCT"),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "november",
		"label": _("NOV"),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "december",
		"label": _("DEC"),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "total",
		"label": _("Total"),
		"options": "Data",
		"width": 70
	    })


	columns.append({
		"fieldname": "%",
		"label": _("%"),
		"options": "Data",
		"width": 70
	    })


	columns.append({
		"fieldname": "vac",
		"label": _("VAC %"),
		"options": "Data",
		"width": 70
	    })












	return columns

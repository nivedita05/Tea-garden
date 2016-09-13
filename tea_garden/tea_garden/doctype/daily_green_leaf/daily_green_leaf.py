# -*- coding: utf-8 -*-
# Copyright (c) 2015, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _
from frappe import utils





class DailyGreenLeaf(Document):


	def validate(self):
		self.get_bush_name()
		self.get_prune_name()
		self.calculate_today_budget()
		self.validate_section_name()
		self.validtae_area()
		self.validate_uniqueness()

	
		
		

# check the area entered is less than the original area or not , otherwise give  an error message

	def validtae_area(self):
		for i in self.leaf_details:
			if(i.section_area<i.area):
				frappe.throw("the area entered is more than the original area  !!!!!!!")
						
# check the combination of date and garden is unique or not 

	def validate_uniqueness(self):
		name=frappe.db.sql("""select date from `tabDaily Green Leaf` 
				where date=%s and estate_name=%s and docstatus=1""",(self.date,self.estate_name))
		if name:
			frappe.throw("Record already exist for the date!!!!")

# if a record realated to a section for a particula garden on a particular date is already entered or not

	def validate_section_name(self):
		"""Set missing names and warn if duplicate"""
		found = []
		for section in self.leaf_details:

			if section.section_name in found:
				frappe.throw(_("Section {0} entered twice").format(section.section_name))

			found.append(section.section_name)
				
# calculate the budget corresponding to a particular date of a particular month

	def calculate_today_budget(self):
		
		for i in self.leaf_details:
			#if (frappe.utils.get_datetime(self.date).strftime('%Y')=="2016" or frappe.utils.get_datetime(self.date).strftime('%Y')=="2017" or frappe.utils.get_datetime(self.date).strftime('%Y')=="2018" or frappe.utils.get_datetime(self.date).strftime('%Y')=="2019"):
				
			if(frappe.utils.get_datetime(self.date).strftime('%m')=="01"):
				prune_cycle=frappe.db.sql("""select january from `tabPruning Cycle` where year=%s and section_name=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_name))
				i.today_budget=round((float(prune_cycle[0][0])/31),2)

			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="02"):
				prune_cycle=frappe.db.sql("""select february from `tabPruning Cycle` where year=%s and section_name=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_name))
				i.today_budget=round((float(prune_cycle[0][0])/28),2)

			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="03"):
				prune_cycle=frappe.db.sql("""select march from `tabPruning Cycle` where year=%s and section_name=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_name))
				i.today_budget=round((float(prune_cycle[0][0])/31),2)

			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="04"):
				prune_cycle=frappe.db.sql("""select april from `tabPruning Cycle` where year=%s and section_name=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_name))
				i.today_budget=round((float(prune_cycle[0][0])/30),2)

			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="05"):
				prune_cycle=frappe.db.sql("""select may from `tabPruning Cycle` where year=%s and section_name=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_name))
				i.today_budget=round((float(prune_cycle[0][0])/31),2)


			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="06"):
				prune_cycle=frappe.db.sql("""select june from `tabPruning Cycle` where year=%s and section_name=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_name))
				i.today_budget=round((float(prune_cycle[0][0])/30),2)


			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="07"):
				prune_cycle=frappe.db.sql("""select july from `tabPruning Cycle` where year=%s and section_name=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_name))
				i.today_budget=round((float(prune_cycle[0][0])/31),2)

			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="08"):
				prune_cycle=frappe.db.sql("""select august from `tabPruning Cycle` where year=%s and section_name=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_name))
				i.today_budget=round((float(prune_cycle[0][0])/31),2)

			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="09"):
				prune_cycle=frappe.db.sql("""select september from `tabPruning Cycle` where year=%s and section_name=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_name))
				i.today_budget=round((float(prune_cycle[0][0])/30),2)

			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="10"):
				prune_cycle=frappe.db.sql("""select october from `tabPruning Cycle` where year=%s and section_name=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_name))
				i.today_budget=round((float(prune_cycle[0][0])/31),2)

			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="11"):
				prune_cycle=frappe.db.sql("""select november from `tabPruning Cycle` where year=%s and section_name=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_name))
				i.today_budget=round((float(prune_cycle[0][0])/30),2)

			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="12"):
				prune_cycle=frappe.db.sql("""select december from `tabPruning Cycle` where year=%s and section_name=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_name))
				i.today_budget=round((float(prune_cycle[0][0])/31),2)

		

# get the prune name corresponding to the section

	def get_prune_name(self):
		
		for i in self.leaf_details:
			#if (frappe.utils.get_datetime(self.date).strftime('%Y')=="2016" or frappe.utils.get_datetime(self.date).strftime('%Y')=="2017" or frappe.utils.get_datetime(self.date).strftime('%Y')=="2018" or frappe.utils.get_datetime(self.date).strftime('%Y')=="2019"):
			prune_cycle=frappe.db.sql("""select  prune_type from `tabPruning Cycle` where year=%s and section_name=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_name))
			i.prune_type=prune_cycle[0][0]
		

# get the bush name corresponding to the section

	def get_bush_name(self):
		
		for i in self.leaf_details:
			#if (frappe.utils.get_datetime(self.date).strftime('%Y')=="2016" or frappe.utils.get_datetime(self.date).strftime('%Y')=="2017" or frappe.utils.get_datetime(self.date).strftime('%Y')=="2018" or frappe.utils.get_datetime(self.date).strftime('%Y')=="2019"):
			prune_cycle=frappe.db.sql("""select bush_type from `tabPruning Cycle` where year=%s and section_name=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_name))
			i.bush_type=prune_cycle[0][0]
		
				
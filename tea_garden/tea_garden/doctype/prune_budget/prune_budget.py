# -*- coding: utf-8 -*-
# Copyright (c) 2015, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

class PruneBudget(Document):
	
	def validate(self):
		self.validate_100()
		self.uniqueness_in_three()
		

# chack that after suming the percentage of 12 months it returns 100 or not
	def validate_100(self):
		if self.prune_type!="NP":
			sumv=self.january+self.february+self.march+self.april+self.may+self.june+self.july+self.august+self.september+self.october+self.november+self.december
			if (round(float(sumv),2)!=100):
				frappe.throw("The sum of the given percentages is not equal to hundred")
		
#the combination of garden,prune and bush must be unique when preparing a budget
	def uniqueness_in_three(self):
		name=frappe.db.sql("""select * from `tabPrune Budget` as pb
				where pb.prune_type=%s and pb.estate_name=%s and pb.bush_type=%s  and docstatus=1""",(self.prune_type,self.estate_name,self.bush_type))
		if name and self.docstatus==0:
			frappe.throw("Record already exist for this combination !!!!")

	
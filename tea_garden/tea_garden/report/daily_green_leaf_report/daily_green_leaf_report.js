// Copyright (c) 2016, frappe and contributors
// For license information, please see license.txt

frappe.query_reports["Daily Green Leaf Report"] = {
	"filters": [
	 {
            "fieldname":"date",
            "label": __("DATE"),
            "fieldtype": "Date",
            "options": "",
            "default": frappe.defaults.get_user_default("date"),
            "reqd":1
        },


        {
            "fieldname":"estate_name",
            "label": __("ESTATE NAME"),
            "fieldtype": "Link",
            "options": "Estate",
            "default": frappe.defaults.get_user_default("estate_name"),
            "reqd":1
         },

        {
            "fieldname":"bush_type",
            "label": __("Bush"),
            "fieldtype":"Data",
            "options":"",
            "default": frappe.defaults.get_user_default("Mature"),
            "reqd":1
         },

        {
            "fieldname":"prune_type",
            "label": __("Prune"),
            "fieldtype": "Link",
            "options": "Prune Type",
            "default": frappe.defaults.get_user_default("prune_type"),
            "reqd":1
         },

        {
            "fieldname":"division_name",
            "label": __("Division"),
            "fieldtype": "Link",
            "options": "Division",
            "default": frappe.defaults.get_user_default("division_name"),
            "reqd":1
         }

	]


		
    }



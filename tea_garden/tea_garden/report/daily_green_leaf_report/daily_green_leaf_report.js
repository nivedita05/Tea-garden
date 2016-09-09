// Copyright (c) 2016, frappe and contributors
// For license information, please see license.txt
frappe.require("assets/js/daily_green_leaf_statement.js", function() { 
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
         }

	],


    "formatter": daily_green_leaf_statement.formatter,
    "tree":true,
    "name_fielde":"section",
    "parent_field":"division_name",
    "initial_depth":3
		
    }

});


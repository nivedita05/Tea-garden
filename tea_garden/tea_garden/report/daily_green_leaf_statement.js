frappe.provide("daily_green_leaf_statement");

daily_green_leaf_statement = {
	"filters": [
		{
			"fieldname":"date",
			"label": __("Date"),
			"fieldtype": "date",
			"options": "",
			"default": frappe.defaults.get_user_default("date"),
			"reqd": 1
		},
		{
			"fieldname":"estate_name",
			"label": __("Estate Name"),
			"fieldtype": "Link",
			"options": "Estate",
			"default": frappe.defaults.get_user_default("estate_name"),
			"reqd": 1
		},
		
	],
	"formatter": function(row, cell, value, columnDef, dataContext, default_formatter) {
		if (columnDef.df.fieldname=="Section") {
			value = dataContext.section_name;

			columnDef.df.link_onclick =
				"daily_green_leaf_statement.open_general_ledger(" + JSON.stringify(dataContext) + ")";
			columnDef.df.is_tree = true;
		}

		value = default_formatter(row, cell, value, columnDef, dataContext);

		if (!dataContext.division_id) {
			var $value = $(value).css("font-weight", "bold");
			if (dataContext.warn_if_negative && dataContext[columnDef.df.fieldname] < 0) {
				$value.addClass("text-danger");
			}

			value = $value.wrap("<p></p>").parent().html();
		}

		return value;
	},
	"open_general_ledger": function(data) {
		if (!data.section) return;

		frappe.route_options = {
			"date": date.date,
			"estate_name": data.estate_name
			
		};
		frappe.set_route("query-report", "General Ledger");
	},
	"tree": true,
	"name_field": "section",
	"parent_field": "division_name",
	"initial_depth": 3
	
};

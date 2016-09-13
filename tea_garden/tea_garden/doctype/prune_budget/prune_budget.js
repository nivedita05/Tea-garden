// Copyright (c) 2016, frappe and contributors
// For license information, please see license.txt

// naming series for prune budget

frappe.ui.form.on("Prune Budget", "validate", function(frm) {
    frm.budget_code="";
    name=frm.doc.estate_name+"-"+frm.doc.prune_type+"-"+frm.doc.bush_type;
    frm.set_value("budget_code",name);
});
   
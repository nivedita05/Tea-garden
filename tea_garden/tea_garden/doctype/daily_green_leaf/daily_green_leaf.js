// Copyright (c) 2016, frappe and contributors
// For license information, please see license.txt



// to get the date from parent table to child table//

frappe.ui.form.on("Daily Green Leaf", "validate", function(frm) {
  for(var i in frm.doc.leaf_details){
     frm.doc.leaf_details[i].date = frm.doc.date;
     }
  });


// naming series for daily green leaf

frappe.ui.form.on("Daily Green Leaf", "validate", function(frm) {
    frm.dgl_code="";
    name=frm.doc.estate_name+":"+frm.doc.date;
    frm.set_value("dgl_code",name);
});
   
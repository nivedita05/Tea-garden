// Copyright (c) 2016, frappe and contributors
// For license information, please see license.txt

//frappe.ui.form.on('Daily Green Leaf', {
//	refresh: function(frm) {

//	}
////});
//frappe.ui.form.on("Daily Green Leaf", "validate", function(frm) {
  //for(var section in frm.doc.leaf_details){
    // if(frm.doc.leaf_details[section].area && frm.doc.leaf_details[section].area >  frm.doc.leaf_details[section].section_area){
      //  msgprint("The area of the farm is : "+frm.doc.leaf_details[section].section_area);
        //validate=false;
     //}
    //}
  //});
frappe.ui.form.on("Daily Green Leaf", "validate", function(frm) {
  for(var i in frm.doc.leaf_details){
     frm.doc.leaf_details[i].date = frm.doc.date;
     }
  });
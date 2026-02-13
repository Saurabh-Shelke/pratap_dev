import frappe

def po_calculation_by_weight(doc, method):

    # 🔒 Run only when checkbox ON
    if not doc.custom_calculate_based_on_weight:
        return

    total_doc_amount = 0

    for item in doc.items:
        try:
            custom_rate = float(item.custom_rate_in_kg or 0)
            weight_per_unit = float(item.weight_per_unit or 0)
            qty = float(item.qty or 0)
            normal_rate = float(item.rate or 0)
        except Exception:
            continue

        # ==============================
        # 🟢 CASE 1 → Custom rate entered
        # ==============================
        if custom_rate > 0:

            if weight_per_unit > 0:
                final_rate = round(custom_rate * weight_per_unit, 2)
            else:
                final_rate = round(custom_rate, 2)

            final_amount = round(final_rate * qty, 2)

            # 🔥 Update all fields
            item.rate = final_rate
            item.net_rate = final_rate
            item.base_rate = final_rate
            item.base_net_rate = final_rate

            item.amount = final_amount
            item.net_amount = final_amount
            item.base_amount = final_amount
            item.base_net_amount = final_amount
            item.taxable_value = final_amount

            total_doc_amount += final_amount

        # ==============================
        # 🟡 CASE 2 → Custom rate = 0
        # 👉 Use normal ERPNext behaviour
        # ==============================
        else:
            normal_amount = round(normal_rate * qty, 2)
            total_doc_amount += normal_amount

    # ✅ Update doc totals
    doc.total = total_doc_amount
    doc.net_total = total_doc_amount
    doc.base_total = total_doc_amount
    doc.base_net_total = total_doc_amount

    frappe.msgprint("✅ Weight/custom pricing applied")















function set_opportunity_from_filter(frm) {
    frm.set_query("opportunity_from", () => {
        return {
            filters: {
                name: ["in", ["Customer", "Prospect"]],
            },
        };
    });
}

frappe.ui.form.on("Opportunity", {
    setup(frm) {
        set_opportunity_from_filter(frm);
    },
    refresh(frm) {
        set_opportunity_from_filter(frm);
    },
});
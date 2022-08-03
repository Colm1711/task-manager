document.addEventListener("DOMContentLoaded", function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    var datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmmmm, yyyy",
        i18n: {done: "Select"}
    });

    var selects = document.querySelectorAll('select');
    var instances = M.FormSelect.init(selects);
});
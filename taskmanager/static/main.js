/**
 * Created by gregory on 8/11/15.
 */

function initDateFields() {
    $('input.dateinput').datetimepicker({
        'format': 'YYYY-MM-DD',
        locale: 'uk'
    });
}
$(document).ready(function () {
    initDateFields();
});

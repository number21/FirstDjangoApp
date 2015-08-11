/**
 * Created by gregory on 8/11/15.
 */
function diffTime() {
    var ends = document.getElementsByClassName('end');
    var elapseds = document.getElementsByClassName('elapsed');
    for (i = 0; i < ends.length; i++) {
        var start = new Date();
        console.log(start);
        var end = new Date(ends.item(i).innerHTML);
        console.log(end);
        var diff = new Date(end.getTime() - start.getTime());
        var years = diff.getUTCFullYear() - 1970;
        var months = diff.getUTCMonth() - 1;
        var days = diff.getUTCDate() - 1;
        var hours = diff.getUTCHours();
        var minutes = diff.getUTCMinutes();
        var seconds = diff.getUTCSeconds();
        elapseds.item(i).innerHTML = "" + years + "р " + months + "м " + days + "д " + hours + "г " + minutes + "х " + seconds + "с ";
        t = setTimeout('diffTime()', 500);
    }

}
function initDateFields() {
    $('input.dateinput').datetimepicker({
        'format': 'YYYY-MM-DD',
        locale: 'uk'
    });
}
$(document).ready(function () {
    initDateFields();
    diffTime();
});

$j = django.jQuery

function get_lat_long() {
    var address = $j(this).val();
    $j.get(window.location.href + "../get_lat_long/?q=" + address, function(data, code) {
        $j("input#id_latitude").val(data.split(",")[2]);
        $j("input#id_longitude").val(data.split(",")[3]);
    });
}

$j(document).ready(function() {
    $j("textarea#id_address").blur(get_lat_long);
});

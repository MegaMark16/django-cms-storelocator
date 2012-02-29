$j = django.jQuery

try {
    get_lat_long_url = get_lat_long_url + '?q=';
}
catch(err) {
    get_lat_long_url = window.location.href + '../get_lat_long/?q=';
}

function get_lat_long() {
    var address = $j(this).val();
    $j.get(get_lat_long_url + address, function(data, code) {
        $j("input#id_latitude").val(data.split(",")[2]);
        $j("input#id_longitude").val(data.split(",")[3]);
    });
}

$j(document).ready(function() {
    $j("textarea#id_address").blur(get_lat_long);
});

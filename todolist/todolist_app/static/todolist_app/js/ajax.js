function fireAjax(url) {
    jQuery.ajax(
        url,
        {
            success: function(result) { location.reload(); }
        }
    );
}

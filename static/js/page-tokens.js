(function (jQuery) {
    function init() {
        $("#id_clear").click(function () {
            $('.csn-user-field-wrapper input').val("");
            $('.message-pane').hide();
            $('#id_reset_token').show();
            $(this).hide();
        });

        if (!$('#id_result').val()) {
            $('#id_clear').hide();
            $('#id_reset_token').show();
        } else {
            $('#id_clear').show();
            $('#id_reset_token').hide();
        }
    }

    $(document).ready(init);
})(jQuery);
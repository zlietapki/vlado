function upload_image() {
    $.ajax({
        url: location.pathname,
        type: "POST",
        data: new FormData($('#upload_form')[0]),
        processData: false,
        contentType: false
    }).done(function () {
        location.reload();
    }).fail(function () {
        location.reload();
    });
}

function del_image(image_path) {
    if (confirm("Delete image?")) {
        $.ajax({
            type: "POST",
            url: "/adm/delete-image",
            data: {
                "image_path": image_path,
            },
            success: function () {
                location.reload();
            }
        });
    }
}

$(document).ready(
    function () {
        $('#upload_file').change(
            function () {
                if ($(this).val()) {
                    $('#upload_button').removeAttr('disabled');
                }
            }
        );
    });

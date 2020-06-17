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
                    $('#upload_submit').removeAttr('disabled');
                }
            }
        );
    });

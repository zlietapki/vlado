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

$('#upload').on('click', function () {
    var file_data = $('#file-to-upload').prop('files')[0];
    var form_data = new FormData();
    form_data.append('file', file_data);
    alert(form_data);
    $.ajax({
        url: '/adm/upload', // point to server-side PHP script
        dataType: 'text',  // what to expect back from the PHP script, if anything
        cache: false,
        contentType: false,
        processData: false,
        data: form_data,
        type: 'post',
        success: function (php_script_response) {
            alert(php_script_response); // display response from the PHP script, if any
        }
    });
});

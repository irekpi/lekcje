// Append, Prepend, Remove, ADD attribute

$(document).ready(function () {
    $('#container1').on('click', 'button.switch', function () {
        $.ajax('result.html', {
            beforeSend: function () {
                $('.status').text('loading...');
            }
        })
            .done(function (response) {
                $('.result').html(response);
        })
            .fail(function (request, errorType, errorMessage) {
                alert(errorMessage);
                console.log(errorType)
            })
            .always(function () {
                $('.status').text('Completed');
            })
    });
    $.ajax('2.data.json', {
        dataType: 'json',
        contentType: 'application/json',
    })
        .done(function (response) {
            console.log(response);
        })
    var cart = 0
    $('.adder').on('click', '.container-adder button', function (event) {
        event.preventDefault();
        var object_id = +$(this).closest('.container-adder').data('id');
        $.ajax('additem.json', {
            type: 'post',
            data: {id: object_id},
            dataType: 'json',
            contentType: 'application/json',
            })

            .done(function (response) {
                console.log(response)
                cart += response.number_2
                $('.total-cost').text('total cost' + cart)

            })

    });
});
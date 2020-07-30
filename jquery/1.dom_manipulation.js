// Append, Prepend, Remove, ADD attribute

$(document).ready(function () {
    $('#add-container').on('click', 'button', function () {
        var value = $('#add-container input').val();
        console.log(value);
        var html = '<div class="item" style="width: 150px">\
            <div class="remove" style="float:right">x</div>' + value + '</div>';
        console.log(html)

        // Append as last element
        $('#places-container').append(html);
        // $(html).appendTo('#places-container');

        //Prepend as first element
        // $('#places-container').prepend(html);
        // $(html).prependTo('#places-container');
    });

    $('#places-container').on('click', '.remove', function () {
        $(this).parent().remove();
    });

    $('#container').html('New Joker')

    $('#container1').on('click', 'a.info-link', function (event) {
        event.preventDefault();
        $(this).closest('#container1').find('.more-info').toggle();
    });

});
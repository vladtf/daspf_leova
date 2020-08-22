window.jQuery = window.$ = require('jquery');

import '../scss/main.scss';

import 'bootstrap';
import 'popper.js';

import './fit-text'


if (document.getElementById('id_body') !== null) {
    CKEDITOR.replace('id_body', {
        extraPlugins: ['autogrow', 'indentlist', 'image2'],
    });
}

$('.carousel').on('slide.bs.carousel', function (event) {
    var height = $(event.relatedTarget).height();
    var $innerCarousel = $(event.target).find('.carousel-inner');

    $innerCarousel.animate({
        height: height
    });
});

$('.sidebar-card-text').fitText();


let form_count = Number($("[name=form-TOTAL_FORMS]").val());

$("#add_extra").click(function () {

    let image_field = $(
        '<div class="col-md-12 py-2 form-group image-field">' +
        '<label for="id_form-' + form_count + '-image">Image: </label>' +
        '<input type="file" name="form-' + form_count + '-image" accept="image/*" id="id_form-' + form_count + '-image">' +
        '<input type="hidden" name="form-' + form_count + '-id" id="id_form-' + form_count + '-id">' +
        '</div>'
    );

    $('.image-field').last().after(image_field);

    $("[name=form-TOTAL_FORMS]").val(++form_count);
});


$("textarea").each(function (textarea) {
    $(this).height($(this)[0].scrollHeight);

    $(this).on("keydown keypress change", function () {
        $(this).height(0);
        $(this).height(this.scrollHeight+30);
    })
});

// $('.my-image').croppie({
//     viewport: {
//         width: 150,
//         height: 150
//     },
//     boundary: {
//         width: 300,
//         height: 300,
//     }
// });
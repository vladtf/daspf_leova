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
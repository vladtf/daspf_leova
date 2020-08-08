import '../scss/main.scss';

import 'bootstrap';
import 'popper.js';

window.jQuery = window.$ = require('jquery');


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

// tinymce.init({selector: 'textarea'});

if (document.getElementById('id_body') !== null) {
    CKEDITOR.replace('id_body', {
        extraPlugins: ['autogrow', 'image2', 'indentlist']
    });
}

$('.carousel').on('slide.bs.carousel', function (event) {
    var height = $(event.relatedTarget).height();
    var $innerCarousel = $(event.target).find('.carousel-inner');

    $innerCarousel.animate({
        height: height
    });
});
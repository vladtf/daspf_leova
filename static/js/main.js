window.jQuery = window.$ = require('jquery');

require("jquery-ui/ui/widgets/dialog");

import '../scss/main.scss';

import 'bootstrap';
import 'popper.js';

import './fit-text'


function setupCKEditor() {
    if ($("#id_body").length) {
        CKEDITOR.replace('id_body', {
            extraPlugins: ['autogrow', 'indentlist', 'image2'],
        });
    }
}

function updateImagesSliderHeight() {
    $('.carousel').on('slide.bs.carousel', function (event) {
        var height = $(event.relatedTarget).height();
        var $innerCarousel = $(event.target).find('.carousel-inner');

        $innerCarousel.animate({
            height: height
        });
    });
}

function addExtraImagesField() {
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
}

function updateTextAreaHeight() {
    $("textarea").each(function (textarea) {
        $(this).height($(this)[0].scrollHeight);

        $(this).on("keydown keypress change", function () {
            $(this).height(0);
            $(this).height(this.scrollHeight + 30);
        })
    });
};


function configCaptcha() {
    $('.captcha').click(function () {
        update_captcha()
    });

    $('#id_captcha_1').after('<button class=\'js-captcha-refresh btn btn-outline-danger ml-2\' type="button" id="re_captcha"><i class="fas fa-undo"></i></button>')
    $('#re_captcha').click(function () {
        update_captcha()
    })
}

function update_captcha() {
    $.getJSON("/captcha/refresh/", function (result) {
        $('.captcha').attr('src', result['image_url']);
        $('#id_captcha_0').val(result['key'])
    });
}

function setMapWidget() {
    if ($('#mapid').length) {
        var mymap = L.map('mapid').setView([46.47715, 28.249547], 16);

        mymap.addControl(new L.Control.Fullscreen());

        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        }).addTo(mymap);

        var marker = L.marker([46.47715, 28.249547]).addTo(mymap);
        marker.bindPopup("Directia Asistenta Sociala Leova");
    }
}

$('#hide-editor-check').click(function () {
    $('#edit-form').toggle(400)
});

$('#hide-check').click(function () {
    $('.admin-control').toggle(400)
});

$("#scroll-top").click(function () {
    $("html, body").stop().animate({scrollTop: 0}, 500, 'linear');
    return false;
});

function showScrollButton() {
    var button = $('#scroll-top');
    var timeoutKey = -1;
    var view = $(window);

    $(document).scroll(function () {
        if (timeoutKey) {
            window.clearTimeout(timeoutKey);
        }

        timeoutKey = window.setTimeout(function () {
            if (view.scrollTop() < 50) {
                button.fadeOut();
            } else {
                button.fadeIn();
            }
        }, 100);
    });
}


$(function () {
    $('.sidebar-card-text').fitText();

    $('#btnDelete').click(function () {
        $('#dialog').dialog();
        return false;
    });

    showScrollButton();
    updateTextAreaHeight();
    setupCKEditor();
    updateImagesSliderHeight();
    addExtraImagesField();
    configCaptcha();
    setMapWidget();
});
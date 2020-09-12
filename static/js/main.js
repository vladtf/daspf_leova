const dialog = require('jquery-ui/dialog');

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

function findActiveLinks() {
    var path = window.location.pathname
    $("a.nav-link[href='" + path + "']").addClass('active');
}

function sidebarCardFitText() {
    $('.sidebar-card-text').fitText();
}

function scrollToTop() {
    $("#scroll-top").click(function () {
        $("html, body").stop().animate({scrollTop: 0}, 500, 'linear');
        return false;
    });
}

function hideAdminButtons() {
    $('#hide-editor-check').click(function () {
        $('#edit-form').toggle(400)
    });

    $('#hide-check').click(function () {
        $('.admin-control').toggle(400)
    });
}

function openDeleteDialog() {
    $('#btnDelete').click(function () {
        $('#dialog').dialog({
            buttons: [
                {
                    text: "Șterge",
                    class: "btn btn-outline-danger",
                    click: function () {
                        var form = $('#post_form');
                        var post_id = form.find('input[name="post_id"]').val();
                        var url = form.find('input[name="post_delete_url"]').val();
                        var csrf_token = form.find('input:first').val();

                        var action = window.location.pathname.split('/').pop();

                        var form_data = {
                            'post_id': post_id,
                            'action': action
                        }

                        console.log(post_id, action, csrf_token);

                        $.ajax({
                            method: 'POST',
                            url: url,
                            headers: {
                                'Content-Type': 'application/json',
                                'X-CSRFToken': csrf_token,
                            },
                            data: JSON.stringify(form_data),
                            success: function (response) {
                                console.log(response);

                                var message = response.message;
                                var redirect = response.redirect;

                                alert(message);

                                window.location.href = redirect;
                            },
                            error: function () {
                                alert("Error on server side!");
                            }
                        });
                    }
                },
                {
                    text: "Renunță",
                    class: "btn btn-outline-secondary",
                    click: function () {
                        $(this).dialog("close");
                    }
                }
            ]
        });
        return false;
    });
}

function fitOverflowedImage() {
    $(window).on('load resize', function () {
        $('.index-view').find('img').each(function () {
            var imageWidth = $(this).width();
            var parentWidth = $(this).parent().width();

            console.log("Image width: " + imageWidth);
            console.log("Parent width: " + parentWidth);

            if (imageWidth > parentWidth) {
                $(this).css({
                    "height": "100%",
                    "width": "100%",
                    "object-fit": "contain"
                });
            }
        });
    });
}

$(function () {

    fitOverflowedImage();
    openDeleteDialog();
    hideAdminButtons();
    scrollToTop();
    sidebarCardFitText();
    showScrollButton();
    updateTextAreaHeight();
    setupCKEditor();
    updateImagesSliderHeight();
    addExtraImagesField();
    configCaptcha();
    setMapWidget();
    findActiveLinks();

});
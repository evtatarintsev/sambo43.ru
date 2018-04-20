$(document).ready(function(){

    $('.fancybox').fancybox();

    $('.index-slider-box').slick({
        infinite: true,
        dots: true,
        customPaging : function(slider, i) {
            var thumb = $(slider.$slides[i]).data();
            return '<a href="#"></a>';
        },
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        appendDots: '.index-slider-dots'
    });

    $('.slider-box').slick({
        infinite: true,
        dots: true,
        customPaging : function(slider, i) {
            var thumb = $(slider.$slides[i]).data();
            return '<a href="#"></a>';
        },
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        appendDots: '.index-slider-dots'
    });

    $('.js-slider-preson-detail').slick({
        infinite: true,
        slidesToShow: 6,
        dots: false,
        slidesToScroll: 6,
        arrows: true,
    });


    $('.catalog-category').click(function(){
       $(this).parent().toggleClass('_active');

       return false;
    });

    $('.tabs-tab').click(function () {
        $('.tabs-tab').removeClass('_active');
        $('.tab-content').removeClass('_active');

        var selectedTabClass = $(this).attr('id');

        $(this).addClass('_active');
        $('.'+selectedTabClass).addClass('_active');

        return false;
    });


});
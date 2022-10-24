var owl = $('.owl-carousel');
owl.owlCarousel({
    items: 1,
    loop:true,
    margin:10,
    // nav:true,
    autoplay: true,
    autoplayTimeout:5000,
    autoplayHoverPause:true,
    responsive:{
        0:{
            items:1,
        },
        875:{
            items:2
        },
        1000:{
            items:3
        }
    }
})

// $(document).ready(function() {
//     //responsive menu toggle
//     $("#menutoggle").click(function() {
//         $('.xs-menu').toggleClass('displaynone');

//         });
    
//     //drop down menu	
//         $(".drop-down").hover(function() {
//             $('.mega-menu').addClass('display-on');
//         });
//         $(".drop-down").mouseleave(function() {
//             $('.mega-menu').removeClass('display-on');
//         });
// });
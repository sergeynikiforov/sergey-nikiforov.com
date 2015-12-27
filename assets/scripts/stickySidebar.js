// sticky sidebar on photoset page
//
//

var StickySidebar = {};

// helper switches
StickySidebar.isSetUp = false;
StickySidebar.isTopBarSetUp = false;
StickySidebar.isSidebarFixed = false;
StickySidebar.isSidebarBottom = false;

// helper functions

StickySidebar.changeTopBarBackgroundColor = function () {
    $('#top-bar-wrapper > div').toggleClass('white-bg');
    $('#top-bar-wrapper > .fixed').css('height', '70px');
}

StickySidebar.addTopBarBackgroundColor = function () {
    $('#top-bar-wrapper > div').addClass('white-bg');
    $('#top-bar-wrapper > .fixed').css('height', '70px');
    $('#navigation-bar').removeClass('black-color');
}

StickySidebar.removeTopBarBackgroundColor = function () {
    $('#top-bar-wrapper > div').removeClass('white-bg');
    $('#top-bar-wrapper > .fixed').css('height', 'auto');
}


// add fixed classes to sidebar
StickySidebar.makeSidebarFixed = function() {
    $('#fixed-wrapper').addClass('fixed-sidebar');
    $('#thumbs-wrapper > div').addClass('large-offset-4');
    $('#sidebar-wrapper').removeClass('content-down');
    StickySidebar.isSidebarFixed = true;
    StickySidebar.setStickySidebarColumnMargins();
}

// remove fixed classes from sidebar
StickySidebar.makeSidebarUnFixed = function() {
    $('#fixed-wrapper').removeClass('fixed-sidebar');
    $('#thumbs-wrapper > div').removeClass('large-offset-4');
    StickySidebar.isSidebarFixed = false;
    StickySidebar.setStickySidebarColumnMargins();
}

// place sidebar on the bottom of its container
StickySidebar.placeSidebarBottom = function() {
    $('#sidebar-wrapper').addClass('content-down');
    StickySidebar.isSidebarBottom = true;
}

// lift sidebar from the bottom of its container
StickySidebar.liftSidebarFromBottom = function() {
    $('#sidebar-wrapper').removeClass('content-down');
    StickySidebar.isSidebarBottom = false;
}

// sets sidebar wrapper column equal to thumbs height
StickySidebar.setStickySidebarColumnHeight = function () {
    StickySidebar.thumbsHeight = $('#thumbs').outerHeight();
    $('#fixed-wrapper > div').outerHeight(StickySidebar.thumbsHeight);
}

// sets margin-left of the sidebar, called on ready, resize, make sidebar fixed/unfixed
StickySidebar.setStickySidebarColumnMargins = function () {

    // initial assingments, align with top-bar left
    StickySidebar.stickySidebarColumnLeftMargin = $('#header-wrapper').offset().left;
    StickySidebar.stickySidebarColumnLeftMarginLargeScreensOffset = $('#make-fixed > div').offset().left;

    // if sidebar is fixed
    if (StickySidebar.isSidebarFixed) {
        $('#fixed-wrapper > div').attr('style', 'margin-left:' + (StickySidebar.stickySidebarColumnLeftMargin - StickySidebar.stickySidebarColumnLeftMarginLargeScreensOffset) + 'px !important;');
    } else { // if sidebar is not fixed
        $('#fixed-wrapper > div').css('margin-left', 'auto');
    };
}

// function is called whenever we scroll or resize
StickySidebar.stickySidebar = function() {

    StickySidebar.makeFixedTop = $('#make-fixed').offset().top;
    StickySidebar.makeFixedBottom = $('#make-fixed').offset().top + $('#make-fixed').outerHeight();

    if (StickySidebar.isSidebarFixed) {
        // we touched the bottom
        if (StickySidebar.topbarBottom + StickySidebar.sidebarContentHeight > StickySidebar.makeFixedBottom) {
            StickySidebar.makeSidebarUnFixed();
            StickySidebar.placeSidebarBottom();
        }

        // we reached the top
        if (StickySidebar.topbarBottom < StickySidebar.makeFixedTop) {
            StickySidebar.makeSidebarUnFixed();
        };

    } else { // NOT fixed

        if (StickySidebar.isSidebarBottom) {
            if (StickySidebar.topbarBottom + StickySidebar.sidebarContentHeight < StickySidebar.makeFixedBottom) {
                StickySidebar.makeSidebarFixed();
                StickySidebar.liftSidebarFromBottom();
            };

        // sidebar NOT bottom
        } else {
            if (StickySidebar.topbarBottom > StickySidebar.makeFixedTop && StickySidebar.topbarBottom + StickySidebar.sidebarContentHeight < StickySidebar.makeFixedBottom) {
                StickySidebar.makeSidebarFixed();
            }
        };
    };
}

// set up top bar for sticky sidebar, depending on its position and viewport width
StickySidebar.setUpTopBar = function() {


    // set a non-transparent bg for large screens, otherwise - remove whatever color it was
    if (window.innerWidth > 1024) {

        StickySidebar.topbarBottom = $('#top-bar-wrapper > div').offset().top + $('#top-bar-wrapper > div').outerHeight();
        StickySidebar.topbarMarker = $('#change-bg').offset().top + $('#change-bg').outerHeight();

        // if it's lower than the mark - set new bg, else - remove color
        if (StickySidebar.topbarBottom >= StickySidebar.topbarMarker) {
            StickySidebar.addTopBarBackgroundColor();
            StickySidebar.isTopBarSetUp = true;
        } else {
            StickySidebar.removeTopBarBackgroundColor();
            StickySidebar.isTopBarSetUp = false;
        };
    } else {
        StickySidebar.removeTopBarBackgroundColor();
        StickySidebar.isTopBarSetUp = false;
    };

}


// called on ready & on resize
StickySidebar.setUpStickySidebar = function() {

    // set it only on large screens && on page with thumbs & sidebar-wrapper
    if ($('#sidebar-wrapper').length > 0 && $('#thumbs').length > 0 && window.innerWidth > 1024) {

        // set content height, used in stickySidebar()
        StickySidebar.sidebarContentHeight = $('#sidebar-wrapper > div').outerHeight();

        // call set-up functions
        StickySidebar.setUpTopBar();
        StickySidebar.setStickySidebarColumnHeight();
        StickySidebar.setStickySidebarColumnMargins();
        StickySidebar.stickySidebar();

        // switch on
        StickySidebar.isSetUp = true;

    } else {
        StickySidebar.isSetUp = false;
    };
}

$(document).ready(function() {
    // when ready, try to set up sticky sidebar
    StickySidebar.setUpStickySidebar();

    // if sidebar is set up - listen for scroll events
    $(document).on('scroll', function() {
        if (StickySidebar.isSetUp) {
            StickySidebar.setUpTopBar();
            StickySidebar.setStickySidebarColumnHeight();
            StickySidebar.stickySidebar();
        };
    });

    // when resized - set up again
    $(window).on('resize', function() {
        StickySidebar.setUpStickySidebar();
        StickySidebar.setUpTopBar();
        Waypoint.refreshAll();
    });
});
require('es6-promise').polyfill();
var gulp = require('gulp');
var sass = require('gulp-sass');
var watch = require('gulp-watch');
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var gzip = require('gulp-gzip');
var livereload = require('gulp-livereload');
var plumber = require('gulp-plumber');
var concat = require('gulp-concat');
var merge = require('merge-stream');
var autoprefixer = require('gulp-autoprefixer');
var uglify = require('gulp-uglify');
var minify = require('gulp-minify');

var gzip_options = {
    threshold: '1kb',
    gzipOptions: {
        level: 9
    }
};

// paths for bower and assets
var paths = {
    'bower': './bower_components',
    'assets': './assets'
}

// error handler for plumber
var onError = function (err) {
  console.log(err);
  this.emit('end');
};

gulp.task('sass', function() {
    // get sass stream
    var sassStream = gulp.src([
            paths.assets + '/styles/app.scss'
                    ])
    // plumber for error handling
    .pipe(plumber({
        errorHandler: onError
    }))
    // run through sass compiler, passing foundation scss in includePaths
    .pipe(sass({
          includePaths: [
            paths.bower + '/foundation/scss'
          ]
    }));

    // get css stream
    var cssStream = gulp.src([
          ]);

    // merge two streams
    return merge(sassStream, cssStream)
    // concat css files
    .pipe(concat('app.min.css'))
    // run through autoprefixer
    .pipe(autoprefixer())
    // minify
    .pipe(minifycss())
    // put into destination dir
    .pipe(gulp.dest('./sn_app/static/sn_app/css'))
    // run reload
    .pipe(livereload());
});

// gulp task for js scripts
gulp.task('scripts', function() {
    // include all the needed js files
    return gulp.src([
            paths.bower + '/fastclick/lib/fastclick.js',
            paths.bower + '/foundation/js/foundation.js',
            paths.bower + '/foundation/js/foundation/foundation.alert.js',
            paths.bower + '/waypoints/lib/jquery.waypoints.js',
            paths.assets + '/scripts/jquery.mobile.custom.js',
            paths.assets + '/scripts/app.js'
            //paths.assets + '/scripts/myStickyFooter.js',
             ])
    // concat into 1 file
    .pipe(concat('app.min.js'))
    // uglify
    .pipe(uglify())
    // put into dest dir
    .pipe(gulp.dest('./sn_app/static/sn_app/js'))
    // run reload
    .pipe(livereload());
});

gulp.task('photoapp', function() {
    // include all the needed js files
    return gulp.src([
            paths.bower + '/underscore/underscore.js',
            paths.bower + '/backbone/backbone.js',
            paths.assets + '/scripts/photoApp.js'
             ])
    .pipe(plumber({
        errorHandler: onError
    }))
    // concat into 1 file
    .pipe(concat('photoapp.min.js'))
    // uglify
    .pipe(uglify())
    // put into dest dir
    .pipe(gulp.dest('./sn_app/static/sn_app/js'))
});

gulp.task('modernizr', function() {
    // include all the needed js files
    return gulp.src([
            paths.bower + '/modernizr/modernizr.js'
             ])
    .pipe(plumber({
        errorHandler: onError
    }))
    // concat into 1 file
    .pipe(concat('modernizr.min.js'))
    // uglify
    .pipe(uglify())
    // put into dest dir
    .pipe(gulp.dest('./sn_app/static/sn_app/js'))
});

gulp.task('sidebar', function() {
    // include all the needed js files
    return gulp.src([
            paths.assets + '/scripts/stickySidebar.js'
             ])
    .pipe(plumber({
        errorHandler: onError
    }))
    // concat into 1 file
    .pipe(concat('stickysidebar.min.js'))
    // uglify
    .pipe(uglify())
    // put into dest dir
    .pipe(gulp.dest('./sn_app/static/sn_app/js'))
});

// livereload task
gulp.task('reload', function() {
    return livereload.reload();
});

// watch task
gulp.task('watch', function() {
    livereload.listen();
    gulp.watch(paths.assets + '/**/**/*.{scss,js,css,html}', ['sass', 'modernizr', 'scripts', 'sidebar', 'photoapp']);
    gulp.watch('sn_app/templates/sn_app/*.html', ['reload']);
});

// default task
gulp.task('default', ['sass', 'modernizr', 'scripts', 'sidebar', 'photoapp']);

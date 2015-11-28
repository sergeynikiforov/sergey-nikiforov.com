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
          paths.assets + '/styles/owl.carousel.css',
          paths.assets + '/styles/owl.theme.css',
          paths.assets + '/styles/owl.transitions.css'
          ]);

    // merge two streams
    return merge(sassStream, cssStream)
    // concat css files
    .pipe(concat('app.css'))
    // run through autoprefixer
    .pipe(autoprefixer())
    // put into destination dir
    .pipe(gulp.dest('./sn_app/static/sn_app/css'))
    // run reload
    .pipe(livereload());
});

// gulp task for js scripts
gulp.task('scripts', function() {
    // include all the needed js files
    return gulp.src([
            paths.bower + '/jquery/dist/jquery.js',
            paths.bower + '/fastclick/lib/fastclick.js',
            paths.bower + '/foundation/js/foundation.js',
            paths.bower + '/foundation/js/foundation/foundation.alert.js',
            paths.bower + '/underscore/underscore.js',
            paths.bower + '/backbone/backbone.js',
            paths.bower + '/cloudinary-jquery/cloudinary-jquery.js',
            paths.assets + '/scripts/app.js',
            paths.assets + '/scripts/myStickyFooter.js',
            paths.assets + '/scripts/owl.carousel.js',
            paths.assets + '/scripts/photoApp.js'
             ])
    // concat into 1 file
    .pipe(concat('app.js'))
    // put into dest dir
    .pipe(gulp.dest('./sn_app/static/sn_app/js'))
    // run reload
    .pipe(livereload());
});

// livereload task
gulp.task('reload', function() {
    return livereload.reload();
});

// watch task
gulp.task('watch', function() {
    livereload.listen();
    gulp.watch(paths.assets + '/**/**/*.{scss,js,css,html}', ['sass', 'scripts']);
    gulp.watch('sn_app/templates/sn_app/*.html', ['reload']);
});

// default task
gulp.task('default', ['sass', 'scripts']);

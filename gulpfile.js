var gulp = require('gulp');
var sass = require('gulp-sass');
var watch = require('gulp-watch');
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var gzip = require('gulp-gzip');
var livereload = require('gulp-livereload');

var gzip_options = {
    threshold: '1kb',
    gzipOptions: {
        level: 9
    }
};

gulp.task('sass', function() {
    return gulp.src([
            './assets/styles/app.scss'
                    ])
    .pipe(sass({
          includePaths: [
          './bower_components/foundation/scss'
          ]
    }))
    .pipe(rename('app.css'))
    .pipe(gulp.dest('./sn_app/static/sn_app/css'));
});

gulp.task('watch', function() {
    gulp.watch('./assets/styles/**/*.scss', ['sass']);
});

gulp.task('default', ['sass']);

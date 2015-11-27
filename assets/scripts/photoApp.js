// set up cloudinary
var CLOUD_NAME = 'sergeynikiforov';
//var cl = cloudinary.Cloudinary.new();
$.cloudinary.config({"cloud_name": CLOUD_NAME, "cdn_subdomain": true, "secure": true});
var cl = $.cloudinary;
//cl.config("cdn_subdomain", true);
//cl.config("secure", true);
var SRCSET = '200w 400w 600w 800w 1000w 1200w 1400w 1600w 2000w 2400w 2800w 3200w'.split(' ');
var SIZES = '(min-width: 1025px) 80vw, (min-width: 641px) 90vw, 100vw';

function srcsetWebp(publicID) {
    var result = '';
    var width = null;
    var clUrl = '';
    for (var i=0; i<SRCSET.length; i++) {
        width = parseInt(SRCSET[i].slice(0, -1));
        clUrl = cl.url(publicID, { width: width, crop: "fill", format: "webp", quality: 85});
        result = result.concat(clUrl+' '+width+', ');
    }
    return result.slice(0, -2);
}

function srcsetJpg(publicID) {
    var result = '';
    var width = null;
    var clUrl = '';
    for (var i=0; i<SRCSET.length; i++) {
        width = parseInt(SRCSET[i].slice(0, -1));
        clUrl = cl.url(publicID, { width: width, crop: "fill", format: "jpg", quality: 85});
        result = result.concat(clUrl+' '+width+', ');
    }
    return result.slice(0, -2);
}

// define Backbone.Model
var PhotoModel = Backbone.Model.extend({
    //initialize: function() {
    //    this.url = document.location.pathname +'api/photos/'+this.id
    //},
    initialize: function(id) {
        this.attributes.id = id;
    },
    collection: PhotoCollection,
    defaults: {
            id: null,
            photoset: null,
            title: null,
            description: null,
            srcsetWebp: null,
            srcsetJpg: null,
            imgSrc: null,
            prev_photoID: null,
            next_photoID: null,
            sizes: SIZES
        }
});

var PhotoCollection = Backbone.Collection.extend({
    model: PhotoModel,
    url: document.location.pathname +'api/photos/'
});


// view for photo
var PhotoView = Backbone.View.extend({
    el: '#photo-wrapper',
    template: _.template($('#photo-item-tmpl').html()),
    initialize: function() {
        this.listenTo(this.model, 'sync change', this.render);
        this.model.fetch();
        this.render();
    },
    render: function() {
        var html = this.template(this.model.toJSON());
        this.$el.html(html);
        return this;
    }
});

//var collection = new PhotoCollection();
//var photo = new PhotoModel('yhtla86f8wrkzbcqnad1');
//collection.add(photo);
//var photoView = new PhotoView({model: photo, collection: collection});

var PhotoRouter = Backbone.Router.extend({

    routes: {
        ':id': 'showPhoto'
    },
    showPhoto: function(id) {
        var collection = new PhotoCollection();
        var photo = new PhotoModel(id);
        collection.add(photo);
        var photoView = new PhotoView({model: photo});
        console.log(id);
    }

});

var appRouter = new PhotoRouter();

// Start Backbone history
Backbone.history.start();

/*

var PhotoRouter = Backbone.Router.extend({

    routes: {
        ':id': 'showPhoto'
    },
    showPhoto: function(id) {
        var photo = new PhotoModel(id);
        var photoView = new PhotoView({model: photo});
        console.log(id);
    }

});

var appRouter = new PhotoRouter();

// Start Backbone history
Backbone.history.start();



// define Backbone.Collection of PhotoModel-s
var PhotosCollection = Backbone.Collection.extend({
    model: PhotoModel,
    url: '/sn_app/'
});

var PhotosetModel = Backbone.Model.extend({
    initialize: function() {
        this.
    },
    defaults: {
        cover: null,
        title: null,
        description: null
    }
});
*/
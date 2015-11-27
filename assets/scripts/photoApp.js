var SIZES = '(min-width: 1025px) 80vw, (min-width: 641px) 90vw, 100vw';

var App = {};

// define Backbone.Model
App.PhotoModel = Backbone.Model.extend({

    initialize: function(id) {
        this.url = document.location.pathname + 'api/photos/' + id;
    },
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


App.PhotoCollection = Backbone.Collection.extend({
    model: App.PhotoModel,
    url: document.location.pathname + '/api/photos/',
    parse: function(data) {
        return data.models;
    }
});


App.PhotoView = Backbone.View.extend({
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


App.DescriptionView = Backbone.View.extend({
    el: '#photo-description-wrapper',
    template: _.template($('#photo-description-tmpl').html()),
    initialize: function() {
        this.listenTo(this.model, 'sync change', this.render);
        this.render();
    },
    render: function() {
        var html = this.template(this.model.toJSON());
        this.$el.html(html);
        return this;
    }
});


App.TitleView = Backbone.View.extend({
    el: '#photo-title-wrapper',
    template: _.template($('#photo-title-tmpl').html()),
    initialize: function() {
        this.listenTo(this.model, 'sync change', this.render);
        this.render();
    },
    render: function() {
        var html = this.template(this.model.toJSON());
        this.$el.html(html);
        return this;
    }
});


App.GeneralView = Backbone.View.extend({
    el: 'body',
    initialize: function() {
        this.router = new App.PhotoRouter();
    },
    events: {
        'click #next': 'changePhoto',
        'click #prev': 'changePhoto'
    },
    changePhoto: function(event) {
        event.preventDefault();
        if (event.target.id == 'next') {
            this.router.navigate(App.photo.attributes.next_photoID, true);
        } else {
            this.router.navigate(App.photo.attributes.prev_photoID, true);
        };
    }
});


App.PhotoRouter = Backbone.Router.extend({
    routes: {
        ':id': 'showPhoto'
    },
    showPhoto: function(id) {
        App.photo = new App.PhotoModel(id);
        App.photoView = new App.PhotoView({model: App.photo});
        App.photoDescrView = new App.DescriptionView({model: App.photo});
        App.photoTitleView = new App.TitleView({model: App.photo});
    }
});


$(function() {
    App.app = new App.GeneralView();
    App.hist = Backbone.history.start();
});

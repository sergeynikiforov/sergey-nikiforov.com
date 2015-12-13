var SIZES = '(min-width: 1025px) 80vw, 100vw';

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
            year: null,
            order: null,
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
        //this.model.fetch();
        this.render();
    },
    render: function() {
        var html = this.template(this.model.toJSON());
        this.$el.html(html);
        return this;
    }
});


App.OrderView = Backbone.View.extend({
    el: '#order-wrapper',
    template: _.template($('#order-tmpl').html()),
    initialize: function() {
        this.listenTo(this.model, 'sync change', this.render);
        //this.model.fetch();
        this.render();
    },
    render: function() {
        var html = this.template(this.model.toJSON());
        this.$el.html(html);
        return this;
    }
});


App.DescriptionView = Backbone.View.extend({
    medium: '#medium-photo-description-wrapper',
    large: '#large-photo-description-wrapper',
    template: _.template($('#photo-description-tmpl').html()),
    initialize: function() {
        this.listenTo(this.model, 'sync change', this.render);
        this.render();
    },
    render: function() {
        if (this.model.toJSON().description != 'No description') {
            var html_medium = this.template(this.model.toJSON());
            var html_large = html_medium;
        }
        else {
            var html_medium = '<p> </p>';
            var html_large = html_medium;
        }
        $(this.medium).html(html_medium);
        $(this.large).html(html_large);
        return this;
    }
});

// render two templates - for tap & top bars
App.TitleView = Backbone.View.extend({
    large_title: '#large-title-wrapper',
    tab_bar: '#tab-bar-title-wrapper',
    template_large_title: _.template($('#large-photo-title-tmpl').html()),
    template_TAB_bar: _.template($('#tab-bar-photo-title-tmpl').html()),
    initialize: function() {
        this.listenTo(this.model, 'sync change', this.render);
        this.render();
    },
    render: function() {
        /*
        if (this.model.toJSON().title != 'Untitled') {
            var html = this.template(this.model.toJSON());
        }
        else {
            var html = '';
        }
        */
        //this.model.attributes.title = this.model.attributes.title.toUpperCase();
        var html_large_title = this.template_large_title(this.model.toJSON());
        var html_TAB_bar = this.template_TAB_bar(this.model.toJSON());
        $(this.large_title).html(html_large_title);
        $(this.tab_bar).html(html_TAB_bar);
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
        if (event.target.id == 'next') {
            this.router.navigate(App.photo.attributes.next_photoID, true);
        } else {
            this.router.navigate(App.photo.attributes.prev_photoID, true);
        }
    }
});


App.PhotoRouter = Backbone.Router.extend({
    routes: {
        ':id': 'showPhoto'
    },
    showPhoto: function(id) {
        App.photo = new App.PhotoModel(id);
        App.photo.fetch({
            success: function() {
                App.photoView = new App.PhotoView({model: App.photo});
                App.orderView = new App.OrderView({model: App.photo});
                App.photoTitleView = new App.TitleView({model: App.photo});
                App.photoDescrView = new App.DescriptionView({model: App.photo});
                }
            });
    }
});


$(function() {
    App.app = new App.GeneralView();
    App.hist = Backbone.history.start();
});

var App = {};

App.SIZES = '(min-width: 1025px) 80vw, 100vw';

// transition functions (http://mikefowler.me/)
App.transitionIn = function (passedview, callback) {

  var view = passedview, delay;

  var transitionIn = function() {
    view.$el.addClass('is-visible');
    view.$el.one('transitionend', function() {
      if (_.isFunction(callback)) {
        callback();
      }
    })
  };

  _.delay(transitionIn, 20);

}

App.transitionOut = function(passedview, callback) {

  var view = passedview;

  view.$el.removeClass('is-visible');
  view.$el.one('transitionend', function() {
    if (_.isFunction(callback)) {
      callback();
    };
  });
}


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
            sizes: App.SIZES
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
        this.render();
        // transitionIn only once loaded
        $('#photo-wrapper img').load(function() {
            App.transitionIn(App.photoView, null);
        });
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
        this.render();
    },

    render: function() {
        var html = this.template(this.model.toJSON());
        this.$el.html(html);
        return this;
    }
});


App.DescriptionView = Backbone.View.extend({
    el: '#large-photo-description-wrapper',
    template: _.template($('#photo-description-tmpl').html()),

    initialize: function() {
        this.render();
    },

    render: function() {
        var model_json = this.model.toJSON();
        if (model_json.description != 'No description') {
            var html_large = this.template(model_json);
        }
        else {
            model_json.description = '';
            var html_large = this.template(model_json);

        }
        this.$el.html(html_large);
        return this;
    }
});

// render two templates - for tap & top bars
App.TitleView = Backbone.View.extend({
    el: '#large-title-wrapper',
    template_large_title: _.template($('#large-photo-title-tmpl').html()),

    initialize: function() {
        this.render();
    },

    render: function() {
        var html_large_title = this.template_large_title(this.model.toJSON());
        this.$el.html(html_large_title);
        return this;
    }
});

App.ErrorView = Backbone.View.extend({
    el: '#error-wrapper',
    err_string: '<div id="error" class="row">
                    <div class="small-12 medium-10 medium-centered text-left columns">
                        <p class="photo-error-msg">Sorry, I haven\'t taken this photo yet...</p>
                    </div>
                </div>',
    initialize: function() {
        this.render();
    },

    render: function() {
        this.$el.html(this.err_string);
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
            // first tramsitionOut, then navigate
            App.transitionOut(App.photoView, function(){
                App.app.router.navigate(App.photomodel.attributes.next_photoID, true);
            });
        } else {
            App.transitionOut(App.photoView, function() {
                App.app.router.navigate(App.photomodel.attributes.prev_photoID, true);
            });
        }
    }
});


App.PhotoRouter = Backbone.Router.extend({
    routes: {
        ':id': 'showPhoto',
        '': 'showPhoto'
    },
    showPhoto: function(id) {
        if (id !== null) {
            App.photomodel = new App.PhotoModel(id);
            App.photomodel.fetch({
                success: function() {
                    $('#error-wrapper').hide();
                    $('#photo-wrapper').show();
                    $('#photo-info-wrapper').show();
                    App.photoView = new App.PhotoView({model: App.photomodel});
                    App.orderView = new App.OrderView({model: App.photomodel});
                    App.photoTitleView = new App.TitleView({model: App.photomodel});
                    App.photoDescrView = new App.DescriptionView({model: App.photomodel});
                    },
                error: function() {
                        $('#photo-wrapper').hide();
                        $('#photo-info-wrapper').hide();
                        $('#error-wrapper').show();
                        App.errorView = new App.ErrorView();
                    }
            });
        } else {
            $('#error-wrapper').show();
            $('#photo-wrapper').hide();
            $('#photo-info-wrapper').hide();
            App.errorView = new App.ErrorView();
        }

    },
});

$(function() {
    App.app = new App.GeneralView();
    App.hist = Backbone.history.start();
});

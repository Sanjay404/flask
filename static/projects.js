var app = angular.module('app', ['ngAnimate'])

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('//');
  $interpolateProvider.endSymbol('//');
});


app.controller('mainCtrl', function($scope) {
  $scope.boxes = [{
      name: 'Covid Face Mask Classifier',
      image: 'https://www.terpconnect.umd.edu/~sanjays/Personal-Website%20Externals/face_mask900x900edited.jpg',
      description: 'Implemented a LeNet computer-vision model that can classify humans based on whether or not they are wearing a face mask with 95% accuracy.',
      technologies: ["Python", "Keras Deep Learning", "Visual Studio", "Google Colaboratory"],
      link: "https://github.com/Sanjay404/Covid19-Face-Mask-Classifier"
    }, {
      name: 'HooHacks 2020',
      image: 'https://www.terpconnect.umd.edu/~sanjays/Personal-Website%20Externals/covid_900x900edited.jpg',
      technologies: ["Python", "Keras Deep Learning", "Google Cloud Platform/Google Colaboratory", "HTML/CSS/JavaScript", ],
      description: 'Built a website that visualized and alerted users of predicted Covid19 cases, estimated by our Keras deep learning time-series model, using GCPs Maps API. I specifically worked on coding an interface for our website with GCPs Maps API. In addition, I contributed to researching the deep learning model used in the group project. ',
      link: "https://github.com/sagars729/HooHacks20"
    },{
      name: 'Multi-Class Animal Classification',
      image: 'https://www.terpconnect.umd.edu/~sanjays/Personal-Website%20Externals/Animal-Class_Edited_900x900.jpg',
      technologies: ["Python", "Keras Deep Learning", "Jupyter Notebooks", "Google Colaboratory"],
      description: 'Developed a VGG19 multi-class computer-vision model that can classify images of animals into 10 different species with 75% validation accuracy.',
      link: "https://github.com/Sanjay404/Animal-Classification"
    },{
      name: 'This Website!',
      image: 'https://www.terpconnect.umd.edu/~sanjays/Personal-Website%20Externals/websiteIMG_900x900edited.jpg',
      technologies: ["HTML/CSS/JavaScript", "Amazon Web Services ", "AngularJS", "Flask"],
      description: 'Built a personal website using HTML, JavaScript, AngularJS, CSS, and the particles.js library. This website currently implements Flask as a backend and is hosted with AWS EC2, Nginx, and Gunicorn',
      link: "https://github.com/Sanjay404/Personal-Website"
    },
	  {
      name: 'Stock Prediction',
      image: 'https://www.terpconnect.umd.edu/~sanjays/Personal-Website%20Externals/stock900x900edited.jpg',
      technologies: ["Python", "Keras Deep Learning", "Visual Studio", ""],
      description: 'Implemented data visualization and developed a Deep Learning NLP Model to predict TSLA (Tesla) stock price using Keras Deep Learning API. Currently working on integrating sentiment analysis for effective stock prediction.',
      link: "https://github.com/Sanjay404/TESLA-KERAS-ANALYSIS"
    },
    /*{
    name: 'Playful',
    image: 'https://source.unsplash.com/b2-fBVrfx0o/900x900'
  }, {
    name: 'Grand',
    image: 'https://source.unsplash.com/Ixp4YhCKZkI/900x900'
  }, {
    name: 'Mist',
    image: 'https://source.unsplash.com/8BmNurlVR6M/900x900'
  }, {
    name: 'Sea',
    image: 'https://source.unsplash.com/6YqpFWWQsno/900x900'
  }, {
    name: 'Reach',
    image: 'https://source.unsplash.com/zFnk_bTLApo/900x900'
  }, {
    name: 'Awe',
    image: 'https://source.unsplash.com/j4PaE7E2_Ws/900x900'
  }, {
    name: 'Surf',
    image: 'https://source.unsplash.com/uohGiEVhWiQ/900x900'
  }, {
    name: 'Thrill',
    image: 'https://source.unsplash.com/ssrbaKvxaos/900x900'
  },*/
  ];

  $scope.selected = [];
  $scope.selectBox = function(item, position) {
    $scope.selected = [{
      item: item,
      position: position
    }];
    $scope.$apply();
  }
  $scope.clearSelection = function() {
    $scope.selected = [];
  }
})

app.directive('box', function() {
  return {
    restrict: 'E',
    scope: {},
    bindToController: {
      onSelect: "=",
      item: "="
    },
    controllerAs: 'box',
    controller: function() {
      var box = this;

      box.goFullscreen = function(e) {
        box.onSelect(box.item, e.target.getBoundingClientRect())
      }
    },
    link: function(scope, element) {
      element.bind('click', scope.box.goFullscreen)
      element.css({
        'background-image': 'url(' + scope.box.item.image + ')'
      })
    }
  }
})

app.directive('bigBox', function($timeout) {
  return {
    restrict: 'AE',
    scope: {},
    bindToController: {
      position: "=",
      selected: "=",
      onSelect: "="
    },
    controllerAs: 'box',
    controller: function() {
      var box = this;
    },
    link: function(scope, element) {
      var css = {}
      for (var key in scope.box.position) {
        css[key] = scope.box.position[key] + 'px';
      }

      element.css(css);

      $timeout(function() {
        element.css({
          top: '50%',
          left: '10%'
        })
        element.addClass('image-out');
      }, 200)

      $timeout(function() {
        element.css({
          width: '80%',
          height: '100%'
        })
      }, 500)

      $timeout(function() {
        element.addClass('show');
      }, 800)
    }
  }
})

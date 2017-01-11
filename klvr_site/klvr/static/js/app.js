var app = angular.module("klever", []);
 app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('//');
    $interpolateProvider.endSymbol('//');
  });
app.controller("kleverCtrl", function ($scope,$http,$window) {
    console.log("thas work")

    // TASK CREATING

    // TASK CREATION  - tags
    $scope.tagger =  null;
    $scope.tagline = null;
    $scope.tags = []
    $scope.tags_basket = []

    $scope.typeTags = function(text){   // taking a TAGS from API
        if(text!=''){
        $http.get("/api/tags/get/?format=json&search="+text).then(function(response) {
        $scope.tags = response.data
        console.log(response.data)
    });}}

    $scope.tags_basket_add = function(tag){
        $scope.tagline = ''
        $scope.tags_basket.push(tag)
        console.log($scope.tags_basket)
        colletc_tags()
    }
    $scope.tags_basket_add_new  = function(text){
        $scope.tagline = ''
        tag = {
            "id":-1,
            "tagname":text
        }
        $scope.tags_basket.push(tag)
        console.log($scope.tags_basket)
        colletc_tags()
    }


    $scope.tags_basket_remove = function(id){
    console.log(id)
    if(id==0){
      $scope.tags_basket.splice(id,id+1)
    }else{
    $scope.tags_basket.splice(id,id)
     console.log($scope.tags_basket)
    }
     colletc_tags()
    }


    $scope.IsSelected= function(tag){
        for(var i=0;i<$scope.tags_basket.length;i++){
            if($scope.tags_basket[i].id==tag.id){
                return false;
            }
        }
        return true
    }

    function colletc_tags(){
        $scope.tagger=''
         for(var i=0;i<$scope.tags_basket.length;i++){
            if($scope.tags_basket[i].id > 0){
                $scope.tagger+=$scope.tags_basket[i].id
            }else{
                $scope.tagger+=$scope.tags_basket[i].tagname
            }
            $scope.tagger+=","
        }
    }
    // TASK_EDIT
    $scope.is_edit = false;
    $scope.task_editable = function(){
        $scope.is_edit = !$scope.is_edit
    }
});

    //AJAX AULA 01
/*
 *var xhr = new XMLHttpRequest();
 *
 *xhr.open('GET','https://api.github.com/users/thiagos98');
 *xhr.send(null);
 *
 *xhr.onreadystatechange = function() {
 *  if(xhr.readyState === 4){// '4' significa quando a houve resposta para requisição
 *       console.log(JSON.parse(xhr.responseText));
 *   }
 *}
 */
/*
var minhaPromise = function(){
     return new Promise(function(resolve, reject){
        var xhr = new XMLHttpRequest();
        xhr.open('GET','https://api.github.com/users/thiagos98');
        xhr.send(null);

        xhr.onreadystatechange = function() {
            if(xhr.readyState === 4){
                if(xhr.status === 200){
                    resolve(JSON.parse(xhr.responseText));
                } else {
                    reject('Erro na requisição.');
                }
            }
        }
     });
}

minhaPromise()
    .then(function(response){
        console.log(response);
    })
    .catch(function(error){
        console.warn(error);
    });*/


axios.get('https://api.github.com/users/thiagos98')
    .then(function(response){
        console.log(response);
    })
    .catch(function(error){
        console.warn(error);
    });
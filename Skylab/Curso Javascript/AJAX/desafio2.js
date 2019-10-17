var inputElement = document.querySelector('#app input');
var btnElement = document.querySelector('#app button');
var listElement = document.querySelector('#app ul');

btnElement.onclick = function(){
    listElement.innerHTML = '';
    var user = inputElement.value;
    axios.get('https://api.github.com/users/' + user)
    .then(function(response){
        axios.get(response.data.repos_url)
            .then(function(response){
                var repos = response.data;
                for(repo of repos){
                    var repoElement = document.createElement('li');
                    var textListElement = document.createTextNode(repo.name);
                    repoElement.appendChild(textListElement);
                    listElement.appendChild(repoElement);
                }
            })
            .catch(function(error){
                console.log('erro 404');
            });
    })
    .catch(function(error){
        console.log('Erro 404');
    });
}


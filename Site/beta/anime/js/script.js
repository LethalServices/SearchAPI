async function search() {
    await fetch('http://127.0.0.1:1337/api/fmovies?search=' + document.querySelector('.query').value, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    }).then(response => {
            if (response.status != 200) {
                throw new Error(`HTTP ERROR:${response.status}`);
            }
            return response.json()
        }

    ).then(data => {
        document.getElementById('swag').innerHTML = "";
        for (let i = 0; i < data['Results'].length; i++) {
            Title = data['Results'][i]['Title']
            Poster = data['Results'][i]['Cover']
            Link = data['Results'][i]['link']
            ContentType = data['Results'][i]['Content-Type']
            document.getElementById('swag').innerHTML += `<tr><td><a href=${Poster}><img src=${Poster} alt="" width="75" height="75"></a></td><td><a href=${Link}>${Title}</a></td></tr>`;
        }
    }).catch(err => {
        console.log(err);
    })
}
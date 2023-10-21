let SearchType;
function ToggleType(value)
{
    SearchType = value;
    return SearchType;
}

async function search() {
    API_LINK = `http://127.0.0.1:7636/api/${SearchType}?search=${document.querySelector('.query').value}`;
    await fetch(API_LINK, {
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
        if(SearchType.includes("fmovies"))
        {
            for (let i = 0; i < data['Results'].length; i++) {
                Title = data['Results'][i]['Title']
                Poster = data['Results'][i]['Cover']
                Link = data['Results'][i]['link']
                ContentType = data['Results'][i]['Content-Type']
                Runtime = data['Results'][i]['Duration']
                Year = data['Results'][i]['Year']
                document.getElementById('swag').innerHTML += `<tr><td><a href=${Poster}><img src=${Poster} alt="" width="75" height="75"></a></td><td><a href=${Link}>${Title}(${Year})</a></td><td>${ContentType} <br>${Runtime} </td></tr>`;
            }
        }
        else
        {
            for (let i = 0; i < data['Results'].length; i++) {
                Title = data['Results'][i]['Title']
                Poster = data['Results'][i]['Cover']
                Link = data['Results'][i]['link']
                ContentType = data['Results'][i]['Content-Type']
                document.getElementById('swag').innerHTML += `<tr><td><a href=${Poster}><img src=${Poster} alt="" width="75" height="75"></a></td><td><a href=${Link}>${Title}</a></td><td>${ContentType} </td></tr>`;
            }
        }
        
        document.getElementById('pages').innerHTML = `
        <li onclick="searchPages('1');">1</li>
        <li onclick="searchPages('2');">2</li>
        <li onclick="searchPages('3');">3</li>
        <li class="next-arrow"><i class="fa fa-arrow-right" style="color: #976ee2;"></i></li>
        <li class="right-arrow" onclick="searchPages(${data['Last_Page']});">»</li>`
        console.log(data['Results']);
    }).catch(err => {
        console.log(err);
    })
}


async function searchPages(page) {
    await fetch(`${API_LINK}&page=${page}`, {
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
        if(SearchType.includes("fmovies"))
        {
            for (let i = 0; i < data['Results'].length; i++) {
                Title = data['Results'][i]['Title']
                Poster = data['Results'][i]['Cover']
                Link = data['Results'][i]['link']
                ContentType = data['Results'][i]['Content-Type']
                Runtime = data['Results'][i]['Duration']
                Year = data['Results'][i]['Year']
                document.getElementById('swag').innerHTML += `<tr><td><a href=${Poster}><img src=${Poster} alt="" width="75" height="75"></a></td><td><a href=${Link}>${Title}(${Year})</a></td><td>${ContentType} <br>${Runtime} </td></tr>`;
            }
        }
        else
        {
            for (let i = 0; i < data['Results'].length; i++) {
                Title = data['Results'][i]['Title']
                Poster = data['Results'][i]['Cover']
                Link = data['Results'][i]['link']
                ContentType = data['Results'][i]['Content-Type']
                document.getElementById('swag').innerHTML += `<tr><td><a href=${Poster}><img src=${Poster} alt="" width="75" height="75"></a></td><td><a href=${Link}>${Title}</a></td><td>${ContentType} </td></tr>`;
            }
        }
    }).catch(err => {
        console.log(err);
    })
}


 /* When the user clicks on the button, 
      toggle between hiding and showing the dropdown content */
      function Settings() {
        document.getElementById("myDropdown").classList.toggle("show");
      }
      
      // Close the dropdown if the user clicks outside of it
      window.onclick = function(event) {
        if (!event.target.matches('.dropbtn')) {
          var dropdowns = document.getElementsByClassName("dropdown-content");
          var i;
          for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
              openDropdown.classList.remove('show');
            }
          }
        }
      }


       /* When the user clicks on the button, 
      toggle between hiding and showing the dropdown content */
      function advOptions() {
        document.getElementById("myDropdown1").classList.toggle("show");
      }
      
      // Close the dropdown if the user clicks outside of it
      window.onclick = function(event) {
        if (!event.target.matches('.dropbtn')) {
          var dropdowns = document.getElementsByClassName("dropdown-content");
          var i;
          for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
              openDropdown.classList.remove('show');
            }
          }
        }
      }
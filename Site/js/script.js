let query = document.querySelector('.query');

function search() {
    if (query.value != "") {
        let url = "http://127.0.0.1:1337/api/fmovies?search=" + query.value;
        window.open(url, '_self')
    } else {
        window.open("https://lethals.org", '_self')
    }
}
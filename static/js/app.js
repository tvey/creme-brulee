const searchForm = document.getElementById('search');

searchForm.addEventListener('keyup', (event) => {
  const userInput = event.target.value;
  if (userInput) {
    let param = `q=${encodeURI(userInput)}`;
    fetchAPIData('search', param);
  } else {
    fetchAPIData('everything');
  }
  event.preventDefault();
});


async function fetchAPIData(route, param = null) {
  let url = `/${route}`;

  if (param) {
    url = `${url}?${param}`
  }

  fetch(url)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      showResult(data);
    })
    .catch(err => console.log(err));
}

function showResult(data) {
  const resultElem = document.getElementById('search-result');

  if (data.length) {
    let listItems = '';
    data.forEach(item => {
      let li = `<li class="list-group-item">${item.content}</li>`;
      listItems = listItems + li;
    });
    resultElem.innerHTML = listItems;
  }
}
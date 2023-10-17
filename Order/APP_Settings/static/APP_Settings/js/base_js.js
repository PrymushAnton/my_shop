let div_menu = document.querySelector('.settings')

let menu = document.createElement('div')
menu.className = 'dropdown-child'
menu.innerHTML += `<a href="/authorization_page/">Ввійдіть в акаунт</a>` +
                `<a href="/registration_page/">Зареєструватись</a>`
div_menu.appendChild(menu)

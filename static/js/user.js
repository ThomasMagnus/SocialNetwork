document.addEventListener('DOMContentLoaded', () => {
    'use strict'

    const userMenuArrow = document.querySelector('.user__menu_arrow'),
          userList = document.querySelector('.user__list'),
          userArrow = document.querySelector('.user__menu_arrow i');

    const showUserMenu = () => {
        userList.classList.toggle('active')
        userArrow.classList.toggle('active__arrow')
    }

    userMenuArrow.addEventListener('click', showUserMenu)
})
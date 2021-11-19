document.addEventListener('DOMContentLoaded', () => {
    const logout = document.querySelector('#logout')

    const logoutUser = e => {
        e.preventDefault()

        fetch('http://localhost:8000/users/')
            .then(response => {
                document.location = response.url
            })
    }

    logout.addEventListener('click', logoutUser)
})
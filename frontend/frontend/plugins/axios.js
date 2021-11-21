export default function ({ $axios, redirect }) {
  $axios.onRequest((config) => {
    // Add Auth Token if saved in local storage
    if (process.client) {
      const user = localStorage.getItem('user')
      if (user) {
        const token = JSON.parse(user).token
        if (token) {
          config.headers.Authorization = `Token ${token}`
        }
      }
    }
  })
}

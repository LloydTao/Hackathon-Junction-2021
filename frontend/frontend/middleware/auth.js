export default function ({ route, store, redirect }) {
  let token = store.state.user.token
  if (token === undefined && process.client) {
    // If User token undefined, try to get one from local storage
    let user = localStorage.getItem('user')
    if (user) {
      user = JSON.parse(user)
      if (user.token) {
        // User exists in local storage, load user and return
        store.commit('user/set', user)
        token = user.token
      }
    }
  }
  if (route.path !== '/login' && token === undefined) {
    // User does not exist, send to login
    return redirect({ path: '/login' })
  }
}

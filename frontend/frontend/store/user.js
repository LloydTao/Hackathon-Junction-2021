export const state = () => ({
  id: -1,
  name: undefined,
  token: undefined,
})

export const mutations = {
  set(state, user) {
    state.id = user.id
    state.name = user.name
    state.token = user.token
    if (process.client) {
      localStorage.setItem('user', JSON.stringify(user))
    }
  },
}

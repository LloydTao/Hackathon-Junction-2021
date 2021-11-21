<template>
  <section class="container mx-auto">
    <div class="w-full rounded-lg">
      <div class="w-full overflow-x-auto">
        <div class="flex flex-col justify-center sm:py-12">
          <div class="p-10 xs:p-0 mx-auto md:w-full md:max-w-md">
            <h1 class="font-bold text-center text-2xl mb-5">Login</h1>
            <div
              class="bg-white shadow w-full rounded-lg divide-y divide-gray-200"
            >
              <div class="px-5 py-7">
                <label class="font-semibold text-sm text-gray-600 pb-1 block"
                  >Username</label
                >
                <input
                  v-model="username"
                  type="text"
                  class="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full"
                />
                <label class="font-semibold text-sm text-gray-600 pb-1 block"
                  >Password</label
                >
                <input
                  v-model="password"
                  type="password"
                  class="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full"
                />
                <div
                  v-if="error"
                  class="
                    border
                    rounded-lg
                    font-semibold
                    px-3
                    py-2.5
                    mt-1
                    mb-5
                    text-sm text-white
                    w-full
                    bg-red-500
                  "
                >
                  Incorrect Username or Password
                </div>
                <button
                  type="button"
                  class="
                    transition
                    duration-200
                    bg-blue-500
                    hover:bg-blue-600
                    focus:bg-blue-700
                    focus:shadow-sm
                    focus:ring-4
                    focus:ring-blue-500
                    focus:ring-opacity-50
                    text-white
                    w-full
                    py-2.5
                    rounded-lg
                    text-sm
                    shadow-sm
                    hover:shadow-md
                    font-semibold
                    text-center
                    inline-block
                  "
                  @click="login"
                >
                  <span class="inline-block mr-2">Login</span>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    class="w-4 h-4 inline-block"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M17 8l4 4m0 0l-4 4m4-4H3"
                    />
                  </svg>
                </button>
              </div>
              <div class="py-5">
                <div class="grid grid-cols-2 gap-1">
                  <div class="text-center sm:text-left whitespace-nowrap">
                    <button
                      class="
                        transition
                        duration-200
                        mx-5
                        px-5
                        py-4
                        cursor-pointer
                        font-normal
                        text-sm
                        rounded-lg
                        text-gray-500
                        hover:bg-gray-100
                        focus:outline-none
                        focus:bg-gray-200
                        focus:ring-2
                        focus:ring-gray-400
                        focus:ring-opacity-50
                        ring-inset
                      "
                      @click="forgot_password"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        class="w-4 h-4 inline-block align-text-top"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M8 11V7a4 4 0 118 0m-4 8v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2z"
                        />
                      </svg>
                      <span class="inline-block ml-1">Forgot Password</span>
                    </button>
                  </div>
                  <div class="text-center sm:text-right whitespace-nowrap">
                    <button
                      class="
                        transition
                        duration-200
                        mx-5
                        px-5
                        py-4
                        cursor-pointer
                        font-normal
                        text-sm
                        rounded-lg
                        text-gray-500
                        hover:bg-gray-100
                        focus:outline-none
                        focus:bg-gray-200
                        focus:ring-2
                        focus:ring-gray-400
                        focus:ring-opacity-50
                        ring-inset
                      "
                      @click="help"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        class="w-4 h-4 inline-block align-text-bottom"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M18.364 5.636l-3.536 3.536m0 5.656l3.536 3.536M9.172 9.172L5.636 5.636m3.536 9.192l-3.536 3.536M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-5 0a4 4 0 11-8 0 4 4 0 018 0z"
                        />
                      </svg>
                      <span class="inline-block ml-1">Help</span>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      error: false,
    }
  },
  created() {
    if (process.client) {
      const user = localStorage.getItem('user')
      if (user) {
        const token = JSON.parse(user).token
        if (token) {
          this.$router.push({ path: '/' })
        }
      }
    }
  },
  methods: {
    forgot_password() {
      alert('Unlucky!')
    },
    help() {
      alert("There's no help in the game of life")
    },
    async login() {
      this.error = false
      const token = (await this.$axios.get('/api/accounts/csrf/')).data.token
      this.$axios
        .post(
          '/api/accounts/login/',
          {
            username: this.username,
            password: this.password,
            csrfmiddlewaretoken: token,
          },
          {
            headers: { 'X-CSRFToken': token },
          }
        )
        .then(({ data }) => {
          this.$store.commit('user/set', {
            id: data.id,
            name: data.username,
            token: data.token,
          })
          this.$router.push({ path: '/' })
        })
        .catch((response) => {
          this.error = true
        })
    },
  },
}
</script>

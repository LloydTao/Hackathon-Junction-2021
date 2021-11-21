<template>
  <div>
    <div class="rounded-xl bg-white overflow-hidden bg-opacity-50">
      <table class="w-full border rounded shadow-md rounded-2xl bg-opacity-0">
        <thead>
          <tr class="text-left text-gray-900 bg-blue-500 bg-opacity-40">
            <th class="text-gray-50 px-4 py-3">User</th>
            <th class="text-gray-50 px-4 py-3">Content</th>
            <th class="text-gray-50 px-4 py-3">Actions</th>
          </tr>
        </thead>
        <tbody class="bg-white bg-opacity-40">
          <tr
            v-for="message in messages"
            :key="message"
            class="items-center text-gray-700 border-b"
          >
            <template v-if="!message.flagged">
              <td class="flex flex-1 items-center px-4 py-3">
                <div class="flex items-center text-sm">
                  <div class="relative w-8 h-8 mr-3 rounded-full md:block">
                    <img
                      class="object-cover w-full h-full rounded-full"
                      src="https://placekitten.com/160/160"
                      alt=""
                      loading="lazy"
                    />
                    <div
                      class="absolute inset-0 rounded-full shadow-inner"
                      aria-hidden="true"
                    ></div>
                  </div>
                  <div>
                    <NuxtLink
                      class="font-semibold text-black hover:underline"
                      :to="{
                        name: 'users-id',
                        params: { id: message.sender.id },
                      }"
                    >
                      <p>{{ message.sender.username }}</p>
                    </NuxtLink>
                  </div>
                </div>
              </td>
              <td class="px-4 py-3 text-sm">{{ message.content }}</td>
              <td class="px-4 py-3">
                <div class="flex items-center space-x-3">
                  <div
                    class="
                      text-gray-50
                      bg-blue-500
                      hover:bg-blue-400
                      h-5
                      w-5
                      rounded-full
                      transition
                      duration-100
                      cursor-pointer
                    "
                    @click="sendFlag(message.id)"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="p-1 h-5 w-5"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                    >
                      <path
                        d="M2 10.5a1.5 1.5 0 113 0v6a1.5 1.5 0 01-3 0v-6zM6 10.333v5.43a2 2 0 001.106 1.79l.05.025A4 4 0 008.943 18h5.416a2 2 0 001.962-1.608l1.2-6A2 2 0 0015.56 8H12V4a2 2 0 00-2-2 1 1 0 00-1 1v.667a4 4 0 01-.8 2.4L6.8 7.933a4 4 0 00-.8 2.4z"
                      />
                    </svg>
                  </div>
                  <div
                    class="
                      text-gray-50
                      bg-red-500
                      hover:bg-red-400
                      h-5
                      w-5
                      rounded-full
                      transition
                      duration-100
                      cursor-pointer
                    "
                    @click="sendLike(message.id)"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="p-1 h-5 w-5"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                    >
                      <path
                        fill-rule="evenodd"
                        d="M3 6a3 3 0 013-3h10a1 1 0 01.8 1.6L14.25 8l2.55 3.4A1 1 0 0116 13H6a1 1 0 00-1 1v3a1 1 0 11-2 0V6z"
                        clip-rule="evenodd"
                      />
                    </svg>
                  </div>
                </div>
              </td>
            </template>
          </tr>
        </tbody>
      </table>
    </div>

    <form class="flex space-x-5 py-3 mt-1">
      <input
        id="message"
        class="
          flex flex-1
          appearance-none
          border
          rounded-lg
          shadow-md
          w-full
          py-2
          px-3
          text-gray-700
          leading-tight
          focus:outline-none focus:shadow-outline
          bg-opacity-70
        "
        type="text"
        placeholder="Type a message..."
      />
      <button
        class="
          bg-blue-500
          hover:bg-blue-700
          text-white
          font-bold
          py-2
          px-4
          rounded-lg
          shadow-md
          focus:outline-none focus:shadow-outline
        "
        type="button"
      >
        Send
      </button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      messages: [],
      errors: [],
    }
  },
  methods: {
    async getMessages() {
      this.error = false
      const token = (await this.$axios.get('/api/accounts/csrf/')).data.token
      this.$axios
        .get(
          '/api/rooms/1/messages/',
          {
            csrfmiddlewaretoken: token,
          },
          {
            headers: { 'X-CSRFToken': token },
          }
        )
        .then(({ data }) => {
          this.messages = data
        })
        .catch((response) => {
          this.error = true
        })
    },
    async sendLike(id) {
      this.error = false
      const token = (await this.$axios.get('/api/accounts/csrf/')).data.token
      this.$axios
        .post(
          `/api/messages/${id}/like/`,
          {
            csrfmiddlewaretoken: token,
          },
          {
            headers: { 'X-CSRFToken': token },
          }
        )
        .catch((response) => {
          this.error = true
        })
    },
    async sendFlag(id) {
      this.error = false
      const token = (await this.$axios.get('/api/accounts/csrf/')).data.token
      this.$axios
        .post(
          `/api/messages/${id}/flag/`,
          {
            csrfmiddlewaretoken: token,
          },
          {
            headers: { 'X-CSRFToken': token },
          }
        )
        .catch((response) => {
          this.error = true
        })
    },
  },
  created() {
    this.getMessages()
  },
}
</script>

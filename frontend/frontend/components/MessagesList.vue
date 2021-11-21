<template>
  <section class="container mx-auto">
    <div class="w-full rounded-lg">
      <div class="w-full overflow-x-auto">
        <h1 class="text-xl text-gray-900 font-semibold mt-3">Messages</h1>
        <table class="w-full border rounded shadow-md mt-5">
          <thead>
            <tr class="text-left text-gray-900 bg-blue-500">
              <th class="text-gray-50 px-4 py-3">User</th>
              <th class="text-gray-50 px-4 py-3">Content</th>
              <th class="text-gray-50 px-4 py-3">Created</th>
              <th class="text-gray-50 px-4 py-3">Hidden</th>
              <th class="text-gray-50 px-4 py-3">Likes</th>
              <th class="text-gray-50 px-4 py-3">Flags</th>
            </tr>
          </thead>
          <tbody class="bg-white">
            <tr
              v-for="message in messages"
              :key="message"
              class="text-gray-700"
            >
              <td class="px-4 py-3">
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
                        params: { id: message.user },
                      }"
                    >
                      <span> {{ message.user }} </span>
                    </NuxtLink>
                  </div>
                </div>
              </td>
              <td class="px-4 py-3 text-sm">{{ message.content }}</td>
              <td class="px-4 py-3 text-sm">{{ message.created }}</td>
              <td class="px-4 py-3 text-xs">
                <span
                  v-if="message.flagged"
                  class="
                    px-2
                    py-1
                    font-semibold
                    leading-tight
                    text-red-700
                    bg-red-100
                    rounded-sm
                  "
                >
                  Yes
                </span>
                <span
                  v-else
                  class="
                    px-2
                    py-1
                    font-semibold
                    leading-tight
                    text-gray-700
                    bg-gray-100
                    rounded-sm
                  "
                >
                  No
                </span>
              </td>
              <td class="px-4 py-3 text-sm">{{ message.likes }}</td>
              <td class="px-4 py-3 text-sm">{{ message.flags }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      messages: [],
      errors: [],
    }
  },
  created() {
    this.getMessages()
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
  },
}
</script>

<template>
  <section class="container mx-auto">
    <div class="w-full rounded-lg">
      <div class="w-full overflow-x-auto">
        <h1 class="text-xl text-gray-900 font-semibold mt-3">Messages</h1>
        <table class="w-full font-mono mt-5">
          <thead>
            <tr
              class="
                font-semibold
                text-left text-gray-900
                bg-gray-100
                uppercase
              "
            >
              <th class="px-4 py-3">User</th>
              <th class="px-4 py-3">Content</th>
              <th class="px-4 py-3">Created</th>
              <th class="px-4 py-3">Hidden</th>
              <th class="px-4 py-3">Likes</th>
              <th class="px-4 py-3">Flags</th>
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
                        params: { id: message.user.id },
                      }"
                    >
                      <span> {{ message.user.username }} </span>
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
      messages: [
        {
          id: 1,
          user: {
            id: 1,
            username: 'lloydtao',
            role: 'Player',
            created: '2021-11-16',
            rating: 1000,
            status: 1,
          },
          content: 'I feel like I hit a learning roadblock',
          created: '2021-11-16',
          flagged: 0,
          likes: 32,
          flags: 1,
        },
        {
          id: 2,
          user: {
            id: 1,
            username: 'lloydtao',
            role: 'Player',
            created: '2021-11-16',
            rating: 1000,
            status: 1,
          },
          content: 'Is it possible to use Mongo DB with Django',
          created: '2021-11-17',
          flagged: 0,
          likes: 4,
          flags: 0,
        },
        {
          id: 3,
          user: {
            id: 1,
            username: 'lloydtao',
            role: 'Player',
            created: '2021-11-16',
            rating: 1000,
            status: 1,
          },
          content:
            'Would anyone be interested in joining a small community of developers?',
          created: '2021-11-18',
          flagged: 0,
          likes: 25,
          flags: 3,
        },
        {
          id: 4,
          user: {
            id: 1,
            username: 'lloydtao',
            role: 'Player',
            created: '2021-11-16',
            rating: 1000,
            status: 1,
          },
          content: 'bitch',
          created: '2021-11-19',
          flagged: 1,
          likes: 0,
          flags: 0,
        },
      ],
    }
  },
}
</script>
